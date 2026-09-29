import os

from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI(title="Docker GitHub Actions Demo")


@app.get("/hello", response_class=PlainTextResponse)
def hello() -> str:
    return os.getenv("APP_MESSAGE", "Hello World 3")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
