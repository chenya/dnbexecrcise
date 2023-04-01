import uvicorn
from fastapi import FastAPI
from stocks.router import stocks_router

app: FastAPI = FastAPI()


app.include_router(stocks_router, prefix="/stock")


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
