# 베이스 이미지 지정 (Docker Hub가 기본 레지스트리)
FROM nginx:alpine
# FROM docker.io/library/nginx:alpine
# docker.io     - Docker Hub 레지스트리
# library       - 공식 이미지 네임스페이스
# nginx         - 이미지 이름
# alpine        - 태그 (버전)

# 작성자 정보 (선택사항)
LABEL maintainer="your-email@company.com"

# HTML 파일들을 컨테이너로 복사
COPY html/ /usr/share/nginx/html/

# 포트 노출 (문서화 목적) <- run 할때 포트기재해주는 것만 의미
EXPOSE 80