import uuid

from pydantic.v1 import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from .config import Base
from datetime import datetime


class Utilisateur(Base):
    __tablename__ = "utilisateur"

    id_utilisateur = Column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    photo_profile = Column(String, nullable=True)
    nom_famille = Column(String, nullable=False)
    prenom = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    numero_telephone = Column(String, unique=True, nullable=False)
    mot_de_passe = Column(String, nullable=False)
    code_otp = Column(String, nullable=True)
    code_otp_expiration = Column(DateTime, nullable=True)
    date_creation_compte = Column(DateTime, default=datetime.utcnow)
    date_mise_a_jour = Column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    activites = relationship("Activite", back_populates="utilisateur")


class Activite(Base):
    __tablename__ = "activite"

    id_activite = Column(UUID(as_uuid=True),
                         primary_key=True, default=uuid.uuid4)
    nbre_total_img = Column(Integer, nullable=False)
    date_activite = Column(DateTime, default=datetime.utcnow)

    id_utilisateur = Column(
        UUID(as_uuid=True), ForeignKey("utilisateur.id_utilisateur"))
    utilisateur = relationship("Utilisateur", back_populates="activites")

    images = relationship("Image", back_populates="activite")


class Image(Base):
    __tablename__ = "image"

    id_image = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    image_path = Column(String, nullable=False)
    nbre_total_fruit = Column(Integer, nullable=False)
    date_televersement = Column(DateTime, default=datetime.utcnow)

    id_activite = Column(UUID(as_uuid=True),
                         ForeignKey("activite.id_activite"))
    activite = relationship("Activite", back_populates="images")

    resultats = relationship("ResultatsAnalyse", back_populates="image")


class ResultatsAnalyse(Base):
    __tablename__ = "resultats_analyse"

    id_resultat = Column(UUID(as_uuid=True),
                         primary_key=True, default=uuid.uuid4)
    nom_fruit = Column(String, nullable=False)
    nbre_fruit = Column(Integer, nullable=False)

    id_image = Column(UUID(as_uuid=True), ForeignKey("image.id_image"))
    image = relationship("Image", back_populates="resultats")
