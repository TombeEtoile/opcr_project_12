# Fichier de configuration de la BDD
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# import os
# base_dir = os.path.abspath(os.path.dirname(__file__))
# DATABASE_URL = f"sqlite:///{os.path.join(base_dir, '../database/epic_events_bdd.db')}"

DATABASE_URL = 'sqlite:///database/epic_events_bdd.db'

engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine)
