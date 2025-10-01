import streamlit as st 
import open_clip
import torch
from PIL import Image
import numpy as np
import chromadb
import logging
from transformers import AutoImageProcessor, AutoModelForObjectDetection
from chromadb.utils.embedding_functions import OpenCLIPEmbeddingFunction
from chromadb.utils.data_loaders import ImageLoader
from pathlib import Path 

# 로깅 설정
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# 의류 카테고리 - 컬렉션명 매핑 정의
YOLO_TO_COLLECTION_MAPPING = {
    'top': 'upper_crop',
    'outer': 'outer_crop',
    'bottom': ['pants_crop', 'skirts_crop'],
    'dress': 'skirts_crop',
}

# 의류 detection yolo 모델 불러옴
@st.cache_resource
def load_detection_model():
    device = 'cpu'
    if torch.cuda.is_available():
        device = torch.device('cuda')
    elif torch.backends.mps.is_available():
        device = torch.device('mps')
    
    ckpt = 'yainage90/fashion-object-detection'
    image_processor = AutoImageProcessor.from_pretrained(ckpt)
    model = AutoModelForObjectDetection.from_pretrained(ckpt).to(device)
    return image_processor, model, device

# detection 영역에 맞게 이미지 크롭
def crop_image(image, box):
    width, height = image.size
    x1, y1, x2, y2 = [int(coord) for coord in box]
    x1, y1 = max(0, x1), max(0, y1)
    x2, y2 = min(width, x2), min(height, y2)
    return image.crop((x1, y1, x2, y2))

# 이미지 속 의류 영역을 detection 하여 크롭하는 함수
def detect_and_crop_fashion_items(image):
    image_processor, model, device = load_detection_model()
    
    with torch.no_grad():
        # 이미지 전처리 
        inputs = image_processor(images=[image], return_tensors="pt")
        # 모델 예측
        outputs = model(**inputs.to(device))
        target_sizes = torch.tensor([[image.size[1], image.size[0]]])
        results = image_processor.post_process_object_detection(outputs, 
                                                             threshold=0.4, 
                                                             target_sizes=target_sizes)[0]
        
        detected_items = []
        # 감지된 객체 처리
        for score, label, box in zip(results["scores"], results["labels"], results["boxes"]):
            label_name = model.config.id2label[label.item()].lower()
            score = score.item()
            box = [i.item() for i in box]
            
            cropped_image = crop_image(image, box)
            
            detected_items.append({
                'image': cropped_image,
                'label': label_name,
                'score': score,
                'box': box
            })
            st.session_state['detected_items'] = detected_items
            logger.debug(f"Detected {label_name} with confidence {score:.3f}")
            
        return detected_items

# 카테고리에 해당하는 컬렉션 반환
def get_collection_for_item(label):
    if label in YOLO_TO_COLLECTION_MAPPING:
        return YOLO_TO_COLLECTION_MAPPING[label]
    return None

# clip model 로드
@st.cache_resource
def load_clip_model():
    model, preprocess_val, _ = open_clip.create_model_and_transforms('hf-hub:Marqo/marqo-fashionSigLIP')
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = model.to(device)
    return model, preprocess_val, device

