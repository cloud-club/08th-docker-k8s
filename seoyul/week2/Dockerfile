# Python 3.11 slim 이미지를 베이스로 사용
FROM python:3.11-slim

# 작업 디렉토리 설정
WORKDIR /app

# requirements.txt를 복사하고 의존성 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 애플리케이션 코드 복사
COPY app.py .

# 포트 8000 노출
EXPOSE 8000

# 애플리케이션 실행
CMD ["python", "app.py"]
