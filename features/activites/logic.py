from fastapi import APIRouter
from db.shema import UtilisateurBase
from lib.session import session

router = APIRouter(
    prefix="/api/activities",
    tags=["Activities"],
)


@router.post("/create")
def create(user: UtilisateurBase) -> UtilisateurBase:
    return user
