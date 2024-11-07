import os


def logout():
    """Déconnecte l'utilisateur en supprimant le fichier de session."""
    if os.path.exists("session_token.json"):
        os.remove("session_token.json")
        print("Déconnexion réussie.")
    else:
        print("Aucun utilisateur connecté.")
