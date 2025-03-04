
from fastapi import APIRouter, Response

from db.shema import UtilisateurBase, UtilisateurCreate
from lib.session import session
from db.models import Utilisateur
from sqlalchemy.exc import IntegrityError


router = APIRouter(
    prefix="/api/auth",
    tags=["Auth"],
)


@router.get("/users")
def get_all_users() -> list[UtilisateurBase]:
    return session.query(Utilisateur).all()


@router.post("/login")
async def login(response: Response, data: UtilisateurBase):
    # response.set_cookie()
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.post("/register")
def register(user: UtilisateurCreate) -> UtilisateurBase:

    try:
        user_mapped = Utilisateur(**user.dict())
        session.add(user_mapped)
        session.commit()
        session.refresh(Utilisateur)
        return user
    except:
        session.rollback()
        return {"error": "Erreur d'insertion, veuillez réessayer."}
