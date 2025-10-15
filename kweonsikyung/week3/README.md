### Summary

1. 로컬 실행 환경 구성 및 전환

   - `kubectl config get-contexts`
   - `kubectl config use-context docker-desktop`
   - `docker context ls`
   - `docker context use desktop-linux`

2. Nginx 공식 이미지 다운로드 및 컨테이너 실행

   - `docker pull nginx`
   - `docker run --name k8s-study -d -p 8000:80 nginx`
   - `docker ps`

3. 실행 중인 컨테이너 접속 및 수동 변경

   - `docker exec -it k8s-study bash`
   - `apt-get update && apt-get install -y vim`
   - `echo "<h1>Kweon Sikyung</h1>" > /usr/share/nginx/html/index.html`
   - `exit`

4. Dockerfile 작성 및 사용자 정의 이미지 빌드

   - `(Dockerfile 파일 생성 및 내용 작성)`
   - `docker build -t k8s-study-nginx .`

5. 사용자 정의 이미지 기반의 컨테이너 실행

   - `docker run --name k8s-study-nginx-app -d -p 8002:80 k8s-study-nginx`

6. 결과
   - `curl http://localhost:8002`

### Dockerfile 작성

```
# 1. 베이스 이미지 선택 (어떤 이미지에서 시작할지)
FROM nginx:latest

# 2. 실행할 명령어 정의 (이미지 안에 설치하거나 수정할 내용)
RUN apt-get update \
 && apt-get install -y vim \
 && echo "<h1>Kweon Sikyung</h1>" > /usr/share/nginx/html/index.html \
 && rm -rf /var/lib/apt/lists/*

# 3. 노출 포트 명시
EXPOSE 80

```
