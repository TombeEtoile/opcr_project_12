from config.database import Session
from models.models import Collaborator
import bcrypt
import json
import tempfile
import os
from view.registration_view import registration


def login_user():
    session = Session()

    user_answer = registration()

    # Recherche l'utilisateur dans la base de données
    user = session.query(Collaborator).filter_by(email=user_answer[0]).first()

    if user and bcrypt.checkpw(user_answer[1].encode('utf-8'), user.password.encode('utf-8')):
        print("Connexion réussie.")

        # Créer un fichier temporaire pour stocker les informations utilisateur
        # create_user_token(user)

        session.close()
        return user  # Peut être utilisé pour d'autres opérations si nécessaire
    else:
        print("Email ou mot de passe incorrect.")
        session.close()
        return None


login_user()
