# Fichier de configuration de la BDD
'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'sqlite:///database/epic_events_bdd.db'

engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(bind=engine)
'''

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

# Définition du chemin de la base de données
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Dossier actuel de `config/database.py`
DATABASE_PATH = os.path.join(BASE_DIR, '../database/epic_events_bdd.db')

# Création de l'engine avec un chemin absolu
engine = create_engine(f'sqlite:///{DATABASE_PATH}', echo=True)

# Configuration de la session pour interagir avec la BDD
Session = sessionmaker(bind=engine)
