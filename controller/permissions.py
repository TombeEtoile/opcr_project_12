import os
import json
"""
PERMISSIONS = {
    "sale": ["list_clients", "list_events", "list_contracts", "list_collaborators",  # list
             "add_client", "add_contract",  # add
             "update_client", "update_contract",  # update
             ],

    "support": ["list_clients", "list_events", "list_contracts", "list_collaborators",  # list
                "update_event",  # update
                ],

    "gestion": ["list_clients", "list_events", "list_contracts", "list_collaborators",  # list
                "add_collaborator", "add_contract",  # add
                "update_collaborator", "update_contract", "update_event",  # update
                ],
}
"""
PERMISSIONS = {
    "gestion": {
        "view_all_clients", "view_all_contracts", "view_all_events", "view_all_collaborators",  # all view accorded
        "filter_events_no_support",  # filtered view
        "create_collaborator", "create_contract",  # add
        "update_collaborator", "update_event", "assign_support_to_event",  # update
        "delete_collaborator", "update_contract"  # delete
    },
    "commercial": {
        "view_all_clients", "view_all_contracts", "view_all_events", "view_all_collaborators",  # all view accorded
        "filter_contracts_unsigned_unpaid",  # filtered view
        "create_client", "create_event_for_signed_client",  # add
        "update_client", "update_contract"  # update
    },
    "support": {
        "view_all_clients", "view_all_contracts", "view_all_events", "view_all_collaborators",  # all view accorded
        "list_events_assigned",  # filtered view
        "update_event_assigned"  # update
    }
}

"""
Gestion --> Filtrer affichage événements --> afficher tous les événements qui n’ont pas de « support » associé.
Commercial --> Filtrer affichage des contrats --> afficher tous les contrats qui ne sont pas encore signés, ou qui ne sont pas encore
entièrement payés.
"""


def has_permission(action):
    # Vérifie si un utilisateur est connecté
    if not os.path.exists("session_token.json"):
        print("Aucun utilisateur connecté.")
        return False

    # Charge les informations de session
    with open("session_token.json", "r") as file:
        session_data = json.load(file)

    user_team_type = session_data.get("team_type")
    return action in PERMISSIONS.get(user_team_type, set())
