## 1. 실습 목적
본 실습의 목적: Docker Desktop을 설치하고, Nginx 컨테이너를 실행하여 정상적으로 웹 서버가 구동되는 것을 확인하는 것

---

## 2. 실습 환경
- 운영체제(OS): macOS  
- 도구(Tool): Docker Desktop
- 
---

## 3. 진행 과정

### 3.1 Docker Desktop 설치 및 실행 확인
- Docker Desktop을 설치 후 실행 (기존에 깔려 있었음)
- 좌측 하단에 **Engine running** 상태가 표시되어 도커 엔진이 정상적으로 동작함을 확인
<img width="1382" height="832" alt="스크린샷 2025-09-24 오후 5 13 33" src="https://github.com/user-attachments/assets/adb4fb28-1a5d-44bb-aaf7-8064b7cf9f60" />

---

### 3.3 Nginx 컨테이너 실행
1. **이미지 다운로드**
   ```bash
   docker pull nginx:stable-alpine
   ```
   <img width="1624" height="1056" alt="스크린샷 2025-09-24 오후 5 23 56" src="https://github.com/user-attachments/assets/f8c64e36-d6ef-4628-a448-07dd2603e879" />

   → Nginx 안정화 버전 이미지를 다운로드

2. **컨테이너 실행**
   ```bash
   docker run --name my-nginx -d -p 8080:80 nginx:stable-alpine
   ```
   <img width="1624" height="1056" alt="스크린샷 2025-09-24 오후 5 24 11" src="https://github.com/user-attachments/assets/13b82120-fc9b-4149-9f75-480ffb7f7698" />

   → my-nginx 이름의 컨테이너를 백그라운드 실행
   → 호스트 PC의 8080 포트를 컨테이너 80 포트와 매핑


3. **실행 상태 확인**
   ```bash
   docker ps
   ```
   <img width="1624" height="1056" alt="스크린샷 2025-09-24 오후 5 24 21" src="https://github.com/user-attachments/assets/8dff9834-64ff-4fb0-bd37-9d11338ab060" />

   → 컨테이너가 STATUS: Up 상태로 실행 중임을 확인

### 3.4 브라우저 접속 확인
	•	웹 브라우저에서 http://localhost:8080 접속
	•	“Welcome to nginx!” 페이지가 정상적으로 표시됨을 확인
  <img width="1624" height="1056" alt="스크린샷 2025-09-24 오후 5 24 40" src="https://github.com/user-attachments/assets/67411387-ca4f-4519-bc1f-9a3bbc78e275" />
<img width="1382" height="832" alt="스크린샷 2025-09-24 오후 5 25 04" src="https://github.com/user-attachments/assets/d9c854d6-008a-4939-a515-dbb4a7a5066c" />
