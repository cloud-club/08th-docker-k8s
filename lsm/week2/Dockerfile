# Python 3.12 베이스 이미지 사용
FROM python:3.12-slim

# 작업 디렉토리 설정
WORKDIR /app

# 시스템 의존성 설치 (이미지 처리 라이브러리)
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

# requirements.txt 복사 및 패키지 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 애플리케이션 파일 복사
COPY app/app-auto.py app.py

# 필요한 디렉토리 및 데이터 복사
COPY fashion_multimodal_db ./fashion_multimodal_db

# Streamlit 포트 노출
EXPOSE 8501

# Streamlit 설정
ENV STREAMLIT_SERVER_PORT=8501
ENV STREAMLIT_SERVER_ADDRESS=0.0.0.0

# 앱 실행
CMD ["streamlit", "run", "app.py", "--server.address", "0.0.0.0"]