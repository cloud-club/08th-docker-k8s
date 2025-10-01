# Todo API - Docker 실습 프로젝트

간단한 할일 관리 웹 애플리케이션을 통해 Docker와 docker-compose를 학습하는 프로젝트입니다.

![Image](https://github.com/user-attachments/assets/ca788a69-79d6-4b67-92b1-3cd7032a50ca)

## 🏗️ 아키텍처

- **프론트엔드**: HTML + CSS + JavaScript (바닐라)
- **API 서버**: Node.js + Express
- **데이터베이스**: MongoDB
- **캐시**: Redis
- **컨테이너화**: Docker + docker-compose

## 🚀 실행 방법

### 1. 프로젝트 실행
```bash
# 모든 서비스 시작
docker-compose up -d

# 로그 확인
docker-compose logs -f

# 서비스 상태 확인
docker-compose ps
```

### 2. 웹 애플리케이션 접속

브라우저에서 다음 URL로 접속:
```
http://localhost:3000
```

웹 인터페이스를 통해 할일을 추가, 완료, 삭제할 수 있습니다.

### 3. API 직접 테스트 (선택사항)

#### 헬스체크
```bash
curl http://localhost:3000/health
```

#### 할일 생성
```bash
curl -X POST http://localhost:3000/todos \
  -H "Content-Type: application/json" \
  -d '{"title": "Docker 공부하기"}'
```

#### 할일 목록 조회
```bash
curl http://localhost:3000/todos
```

#### 할일 완료 토글
```bash
curl -X PATCH http://localhost:3000/todos/{todo_id}
```

#### 할일 삭제
```bash
curl -X DELETE http://localhost:3000/todos/{todo_id}
```

## 🐳 Docker 학습 포인트

### 1. 멀티 컨테이너 구성
- 애플리케이션, 데이터베이스, 캐시를 각각 분리된 컨테이너로 실행
- 서비스 간 네트워크 통신

### 2. 볼륨 관리
- MongoDB와 Redis 데이터 영속성 보장
- 컨테이너 재시작 시에도 데이터 유지

### 3. Docker 네트워크 격리
- **컨테이너 격리 및 그룹화**: 같은 네트워크 내 컨테이너만 서로 통신 가능
- **서비스 이름 기반 통신**: `mongodb://mongo:27017` 형태로 서비스 이름 사용
- **포트 매핑 vs 컨테이너 간 통신**: 외부 접근용 포트 매핑과 내부 통신 분리
- **Linux 커널 기술 활용**:
  - **Network Namespaces**: 각 컨테이너마다 독립적인 네트워크 스택
  - **Virtual Ethernet (veth)**: 컨테이너와 호스트 연결하는 가상 케이블
  - **Linux Bridge**: 가상 스위치 역할로 같은 네트워크 컨테이너 연결
  - **iptables**: 네트워크 트래픽 필터링 및 라우팅


## 🛠️ 유용한 Docker 명령어

```bash
# 서비스 중지
docker-compose down

# 볼륨까지 삭제 (데이터 초기화)
docker-compose down -v

# 특정 서비스만 재시작
docker-compose restart app

# 프론트엔드 수정 후 반영 (재빌드)
docker-compose up -d --build app

# 컨테이너 내부 접속
docker-compose exec app sh
docker-compose exec mongo mongosh

# 이미지 재빌드
docker-compose build --no-cache
```

## 📊 모니터링

```bash
# 실시간 로그 확인
docker-compose logs -f app

# 리소스 사용량 확인
docker stats

# 네트워크 확인
docker network ls
docker network inspect todo-api_todo-network
```
## 📁 프로젝
트 구조

```
todo-api/
├── app/
│   ├── public/           # 프론트엔드 파일
│   │   ├── index.html    # 메인 웹 페이지
│   │   └── script.js     # JavaScript 로직
│   ├── server.js         # Express 서버
│   ├── package.json      # Node.js 의존성
│   ├── Dockerfile        # 앱 컨테이너 설정
│   └── .env             # 환경변수 (선택사항)
├── docker-compose.yml    # 멀티 컨테이너 설정
└── README.md
```

## 🚀 다음 단계

1. **개발 환경 최적화**: 볼륨 마운트로 실시간 파일 반영
2. **Nginx 추가**: 리버스 프록시 및 로드 밸런싱
3. **Docker Swarm**: 컨테이너 오케스트레이션
4. **CI/CD 파이프라인**: GitHub Actions와 Docker 통합