# 유사 아이템 찾는 함수
def search_similar_items(image, top_k=12, select_label='top'):
    logger.debug("=== Starting search_similar_items ===")
    
    try:
        #DB 설정
        client = chromadb.PersistentClient(path="./fashion_multimodal_db")
        embedding_function = OpenCLIPEmbeddingFunction()
        
        model, preprocess_val, device = load_clip_model()
        all_results = []
        
        # 비교할 컬렉션 설정
        collection_name = get_collection_for_item(select_label)
                
        if isinstance(collection_name, list):
            collections = [client.get_collection(name=name, embedding_function=embedding_function) 
                         for name in collection_name]
        else:
            collections = [client.get_collection(name=collection_name, embedding_function=embedding_function)]
        
        # 이미지 전처리 및 특징 추출
        img_processed = preprocess_val(image).unsqueeze(0)
        img_tensor = img_processed.to(device)
            
        with torch.no_grad():
            # 이미지 임베딩
            image_features = model.encode_image(img_tensor)
            image_features = image_features / image_features.norm(dim=-1, keepdim=True)
            features = image_features
            
            # numpy로 변환하고 list로 최종 변환
            features_np = features.cpu().numpy()
            features_1d = features_np.squeeze()
            embedding_list = features_1d.tolist()

            # collection query 수행     
            for collection in collections:
                try:
                    results = collection.query(
                        query_embeddings=embedding_list,
                        n_results=min(top_k, collection.count()),
                        include=['metadatas', 'distances']
                    )
                    
                    if results and 'metadatas' in results and results['metadatas']:
                        for metadata, distance in zip(results['metadatas'][0], results['distances'][0]):
                            similarity_score = 1 / (1 + distance)
                            item_data = metadata.copy()
                            item_data['similarity_score'] = similarity_score * 100
                            item_data['detected_label'] = select_label
                            all_results.append(item_data)
                
                except Exception as e:
                    logger.error(f"Error searching in collection: {str(e)}")
                    continue
        # 유사도 순 정렬
        all_results.sort(key=lambda x: x['similarity_score'], reverse=True)
        return all_results[:top_k]
            
    except Exception as e:
        logger.error(f"Error in search_similar_items: {str(e)}")
        logger.exception("Detailed error:")
        return []

# 감지된 의류 영역에 따른 결과 보여주는 함수
def show_detection_results(image, detected_items):
    st.subheader("감지된 패션 아이템:")
    
    cols = st.columns(len(detected_items))
    for idx, item in enumerate(detected_items):
        with cols[idx]:
            st.image(item['image'], caption=f"{item['label']} ({item['score']:.2%})")

# 카테고리별 결과 필터링
def filter_results_by_category(selected_category, similar_items):
    """선택된 카테고리에 따라 보여줄 결과를 필터링"""
    category_mapping = {
        'top': ['top', 'outer'],
        'outer': ['top', 'outer'],
        'bottom': ['bottom', 'dress'],
        'dress': ['bottom', 'dress']
    }
    
    if selected_category in category_mapping:
        valid_categories = category_mapping[selected_category]
        filtered_items = [
            item for item in similar_items 
            if item['detected_label'] in valid_categories
        ]
        return filtered_items
    return similar_items

# 유사 아이템 표시 함수 (이미지 제거)
def show_similar_items_by_category(similar_items, selected_category=None):
    if not similar_items:
        st.warning("유사한 아이템을 찾지 못했습니다.")
        return
    if selected_category:
        similar_items = filter_results_by_category(selected_category, similar_items)

    categorized_items = {
        '전체': similar_items,
        'top': [item for item in similar_items if item['detected_label'] == 'top'],
        'outer': [item for item in similar_items if item['detected_label'] == 'outer'],
        'bottom': [item for item in similar_items if item['detected_label'] in ['bottom', 'pants', 'skirts']],
        'dress': [item for item in similar_items if item['detected_label'] == 'dress']
    }

    # 카테고리별 탭 표시
    tabs = st.tabs(['전체', 'Top', 'Outer', 'Bottom', 'Dress'])
    
    for tab, (category, items) in zip(tabs, categorized_items.items()):
        with tab:
            if not items:
                st.info(f"{category} 카테고리에서 검색된 아이템이 없습니다.")
                continue
                
            items_per_row = 3
            for i in range(0, len(items), items_per_row):
                cols = st.columns(items_per_row)
                for j, col in enumerate(cols):
                    if i + j < len(items):
                        item = items[i + j]
                        with col:
                            try:
                                # 이미지 표시 부분 제거 - 텍스트 정보만 표시
                                st.markdown(f"**유사도**: {item['similarity_score']:.1f}%")
                                st.write(f"카테고리: {item.get('category', '알 수 없음')}")
                                
                                name = item.get('name', '알 수 없음')
                                if len(name) > 50:
                                    name = name[:47] + "..."
                                st.write(f"이름: {name}")
                                
                                # 이미지 URL이 있다면 링크로 표시
                                if 'image_url' in item:
                                    st.markdown(f"[이미지 보기]({item['image_url']})")
                                
                                with st.expander("상세 정보"):
                                    if 'uri' in item:
                                        st.text(f"경로: {item.get('uri', '경로 없음')}")
                                
                                st.divider()
                                
                            except Exception as e:
                                logger.error(f"Error displaying item: {str(e)}")
                                st.error("이 아이템을 표시하는 중 오류가 발생했습니다")

