from fastapi import FastAPI

from src import retriever

app = FastAPI()

app.include_router(retriever.router)

