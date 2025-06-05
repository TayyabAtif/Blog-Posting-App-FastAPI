from fastapi import FastAPI
from users.routes import router as user_router
from posts.routes import router as post_router
from infrastructure.websocket import router as websocket_router
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

app.include_router(user_router)
app.include_router(post_router)
app.include_router(websocket_router)

@app.get("/")
def root():
    return {"message": "Blog is running!"}