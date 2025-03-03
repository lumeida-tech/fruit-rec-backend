
from sqlalchemy.orm import Session

from db.config import engine

session = Session(engine)
