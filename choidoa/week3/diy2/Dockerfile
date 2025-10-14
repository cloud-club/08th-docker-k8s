# Use latest Nginx base image
FROM nginx:latest

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install vim, replace default page, and clean apt cache
RUN apt-get update \
    && apt-get install -y vim \
    && echo "<h1>Choi Doa</h1>" > /usr/share/nginx/html/index.html \
    && rm -rf /var/lib/apt/lists/*

# Expose port 80
EXPOSE 80