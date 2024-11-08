from view.commercial.commercial_menu_view import commercial_menu_view

from controller.user_route.logout import logout
from controller.permissions import has_permission

from controller.cli.cli_client import ListClient, add_event_to_sale_client, update_client
from controller.cli.cli_contract import ListContract
from controller.cli.cli_event import ListEvent


def commercial_menu_controller():
    while True:
        user_answer = commercial_menu_view()
        if user_answer == '1':  # Lister les clients
            ListClient.list_client()
        elif user_answer == '2':  # Lister les contrats
            ListContract.list_contract()
        elif user_answer == '3':  # Lister les contrats non signés
            ListContract.list_unsigned_contract()
        elif user_answer == '4':  # Lister les contrats non payés
            ListContract.list_unpayed_contract()
        elif user_answer == '5':  # Lister les événements
            ListEvent.list_event()
        elif user_answer == '6':  # Ajouter un client
            add_client_prompt()
        elif user_answer == '7':  # Ajouter un événement pour un de vos clients
            add_client_prompt()
        elif user_answer == '8':  # Modifier un client
            update_client_prompt()
        elif user_answer == '9':  # Déconnexion
            print('-------------------- Déconnexion réussie --------------------')
            logout()
            break
        else:
            print(f'Erreur : valeur non acceptée ({user_answer})')


def add_client_prompt():
    name = input('Nom : ')
    email = input('Email : ')
    phone = input('Téléphone : ')
    company = input('Entreprise : ')
    information = input('Informations : ')
    date_of_first_contract = input('Date du 1er contrat (format jj/mm/aaaa) : ')
    last_maj = input('Date de la dernière mise à jour (format jj/mm/aaaa) : ')
    sale_contact_id = int(input('Commercial en charge : '))

    add_event_to_sale_client(name, email, phone, company, information, date_of_first_contract, last_maj, sale_contact_id)


def update_client_prompt():
    if not has_permission("add_client"):
        print("Vous n'avez pas la permission d'ajouter un client.")
        return

    client_id = input('ID du client à modifier : ')

    name = input('Nom : ')
    email = input('Email : ')
    phone = input('Téléphone : ')
    company = input('Entreprise : ')
    information = input('Informations : ')
    date_of_first_contract = input('Date du 1er contrat (format jj/mm/aaaa) : ')
    last_maj = input('Date de la dernière mise à jour (format jj/mm/aaaa) : ')
    sale_contact_id = int(input('Commercial en charge : '))

    update_client(
        client_id=int(client_id) if client_id else None,
        name=name if name else None,
        email=email if email else None,
        phone=phone if phone else None,
        company=company if company else None,
        information=information if information else None,
        date_of_first_contract=date_of_first_contract if date_of_first_contract else None,
        last_maj=last_maj if last_maj else None,
        sale_contact_id=int(sale_contact_id) if sale_contact_id else None
    )
