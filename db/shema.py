# Les shemas de validations (pour la serialization io)

from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import List, Optional

class UtilisateurBase(BaseModel):
    nom_famille: str
    prenom: str
    email: EmailStr
    numero_telephone: str

class UtilisateurCreate(UtilisateurBase):
    mot_de_passe: str

class UtilisateurResponse(UtilisateurBase):
    id_utilisateur: int
    date_creation_compte: datetime

    class Config:
        orm_mode = True

class ActiviteBase(BaseModel):
    nbre_total_img: int

class ActiviteCreate(ActiviteBase):
    pass

class ActiviteResponse(ActiviteBase):
    id_activite: int
    date_activite: datetime

    class Config:
        orm_mode = True

class ImageBase(BaseModel):
    image_path: str
    nbre_total_fruit: int

class ImageCreate(ImageBase):
    pass

class ImageResponse(ImageBase):
    id_image: int
    date_televersement: datetime

    class Config:
        orm_mode = True

class ResultatsAnalyseBase(BaseModel):
    nom_fruit: str
    nbre_fruit: int

class ResultatsAnalyseCreate(ResultatsAnalyseBase):
    pass

class ResultatsAnalyseResponse(ResultatsAnalyseBase):
    id_resultat: int

    class Config:
        orm_mode = True


