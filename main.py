from typing import Union
from fastapi import FastAPI, Response

app = FastAPI()


@app.get("/ping")
def ping():
    return Response(content="Pong", media_type="text/plain")
