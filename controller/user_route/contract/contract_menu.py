from view.menu_view import menu
from view.contract.contract_menu_view import contract_menu
from controller.cli.cli_contract import list_contract, add_contract, update_contract, delete_contract


def contract_menu_answer():
    user_answer = contract_menu()
    if user_answer == '1':  # list
        list_contract()
        menu()
    elif user_answer == '2':  # add
        add_contract_prompt()
        menu()
    elif user_answer == '3':  # update
        update_contract_prompt()
        menu()
    elif user_answer == '4':  # delete
        delete_contract_prompt()
        menu()
    elif user_answer == '5':  # menu
        menu()
    return print(f'Erreur : valeur non acceptée ({user_answer})')


def add_contract_prompt():
    contract_amount = float(input('Montant (format xxx.xx) : '))
    remains_to_be_paid = float(input('Reste à payer (format xxx.xx) : '))
    contract_creation_date = input('Date de création (format jj/mm/yyyy) : ')
    contract_status = input('Statut (True/False) : ').lower() == 'true'
    client_id = int(input('ID du client lié : '))
    id_commercial_contact = int(input('ID du commercial en charge : '))

    add_contract(contract_amount, remains_to_be_paid, contract_creation_date, contract_status, client_id,
                 id_commercial_contact)


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
        contract_status=True if contract_status.lower() == 'true' else False if contract_status.lower() == 'false' else None,
        client_id=int(client_id) if client_id else None,
        id_commercial_contact=int(id_commercial_contact) if id_commercial_contact else None
    )


def delete_contract_prompt():
    contract_id = int(input('ID du contrat à supprimer : '))
    delete_contract(contract_id)
