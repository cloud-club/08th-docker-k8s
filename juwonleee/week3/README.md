# 3주차 과제 : Docker DIY ① – nginx 컨테이너 실행 및 수정

## 1. 과제 목표
- 로컬 환경에서 nginx 이미지를 실행하고 외부 포트로 접근 가능하도록 설정한다.
- 컨테이너 내부에서 index.html 파일을 수정하여 나만의 문구를 출력해본다.

이번 실습에서는 ‘nhnedu’라는 이름의 컨테이너를 실행하고,  
기본 페이지의 문구를 “Welcome to Juwon”으로 변경하였다.



## 2. 환경 정보

| 항목 | 내용 |
|------|------|
| OS | macOS |
| 도구 | Docker Desktop |
| 이미지 | nginx:latest |
| 컨테이너 이름 | nhnedu |
| 포트 매핑 | 8000 → 80 |



## 3. 실행 과정

**1) nginx 컨테이너 실행**
```
docker run -d --name nhnedu -p 8000:80 nginx
```

**2) 컨테이너 내부 접근 및 vim 설치**
```
docker exec nhnedu apt-get update
docker exec nhnedu apt-get install -y vim
```

**3) index.html 수정**
```
docker exec nhnedu sed -i 's/Welcome to nginx!/Welcome to Juwon/g' /usr/share/nginx/html/index.html
```

**4) 브라우저에서 결과 확인**
- 주소창에 `http://localhost:8000` 입력  
- “Welcome to Juwon” 문구가 출력되면 성공

## 4. 실행 결과
- nhnedu 컨테이너가 8000포트에서 정상 실행됨
- index.html 수정 후 브라우저에서 “Welcome to Juwon” 출력 확인
- Docker 컨테이너 내부 파일 수정 결과가 즉시 반영됨
<img width="801" height="48" alt="스크린샷 2025-10-15 오후 7 34 04" src="https://github.com/user-attachments/assets/d2528a99-20e8-47d0-8b8d-674eeb11ce3e" />
<img width="1624" height="1056" alt="스크린샷 2025-10-15 오후 7 33 18" src="https://github.com/user-attachments/assets/4595eae7-076e-4499-9472-f89fb00873a4" />

## 5. 느낀 점
Docker 컨테이너 내부에서 직접 파일을 수정해보며 컨테이너의 독립성과 실시간 반영 구조를 이해할 수 있었다.  
명령어 실행만으로 웹 서버를 띄우고 수정할 수 있다는 점이 매우 직관적이었다.

# 3주차 과제 : Docker DIY ② – Dockerfile로 커스텀 이미지 빌드

## 1. 과제 목표
- nginx 최신 버전 이미지를 기반으로 커스텀 Dockerfile을 작성한다.
- 직접 작성한 index.html 파일을 컨테이너에 복사하고, 빌드 후 실행해본다.
이번 실습에서는 “welcome to my page” 문구를 출력하는 커스텀 이미지를 빌드하였다.


## 2. 환경 정보

| 항목 | 내용 |
|------|------|
| OS | macOS |
| 도구 | Docker Desktop |
| 베이스 이미지 | nginx:latest |
| 새 이미지 이름 | mynginx |
| 컨테이너 이름 | mynginx-container |
| 포트 매핑 | 8002 → 80 |


## 3. 실행 과정

**1) index.html 작성**
```
echo "welcome to my page" > index.html
```

**2) Dockerfile 작성**
```
FROM nginx:latest
WORKDIR /app
COPY . /usr/share/nginx/html
RUN apt-get update && apt-get install -y vim
EXPOSE 80
```

**3) 이미지 빌드**
```
docker build -t mynginx .
```

**4) 컨테이너 실행**
```
docker run -d --name mynginx-container -p 8002:80 mynginx
```

**5) 브라우저에서 결과 확인**
- 주소창에 `http://localhost:8002` 입력  
- “welcome to my page” 문구가 출력되면 성공


