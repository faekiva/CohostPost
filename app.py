from fastapi import FastAPI, Request
from cohost.models.user import User
from cohost.models.block import MarkdownBlock
from fastapi.responses import JSONResponse
import os


app = FastAPI()

@app.middleware("http")
async def authenticate(request: Request, call_next):
    if request.headers.get("Authorization") != os.getenv("AUTH_TOKEN"):
        return JSONResponse({"status": "unauthorized"}, status_code=401)
    return await call_next(request)

@app.post("/")
async def main(request: Request):
    user = User.login(os.getenv("COHOST_USER"), os.getenv("COHOST_PASS"))
    message = await request.body()
    user.defaultProject.post("",blocks=[MarkdownBlock(message.decode("utf-8"))])
    return {"status": "ok"}
