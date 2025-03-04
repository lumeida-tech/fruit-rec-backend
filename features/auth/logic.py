from fastapi import APIRouter

router = APIRouter(
    prefix="/api/auth",
    tags=["Auth"],
)

@router.get("/login")
async def login():
    return [{"username": "Rick"}, {"username": "Morty"}]



@router.get("/register")
async def register():
    return {"username": "Good"}