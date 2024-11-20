from fastapi import FastAPI


app = FastAPI()


@app.get("/coin/flip")
async def coin_flip() -> str:
    print("Heads")
    return "Heads"


@app.get("/die/6/roll")
async def d6_roll() -> int:
    print(4)
    return 4

