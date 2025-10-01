# 1. 빌드 스테이지 (Builder Stage)
# JDK 환경에서 프로젝트를 빌드하여 실행 가능한 JAR 파일을 생성

FROM gradle:jdk22 AS builder
WORKDIR /app

# Gradle 관련 파일만 먼저 복사 -> 의존성 레이어를 캐싱
COPY gradlew .
COPY gradle gradle
COPY build.gradle .
COPY settings.gradle .
# 의존성 먼저 다운로드 - build.gradle이 바뀌지 않으면 캐시 사용하도록
RUN gradle dependencies --no-daemon

# 소스 코드를 복사하고 애플리케이션을 빌드
COPY src src
RUN gradle bootJar --no-daemon -x test


# 2. JAR 분해 스테이지 (Extractor Stage)
# 빌드된 JAR 파일을 layertools를 이용해 여러 레이어로 분해
FROM eclipse-temurin:22-jre-alpine AS extractor
WORKDIR /app

# 빌더 스테이지에서 생성된 JAR 파일을 복사
COPY --from=builder /app/build/libs/*.jar /app/app.jar
# layertools를 사용해 JAR 파일의 압축을 풀어 레이어별로 디렉토리를 생성
RUN java -Djarmode=layertools -jar app.jar extract


# 3. 최종 실행 스테이지 (Final Runner Stage)
# 분해된 레이어들을 JRE만 있는 가벼운 이미지에 복사하여 최종 이미지 생성
FROM eclipse-temurin:22-jre-alpine AS runner
WORKDIR /app

EXPOSE 8080

# Extractor 스테이지에서 분해된 레이어들을 순서대로 복사
# 의존성 -> 스프링 부트 로더 -> 애플리케이션 순으로 복사하여 캐시 효율 높이기
COPY --from=extractor /app/dependencies/ ./
COPY --from=extractor /app/spring-boot-loader/ ./
COPY --from=extractor /app/snapshot-dependencies/ ./
COPY --from=extractor /app/application/ ./

# Spring Boot Loader를 통해 애플리케이션을 실행
ENTRYPOINT ["java", "org.springframework.boot.loader.launch.JarLauncher"]