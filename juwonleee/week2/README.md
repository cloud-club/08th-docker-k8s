

# 2주차 과제 : Dockerfile

## 1. 과제 목표
	•	개인 프로젝트 또는 예제 코드를 Dockerfile로 컨테이너화하고 실행해보기
	•	Dockerfile 작성 → 이미지 빌드 → 컨테이너 실행 → 결과 확인 과정을 실습

이번 과제에서는 FastAPI “Hello World” 예제를 사용하여 Dockerfile을 작성하고 컨테이너를 실행하였다.


## 2. 프로젝트 구조

fastapi-hello/
├── app.py
├── requirements.txt
├── .dockerfile
├── .dockerignore


## 3. 코드

**app.py**
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, Docker + FastAPI!"}
```
**requirements.txt**
```python
fastapi
uvicorn[standard]
```
.dockerignore
```python
__pycache__/
*.pyc
.venv/
.env
```
.dockerfile
```python
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```


## 4. 실행 과정

**1) 이미지 빌드**
```
docker build -t fastapi-hello:0.1 -f .dockerfile .
```
**2) 컨테이너 실행**
```
docker run -d --rm -p 8000:8000 --name fastapi-hello fastapi-hello:0.1
```
**3) 컨테이너 확인**
```
docker ps
docker logs -n 20 fastapi-hello
```

## 5. 실행 결과
<img width="974" height="441" alt="스크린샷 2025-10-01 오후 8 21 13" src="https://github.com/user-attachments/assets/0122d7eb-acd6-41f1-a757-0716e239bfb9" />
<img width="975" height="535" alt="스크린샷 2025-10-01 오후 8 21 29" src="https://github.com/user-attachments/assets/f6e934c0-e798-454b-9f8a-10f0b3159f0a" />
<img width="972" height="117" alt="스크린샷 2025-10-01 오후 8 22 09" src="https://github.com/user-attachments/assets/1fc9346e-9f5e-4532-a325-1c9a3d52ac95" />
<img width="946" height="33" alt="스크린샷 2025-10-01 오후 8 22 22" src="https://github.com/user-attachments/assets/0d505e48-8ef6-4271-b6c4-5b86eb280e99" />
<img width="514" height="225" alt="스크린샷 2025-10-01 오후 8 22 33" src="https://github.com/user-attachments/assets/2a391770-60be-4738-817a-6cc598632fd2" />
<img width="1268" height="722" alt="스크린샷 2025-10-01 오후 8 22 57" src="https://github.com/user-attachments/assets/4f915abc-630b-4e7a-b968-1874e02114ed" />

✅ Docker Desktop에서 컨테이너 실행 확인

✅ 브라우저에서 응답 확인
```
http://localhost:8000
{"message":"Hello, Docker + FastAPI!"}
```
✅ curl 명령어로 응답 확인
```
curl http://localhost:8000
{"message":"Hello, Docker + FastAPI!"}
```
✅ docker ps 결과

✅ docker build 성공 로그


## 6. 느낀 점
	•	처음에는 Dockerfile 위치와 파일명이 헷갈려서 빌드 에러가 났지만, 올바른 위치와 옵션(-f .dockerfile)을 지정하니 해결되었다.
	•	컨테이너로 실행한 FastAPI가 브라우저에서 정상적으로 응답하는 것을 보고, 내 코드가 환경에 독립적으로 실행된다는 점을 체감할 수 있었다.
	•	다음에는 Docker Hub에 이미지를 올려보고, 쿠버네티스 환경에서도 이 이미지를 배포해보고 싶다.
