from typing import Any
from fastapi import FastAPI

PLUGIN_PORT = 8002
PLUGIN_ADDRESS = f"http://host.docker.internal:{PLUGIN_PORT}"

app = FastAPI(servers=[{"url":PLUGIN_ADDRESS}])


@app.get("/coin/flip")
async def coin_flip() -> Any:
    print("Heads")
    return {"Result": "Heads"}


@app.get("/die/6/roll")
async def d6_roll() -> Any:
    print(4)
    return {"res": 4}

