from fastapi import FastAPI
from api.v1.feedback.router import router as router_feedback


app = FastAPI()

app.include_router(
    router_feedback
)