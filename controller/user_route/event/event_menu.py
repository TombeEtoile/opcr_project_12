from view.menu_view import menu
from view.event.event_menu_view import event_menu
from controller.cli.cli_event import list_event, add_event, update_event, delete_event


def event_menu_answer():
    user_answer = event_menu()
    if user_answer == '1':  # list
        list_event()
        menu()
    elif user_answer == '2':  # add
        add_event_prompt()
        menu()
    elif user_answer == '3':  # update
        update_event_prompt()
        menu()
    elif user_answer == '4':  # delete
        delete_event_prompt()
        menu()
    elif user_answer == '5':  # menu
        menu()
    return print(f'Erreur : valeur non acceptée ({user_answer})')


def add_event_prompt():
    event_date_start = input('Date de commencent : ')
    event_date_end = input('Date de fin : ')
    location = input('Localisation : ')
    attendees = int(input('Nombre de participants : '))
    note = input('Note : ')
    id_contract = int(input('ID du contrat lié : '))
    id_client = int(input('ID du client lié : '))
    id_support_team = int(input('ID du support lié : '))

    add_event(event_date_start, event_date_end, location, attendees, note, id_contract, id_client, id_support_team)


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


def delete_event_prompt():
    event_id = int(input("ID de l'événement à modifier : "))
    delete_event(event_id)
