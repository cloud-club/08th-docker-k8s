# [WEEK2] Docker 설치 후 Nginx 이미지를 pull하여 서버를 실행하기

### 수행 과정 요약
1. ~~Docker 설치~~
2. Ngnix 이미지 pull
   `docker pull nginx:alpine`
4. Nginx 컨테이너 실행
   ```
   docker image inspect nginx:alpine --format '{{.Config.ExposedPorts}} # map[80/tcp:{}]
   docker run -d -p 8080:80 --name demo-nginx
   ```
6. 서버 접속 확인
7. Nginx 컨테이너 종료 후 삭제
   ```
   docker stop demo-nginx
   docker rm demo-nginx
   ```

### 수행 과정 이미지 첨부
![hands_on_0](./src/hands_on_0.png)  

![hands_on_1](./src/hands_on_1.png)  

![hands_on_2](./src/hands_on_2.png)  
