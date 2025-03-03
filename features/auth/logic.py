
from fastapi import APIRouter

from db.shema import UtilisateurBase
from lib.session import session
from db.models import Utilisateur


router = APIRouter(
    prefix="/api/auth",
    tags=["Auth"],
)


@router.get("/login")
async def login():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.post("/register")
def register(user: UtilisateurBase) -> UtilisateurBase:
    # session.add(user)
    return user
