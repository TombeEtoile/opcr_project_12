import bcrypt
from models.models import Collaborator
from config.database import Session
from view.registration_view import registration
import json
# import os

from controller.user_route.menu import menu_answer
# from controller.permissions import PERMISSIONS


def login():
    mail, password = registration()
    session = Session()

    # Recherche le collaborateur avec l'adresse e-mail fournie
    user = session.query(Collaborator).filter_by(email=mail).first()

    if user and bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
        print("Connexion réussie")

        # Crée un fichier temporaire pour stocker les informations de session
        session_data = {"email": user.email, "team_type": user.team_type}
        with open("session_token.json", "w") as file:
            json.dump(session_data, file)

        print(f"Utilisateur connecté avec le rôle : {user.team_type}")
        menu_answer()

    else:
        print("Erreur : e-mail ou mot de passe incorrect")

    session.close()


"""
def logout():
    # Déconnecte l'utilisateur en supprimant le fichier de session.
    if os.path.exists("session_token.json"):
        os.remove("session_token.json")
        print("Déconnexion réussie.")
    else:
        print("Aucun utilisateur connecté.")
"""
