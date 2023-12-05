from fastapi import FastAPI, Request
from cohost.models.user import User
from cohost.models.block import MarkdownBlock
import os


app = FastAPI()

@app.post("/")
async def main(request: Request):
    user = User.login(os.getenv("COHOST_USER"), os.getenv("COHOST_PASS"))
    message = await request.body()
    user.defaultProject.post("",blocks=[MarkdownBlock(message.decode("utf-8"))])
    return {"status": "ok"}