import json

from controller.user_route.commercial.commercial_menu_controller import commercial_menu_controller
from controller.user_route.gestion.gestion_menu_controller import gestion_menu_controller
from controller.user_route.support.support_menu_controller import support_menu_controller
from controller.user_route.logout import logout


def general_menu():
    """
    Menu principal qui dirige vers les sous-menus en fonction du rôle.
    """
    with open("session_token.json", "r") as file:
        user_data = json.load(file)

    if user_data["team_type"] == "gestion":
        gestion_menu_controller()
    elif user_data["team_type"] == "commercial":
        commercial_menu_controller()
    elif user_data["team_type"] == "support":
        support_menu_controller()
    else:
        print("Type d'équipe non reconnu. Déconnexion.")
        logout()
