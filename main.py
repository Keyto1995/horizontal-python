from typing import Union
from fastapi import FastAPI, Request, Response

app = FastAPI()


@app.get("/ping")
def ping():
    return Response(content="Pong", media_type="text/plain")


@app.get("/clientIP")
def clientIP(request: Request):
    client_host = request.client.host
    return {"data": client_host}
