# main.py

# 실행 명령어 uvicorn main:app --reload
# 포트번호 : 8000번
# api list : localhost:8000/docs

from fastapi import FastAPI
from app.router.algRouter import algRouter

app = FastAPI()

app.include_router(algRouter, prefix="/api/alg")
