# Use Python 3.13 slime base image
FROM python:3.13-slim

# Add image metadata 
LABEL maintainer="Doa Choi <doa.choi@gmail.com>"

# Set working directory
WORKDIR /app

# Copy and install dependencies
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Copy application source
COPY ./app /app

# Expose port 80 to allow external access
EXPOSE 80

# Run the FastAPI application using uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
