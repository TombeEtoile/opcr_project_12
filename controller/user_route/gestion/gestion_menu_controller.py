from view.gestion.gestion_menu_view import gestion_menu_view

from controller.cli.cli_client import ListClient
from controller.cli.cli_event import ListEvent
from controller.cli.cli_contract import ListContract, add_contract, update_contract
from controller.cli.cli_collaborator import add_collaborator, update_collaborator, delete_collaborator

from controller.user_route.logout import logout


def gestion_menu_controller():
    while True:
        user_answer = gestion_menu_view()
        if user_answer == '1':  # Lister les clients
            ListClient.list_client()
        if user_answer == '2':  # Lister les contrats
            ListContract.list_contract()
        if user_answer == '3':  # Lister les événements
            ListEvent.list_event()
        if user_answer == '4':  # Lister les événements sans support attitré
            ListEvent.list_event_without_support()
        if user_answer == '5':  # Ajouter un collaborateur
            add_collaborator_prompt()
        if user_answer == '6':  # Ajouter un contrat
            add_contract_prompt()
        if user_answer == '7':  # Modifier un collaborateur
            update_collaborator_prompt()
        if user_answer == '8':  # Modifier un contrat
            update_contract_prompt()
        if user_answer == '9':  # Modifier un événement dont vous êtes en charge
            pass
        if user_answer == '10':  # Supprimer un collaborateur
            delete_collaborator_prompt()
        if user_answer == '11':  # Déconnexion
            print('-------------------- Déconnexion réussie --------------------')
            logout()


def add_collaborator_prompt():
    name = input('Nom : ')
    email = input('Email : ')
    phone = input('Tel : ')
    password = input('Mot de passe : ')
    team_type = input('Équipe (commercial/support/gestion) : ')

    add_collaborator(name, email,  phone, password, team_type)


def add_contract_prompt():
    contract_amount = float(input('Montant (format xxx.xx) : '))
    remains_to_be_paid = float(input('Reste à payer (format xxx.xx) : '))
    contract_creation_date = input('Date de création (format jj/mm/yyyy) : ')
    contract_status = input('Statut (True/False) : ').lower() == 'true'
    client_id = int(input('ID du client lié : '))
    id_commercial_contact = int(input('ID du commercial en charge : '))

    add_contract(contract_amount, remains_to_be_paid, contract_creation_date, contract_status, client_id,
                 id_commercial_contact)


def update_collaborator_prompt():
    collaborator_id = input('ID du collaborateur à modifier : ')

    print('Laissez vide pour garder la valeur initiale')
    name = input('Nom : ')
    email = input('Email : ')
    phone = input('Tel : ')
    password = input('Mot de passe : ')
    team_type = input('Équipe (commercial/support/gestion)')

    update_collaborator(
        collaborator_id=int(collaborator_id),
        name=name if name else None,
        email=email if email else None,
        phone=phone if phone else None,
        password=password if password else None,
        team_type=team_type if team_type else None
    )


def update_contract_prompt():
    contract_id = input("Entrez l'ID du contrat à modifier : ")

    print("Laissez vide un champ si vous ne souhaitez pas le modifier.")
    contract_amount = input('Nouveau montant (ou appuyez sur Entrée pour ignorer) : ')
    remains_to_be_paid = input('Nouveau reste à payer (ou appuyez sur Entrée pour ignorer) : ')
    contract_creation_date = input('Nouvelle date de création (jj/mm/aaaa) (ou appuyez sur Entrée pour ignorer) : ')
    contract_status = input('Nouveau statut (True/False) (ou appuyez sur Entrée pour ignorer) : ')
    client_id = input('Nouvel ID de client (ou appuyez sur Entrée pour ignorer) : ')
    id_commercial_contact = input("Nouvel ID de contact commercial (ou appuyez sur Entrée pour ignorer) : ")

    update_contract(
        contract_id=int(contract_id),
        contract_amount=float(contract_amount) if contract_amount else None,
        remains_to_be_paid=float(remains_to_be_paid) if remains_to_be_paid else None,
        contract_creation_date=contract_creation_date if contract_creation_date else None,
        contract_status=True if contract_status.lower() == 'true'
        else False if contract_status.lower() == 'false' else None,
        client_id=int(client_id) if client_id else None,
        id_commercial_contact=int(id_commercial_contact) if id_commercial_contact else None
    )


def delete_collaborator_prompt():
    collaborator_to_delete = int(input('ID du collaborateur à supprimer : '))

    delete_collaborator(collaborator_to_delete)
