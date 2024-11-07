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
    "management": {
        "create_collaborator",
        "update_collaborator",
        "delete_collaborator",
        "create_contract",
        "update_contract",
        "list_events",
        "filter_events_no_support",
        "update_event",
        "assign_support_to_event"
    },
    "sales": {
        "create_client",
        "update_client",
        "update_contract",
        "filter_contracts_unsigned_unpaid",
        "create_event_for_signed_client"
    },
    "support": {
        "list_events_assigned",
        "update_event_assigned"
    }
}


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