## 4. 실행 결과
- mynginx 이미지가 성공적으로 빌드됨
- mynginx-container가 8002포트에서 정상 실행됨
- 브라우저에서 “welcome to my page” 문구 출력 확인
<img width="872" height="57" alt="스크린샷 2025-10-15 오후 7 42 04" src="https://github.com/user-attachments/assets/6d5d71b1-4178-4f57-80f2-1f7cb96f83bf" />
<img width="947" height="562" alt="스크린샷 2025-10-15 오후 7 41 06" src="https://github.com/user-attachments/assets/eec3c26e-d065-4908-a2d0-f04a32091862" />
<img width="944" height="743" alt="스크린샷 2025-10-15 오후 7 40 56" src="https://github.com/user-attachments/assets/9bfce2a3-1a2d-492e-874e-18b2830b14d8" />
<img width="944" height="757" alt="스크린샷 2025-10-15 오후 7 40 44" src="https://github.com/user-attachments/assets/62fe48d0-c92b-40ba-b655-459835ed5f37" />
<img width="809" height="743" alt="스크린샷 2025-10-15 오후 7 40 30" src="https://github.com/user-attachments/assets/ca5e1aeb-59c7-410c-a534-e653f321b0c2" />
<img width="1624" height="1056" alt="스크린샷 2025-10-15 오후 7 38 58" src="https://github.com/user-attachments/assets/bc223a70-14e2-4355-96d0-9b65d8b85c47" />


## 5. 느낀 점
직접 Dockerfile을 작성하며 이미지 빌드의 구조를 이해할 수 있었다.  
RUN, COPY, EXPOSE 등 각 명령어의 의미와 실행 순서를 익히며,  
Docker가 코드 실행 환경을 자동화하는 방식에 대해 감을 잡을 수 있었다.


# 3주차 과제 : Kubernetes 활성화 확인

## 1. 과제 목표
- Docker Desktop 환경에서 Kubernetes를 활성화한다.
- kubectl 명령어를 이용해 클러스터 네임스페이스를 확인한다.


## 2. 환경 정보

| 항목 | 내용 |
|------|------|
| OS | macOS |
| 도구 | Docker Desktop |
| Kubernetes 버전 | v1.32.2 |
| 프로비저닝 방식 | kubeadm |


## 3. 실행 과정

**1) Docker Desktop 설정**
- Settings → Kubernetes → Enable Kubernetes 체크  
- Show system containers 옵션은 미체크  
- Apply & Restart 클릭 후 클러스터 시작 대기

**2) kubectl 명령어 실행**
```
kubectl version --client
kubectl config get-contexts
kubectl config use-context docker-desktop
kubectl get namespaces
```

**3) 네임스페이스 확인 결과**
```
NAME              STATUS   AGE
default           Active   22s
kube-node-lease   Active   22s
kube-public       Active   22s
kube-system       Active   22s
```

## 4. 실행 결과
- Docker Desktop에서 Kubernetes is running 상태 확인
- kubectl get namespaces 명령 결과, 기본 네임스페이스 4개 Active 상태 확인
<img width="273" height="87" alt="스크린샷 2025-10-15 오후 7 48 24" src="https://github.com/user-attachments/assets/9e99ca46-eb43-45a5-8fcb-03ae65140b54" />
<img width="1382" height="832" alt="스크린샷 2025-10-15 오후 7 46 31" src="https://github.com/user-attachments/assets/a8796f0e-a14e-465b-bdf9-82fe2ff8ce32" />


## 5. 느낀 점
Docker Desktop에서 Kubernetes를 직접 활성화하며 컨테이너 오케스트레이션 환경을 체험할 수 있었다.  
kubectl을 이용해 클러스터 내부 구성요소를 조회하면서, 컨테이너가 단일 단위가 아닌 시스템 단위로 관리된다는 개념을 이해할 수 있었다.

