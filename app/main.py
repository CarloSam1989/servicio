from fastapi import FastAPI
from config import engine
import router

app = FastAPI()

@app.get('/')
async def home():
    return 'hola'

app.include_router(router.router,prefix="/libro",tags=["libro"])