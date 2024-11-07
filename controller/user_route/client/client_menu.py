from view.menu_view import menu
from view.client.client_menu_view import client_menu
from controller.cli.cli_client import list_client, add_client, update_client, delete_client

from controller.permissions import has_permission
# from controller.user_route.menu import menu_answer


def client_menu_answer():
    while True:
        user_answer = client_menu()
        if user_answer == '1':  # list
            list_client()
        elif user_answer == '2':  # add
            add_client_prompt()
        elif user_answer == '3':  # update
            update_client_prompt()
        elif user_answer == '4':  # delete
            delete_client_prompt()
        elif user_answer == '5':  # menu
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

    add_client(name, email, phone, company, information, date_of_first_contract, last_maj, sale_contact_id)


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


def delete_client_prompt():
    client_id = int(input('ID du client à supprimer : '))
    delete_client(client_id)
