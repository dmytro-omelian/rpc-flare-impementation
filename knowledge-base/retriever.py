from fastapi import APIRouter

router = APIRouter(prefix="/retriever")

@router.get("/")
async def root():
    return {"message": "Hello World"}