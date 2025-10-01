from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
	return {"message": "안녕하세요 안녕히가세요"}