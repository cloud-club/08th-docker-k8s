## 실습 1.

지난 번 과제 관련 해설임

```bash
# 1. 이미지 다운로드 (pull)
docker pull nginx:alpine

# 2. 컨테이너 실행 (run)
docker run -d -p 8080:80 --name my-nginx nginx:alpine
# -d: 백그라운드 실행 (detached)
# -p: 포트 매핑 (호스트:컨테이너) # PORTS 컬럼: "0.0.0.0:8080->80/tcp" (실제 매핑됨)
# --name: 컨테이너 이름 지정

# 3. 실행 중인 컨테이너 확인
docker ps

# 4. 브라우저에서 localhost:8080 접속 확인

# 5. 컨테이너 내부 접속
docker exec -it my-nginx sh
# -i: 상호작용 모드
# -t: 터미널 할당
# 내부에서: ls /usr/share/nginx/html

# 6. 컨테이너 로그 확인
docker logs my-nginx

# 7. 컨테이너 중지 및 삭제
docker stop my-nginx
docker rm my-nginx
```


## 실습 2
도커 이미지 만들고 run

docker build -t "이미지이름:태그" -f 경로긴 함(현재 디렉터리에 있음 안써도 무방)

# 현재 디렉토리의 Dockerfile로 이미지 빌드
docker build -t my-web-app:v1.0 .

# 다양한 태그 생성
docker tag my-web-app:v1.0 my-web-app:latest
docker tag my-web-app:v1.0 my-web-app:prod

# 이미지 목록 확인
docker images | grep my-web-app

# 컨테이너 실행 테스트
docker run -d -p 8080:80 --name test-app my-web-app:latest


k8s 나 docker compose 같은 곳에서
expose 유용 

밑에 같은 경우 2개 다 일치 하는 게 매우 중요함니다~
docker-compose 없음 이걸로 자동 매핑하므로
k8s는 자동 매핑은 X이나 힌트

```yaml
# EXPOSE 덕분에 더 간편한 설정
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-app
spec:
  template:
    spec:
      containers:
      - name: app
        image: my-app:latest
        # ports 섹션에서 EXPOSE 정보 활용 가능
        ports:
        - containerPort: 80  # EXPOSE 80과 매칭
```