def handle_file_upload():
    """파일 업로드 처리 함수"""
    if st.session_state.uploaded_file is not None:
        image = Image.open(st.session_state.uploaded_file).convert('RGB')
        st.session_state.image = image
        st.session_state.upload_state = 'image_uploaded'
        st.rerun()

def main():
    """메인 애플리케이션 함수"""
    st.title("패션 이미지 검색")

    if 'image' not in st.session_state:
        st.session_state.image = None
    if 'upload_state' not in st.session_state:
        st.session_state.upload_state = 'initial'
    if 'search_clicked' not in st.session_state:
        st.session_state.search_clicked = False
    if 'search_results' not in st.session_state:
        st.session_state.search_results = None

    if st.session_state.upload_state == 'initial':
        uploaded_file = st.file_uploader("이미지 업로드", type=['png', 'jpg', 'jpeg'], 
                                       key='uploaded_file', on_change=handle_file_upload)

    if st.session_state.image is not None:
        st.image(st.session_state.image, caption="업로드된 이미지")

        if st.session_state.search_results is None:
                with st.spinner("패션 아이템 감지 중..."):
                    detected_items = detect_and_crop_fashion_items(st.session_state.image)
                    if detected_items:
                        show_detection_results(st.session_state.image, detected_items)

                # 감지된 아이템들 중 비교를 원하는 아이템 선택
                if 'detected_items' in st.session_state:
                    detected_labels = [f"{item['label']} ({item['score']:.1%})" for item in st.session_state['detected_items']]
                    selected_label = st.selectbox("검색할 요소를 선택하세요:", ["선택하세요"]+detected_labels, key = "selected label")

                    if selected_label != "선택하세요":
                        selected_item = next((item for item in st.session_state['detected_items'] if 
                            f"{item['label']} ({item['score']:.1%})" == selected_label), None)
                    else:
                        selected_item = None
                else:
                    st.warning("감지된 아이템이 없습니다.")
                    selected_item = None

        # 이미지 표시 및 검색
        search_clicked = False
        if selected_item:
            search_col1, search_col2 = st.columns([1, 2])
            with search_col1:
                search_clicked = st.button("패션 아이템 검색", 
                                     key='search_button',
                                     type="primary")
            
            with search_col2:
                num_results = st.slider("검색 결과 수:", 
                                      min_value=3, 
                                      max_value=21, 
                                      value=12,
                                      step=3,
                                      key='num_results')

        if search_clicked:
            st.session_state.search_results = None
            
        if search_clicked or st.session_state.search_clicked:
            st.session_state.search_clicked = True
            with st.spinner("유사한 아이템 검색 중..."):
                        cropped_image = selected_item['image']
                        similar_items = search_similar_items(
                            cropped_image,
                            top_k=num_results,
                            select_label = selected_item['label']
                        )
                        if similar_items:
                            show_similar_items_by_category(similar_items, selected_label)
                        else:
                            st.warning("유사한 아이템을 찾지 못했습니다.")
            
            
    # 새로운 검색
    if st.button("새로운 검색 시작", key='new_search'):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

if __name__ == "__main__":
    main()