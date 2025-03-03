from sqlalchemy import create_engine

sqlite_file_name = "db.db"
chaine_de_connexion = f"sqlite:///{sqlite_file_name}"

engine = create_engine(chaine_de_connexion, echo=True)
