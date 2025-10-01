from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="FastAPI Docker Demo", description="Simple FastAPI Hello World application")

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>FastAPI Docker Demo</title>
        <style>
            body {
                font-family: 'Arial', sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
            }
            .container {
                background: white;
                padding: 40px;
                border-radius: 15px;
                box-shadow: 0 20px 40px rgba(0,0,0,0.1);
                text-align: center;
                max-width: 600px;
            }
            h1 {
                color: #333;
                margin-bottom: 20px;
                font-size: 2.5em;
            }
            .emoji {
                font-size: 4em;
                margin: 20px 0;
            }
            .info {
                background: #f8f9fa;
                padding: 20px;
                border-radius: 10px;
                margin: 20px 0;
                border-left: 4px solid #667eea;
            }
            .badge {
                display: inline-block;
                background: #667eea;
                color: white;
                padding: 5px 15px;
                border-radius: 20px;
                margin: 5px;
                font-size: 0.9em;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="emoji">🐳</div>
            <h1>Hello Docker + FastAPI!</h1>
            <div class="info">
                <h3>🚀 FastAPI Docker 과제 완료!</h3>
                <p>이 페이지는 Docker 컨테이너에서 실행되는 FastAPI 애플리케이션입니다.</p>
                <div>
                    <span class="badge">FastAPI</span>
                    <span class="badge">Docker</span>
                    <span class="badge">Python</span>
                </div>
            </div>
            <p><strong>API 문서:</strong> <a href="/docs" target="_blank">/docs</a></p>
            <p><strong>ReDoc:</strong> <a href="/redoc" target="_blank">/redoc</a></p>
        </div>
    </body>
    </html>
    """

@app.get("/api/hello")
async def hello_api():
    return {"message": "Hello World from FastAPI!", "status": "success", "docker": True}

@app.get("/api/info")
async def get_info():
    return {
        "application": "FastAPI Docker Demo",
        "version": "1.0.0",
        "description": "Docker 과제용 FastAPI 애플리케이션",
        "endpoints": ["/", "/api/hello", "/api/info", "/docs", "/redoc"]
    }