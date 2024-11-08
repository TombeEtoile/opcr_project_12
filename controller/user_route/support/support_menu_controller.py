from view.support.support_menu_view import support_menu_view
from controller.user_route.logout import logout
from controller.permissions import has_permission

from controller.cli.cli_client import ListClient
from controller.cli.cli_contract import ListContract
from controller.cli.cli_event import ListEvent


def support_menu_controller():
    while True:
        user_answer = support_menu_view()
        if user_answer == '1':  # Lister les clients
            ListClient.list_client()
        if user_answer == '2':  # Lister les contrats
            ListContract.list_contract()
        if user_answer == '3':  # Lister les événements
            ListEvent.list_event()
        if user_answer == '4':  # Lister les événements dont vous êtes responsable
            ListEvent.list_event_dedicated_to_a_support()
        if user_answer == '5':  # Modifier un événement dont vous êtes responsable
            ListEvent.list_event_dedicated_to_a_support()
        if user_answer == '6':  # Déconnexion
            print('-------------------- Déconnexion réussie --------------------')
            logout()


def update_event_prompt():
    event_id = int(input("ID de l'événement à modifier : "))

    event_date_start = input('Date de commencent : ')
    event_date_end = input('Date de fin : ')
    location = input('Localisation : ')
    attendees = input('Nombre de participants : ')
    note = input('Note : ')
    id_contract = input('ID du contrat lié : ')
    id_client = input('ID du client lié : ')
    id_support_team = input('ID du support lié : ')

    update_event(
        event_id=event_id,
        event_date_start=event_date_start if event_date_start else None,
        event_date_end=event_date_end if event_date_end else None,
        location=location if location else None,
        attendees=int(attendees) if attendees else None,
        note=note if note else None,
        id_contract=int(id_contract) if id_contract else None,
        id_client=int(id_client) if id_client else None,
        id_support_team=int(id_support_team) if id_support_team else None
    )
