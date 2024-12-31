from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from router import test, api, front_preferences

app = FastAPI()
#라우터 등록
app.include_router(test.router)
app.include_router(api.router)
app.include_router(front_preferences.router)

# StaticFiles는 최하위 경로로 처리
app.mount("/", StaticFiles(directory="public", html=True), name="static")
