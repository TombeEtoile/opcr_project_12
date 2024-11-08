from models.models import Contract, Client, SaleTeam
from config.database import Session
from datetime import datetime
from controller.permissions import has_permission


class ListContract:
    @staticmethod
    def list_contract():
        """
            Utilisation :
                python main.py contract list
        """
        session = Session()

        if not has_permission("view_all_contracts"):
            print("Vous n'avez pas la permission de voir les contrats.")
            return

        contracts = session.query(Contract).all()

        for contract in contracts:
            print('----- Contract -----')
            print(f"Contract {contract.id}: {contract.contract_amount} | Status: {contract.contract_status}")
        session.close()

    @staticmethod
    def list_unsigned_contract():
        """
            Affiche tous les contrats qui ne sont pas encore signés.
        """
        session = Session()
        contracts = session.query(Contract).filter(Contract.contract_status == False).all()

        if not contracts:
            print("Aucun contrat non signé trouvé.")
        else:
            print("'----- Contrats non signés -----'")
            for contract in contracts:
                print(
                    f"Contrat ID = {contract.id} | Montant = {contract.contract_amount} | "
                    f"Date de création = {contract.contract_creation_date}")

        session.close()

    @staticmethod
    def list_unpayed_contract():
        """
            Affiche tous les contrats qui ne sont pas encore payés.
        """
        session = Session()
        contracts = session.query(Contract).filter(Contract.remains_to_be_paid != 0).all()
        if not contracts:
            print("Aucun contrat non payé trouvé.")
        else:
            print("'----- Contrats non payés -----'")
            for contract in contracts:
                print(
                    f"Contrat ID = {contract.id} | Montant = {contract.contract_amount} | "
                    f"Reste à payer = {contract.remains_to_be_paid}"
                    f"Date de création = {contract.contract_creation_date}")

        session.close()


def add_contract(contract_amount, remains_to_be_paid, contract_creation_date, contract_status,
                 client_id, id_commercial_contact):
    """
        Utilisation :
            python main.py contract add 1300.32 300.32 23/05/2024 "True (False par défaut)" 3 7
        """
    session = Session()

    contract_creation_date = datetime.strptime(contract_creation_date, "%d/%m/%Y").date()

    client = session.query(Client).get(client_id)
    sale_contact = session.query(SaleTeam).get(id_commercial_contact)

    if client and sale_contact:
        new_contract = Contract(contract_amount=contract_amount,
                                remains_to_be_paid=remains_to_be_paid,
                                contract_creation_date=contract_creation_date,
                                contract_status=contract_status,
                                client_id=client_id,
                                id_commercial_contact=id_commercial_contact)
        session.add(new_contract)
        session.commit()
        print(f'{new_contract} a bien été ajouté à la table Contract')

    else:
        print(f"Erreur : Aucun commercial ou client n'a été trouvé avec l'ID "
              f"{id_commercial_contact} ou {client_id}")

    session.close()


def delete_contract(id_contract):
    """
    Utilisation :
        python main.py contract delete <id_contract>
    """
    session = Session()

    contract_to_delete = session.query(Contract).get(id_contract)

    if contract_to_delete:
        session.delete(contract_to_delete)
        session.commit()
        print("Contract supprimé avec succès.")
    else:
        print("Contract introuvable.")

    session.close()


def update_contract(contract_id, contract_amount, remains_to_be_paid, contract_creation_date,
                    contract_status, client_id, id_commercial_contact):
    """
    Utilisation :
        python main.py contract modify <id_contract>
    """
    session = Session()

    contract = session.query(Contract).get(contract_id)

    if not contract:
        print(f"Erreur : Aucun contract trouvé avec l'ID {contract_id}")
        session.close()
        return

    if contract_amount:
        contract.contract_amount = contract_amount
    if remains_to_be_paid:
        contract.remains_to_be_paid = remains_to_be_paid
    if contract_creation_date:
        contract.contract_creation_date = contract_creation_date
    if contract_status:
        contract.contract_status = contract_status
    if client_id:
        contract.client_id = client_id
    if id_commercial_contact:
        contract.id_commercial_contact = id_commercial_contact

    session.commit()
    print(f"Contrat {contract.id} mis à jour avec succès : {contract}")
    session.close()


def contract_parser(subparsers):
    cli_contract_parser = subparsers.add_parser("contract", help="Commandes pour Contract")
    contract_subparsers = cli_contract_parser.add_subparsers(dest="action")

    list_parser = contract_subparsers.add_parser("list", help="Lister les lignes de la table Contract")
    list_parser.set_defaults(func=ListContract.list_contract)

    add_parser = contract_subparsers.add_parser("add", help="Ajouter un contract à la table Contract")
    add_parser.add_argument("contract_amount", type=float, help="Montant du contrat")
    add_parser.add_argument("remains_to_be_paid", type=float, help="Reste à payer")
    add_parser.add_argument("contract_creation_date", type=str,
                            help="Date de création du contract (format 'dd/mm/yyyy')")
    add_parser.add_argument("contract_status", type=lambda x: (str(x).lower() == 'true'),
                            help="True = payé, False = à (finir de) payer")
    add_parser.add_argument("client_id", type=int, help="ID du client")
    add_parser.add_argument("id_commercial_contact", type=int, help="ID du commercial en charge du contrat")
    add_parser.set_defaults(func=add_contract)

    delete_parser = contract_subparsers.add_parser("delete", help="Supprimer un contract à la table Contract")
    delete_parser.add_argument("id_contract", type=int, help="L'identifiant du contract à supprimer")
    delete_parser.set_defaults(func=delete_contract)

    update_parser = contract_subparsers.add_parser("update", help="Modifier les données d'un contrat de la table "
                                                                  "Contrat")
    update_parser.add_argument("contract_id", type=int, help="ID du contrat")
    update_parser.add_argument("--contract_amount", type=int, help="Montant du contrat")
    update_parser.add_argument("--remains_to_be_paid", type=int, help="Reste à payer du contrat")
    update_parser.add_argument("--contract_creation_date", type=str, help="Date de création du contrat")
    update_parser.add_argument("--contract_status", type=bool, help="Statut du contrat")
    update_parser.add_argument("--client_id", type=lambda x: (str(x).lower() == 'true'), help="ID du client en charge")
    update_parser.add_argument("--id_commercial_contact", type=int, help="ID du commercial en charge")
    update_parser.set_defaults(func=update_contract)
