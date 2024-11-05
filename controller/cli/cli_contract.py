from models.models import Contract, Client, SaleTeam
from config.database import Session
from datetime import datetime


def list_contract(args):
    """
        Liste les contracts de la table Contract.

        Utilisation :
            python main.py contract list

        Affiche :
            Affiche la liste des contracts, incluant le nom, l'email, le téléphone, l'entreprise et les informations supplémentaires.
    """
    session = Session()
    contracts = session.query(Contract).all()
    print('----- Contract -----')
    for contract in contracts:
        print(f'{contract.contract_amount} | {contract.remains_to_be_paid} | {contract.contract_creation_date} |'
              f' {contract.contract_status}')
    session.close()


def add_contract(args):
    """
        Ajoute un contract dans la table Contract.

        Utilisation :
            python main.py contract add 1300.32 300.32 23/05/2024 "True (False par défaut)" 3 7

        Paramètres :
        ----------
        args : argparse.Namespace
            Les arguments contenant les informations du contract :
            - contract_amount (float) : montant du contract.
            - remains_to_be_paid (float) : reste à payer.
            - contract_creation_date (str) : date de création du contrat, format "dd/mm/yyyy".
            - contract_status (bool) : état du contrat (True = payé, False = à (finir de) payer).
            - client_id (int) : ID du client.
            - id_commercial_contact (int) : ID du commercial en charge.
        """
    session = Session()

    contract_creation_date = datetime.strptime(args.contract_creation_date, "%d/%m/%Y").date()

    client = session.query(Client).get(args.client_id)
    sale_contact = session.query(SaleTeam).get(args.id_commercial_contact)

    if client and sale_contact:
        new_contract = Contract(contract_amount=args.contract_amount,
                                remains_to_be_paid=args.remains_to_be_paid,
                                contract_creation_date=contract_creation_date,
                                contract_status=args.contract_status,
                                client_id=args.client_id,
                                id_commercial_contact=args.id_commercial_contact)
        session.add(new_contract)
        session.commit()
        print(f'{new_contract} a bien été ajouté à la table Contract')

    else:
        print(f"Erreur : Aucun commercial ou client n'a été trouvé avec l'ID "
              f"{args.id_commercial_contact} ou {args.client_id}")

    session.close()


def delete_contract(args):
    """
    Utilisation :
        python main.py contract delete <id_contract>
    """
    session = Session()

    contract_to_delete = session.query(Contract).get(args.id_contract)

    if contract_to_delete:
        session.delete(contract_to_delete)
        session.commit()
        print("Contract supprimé avec succès.")
    else:
        print("Contract introuvable.")

    session.close()


def update_contract(args):
    """
    Utilisation :
        python main.py contract modify <id_contract>
    """
    session = Session()

    contract = session.query(Contract).get(args.contract_id)

    if not contract:
        print(f"Erreur : Aucun contract trouvé avec l'ID {args.contract_id}")
        session.close()
        return

    if args.contract_amount:
        contract.contract_amount = args.contract_amount
    if args.remains_to_be_paid:
        contract.remains_to_be_paid = args.remains_to_be_paid
    if args.contract_creation_date:
        contract.contract_creation_date = args.contract_creation_date
    if args.contract_status:
        contract.contract_status = args.contract_status
    if args.client_id:
        contract.client_id = args.client_id
    if args.id_commercial_contact:
        contract.id_commercial_contact = args.id_commercial_contact

    session.commit()
    print(f"Contrat {contract.id} mis à jour avec succès : {contract}")
    session.close()


def contract_parser(subparsers):
    cli_contract_parser = subparsers.add_parser("contract", help="Commandes pour Contract")
    contract_subparsers = cli_contract_parser.add_subparsers(dest="action")

    list_parser = contract_subparsers.add_parser("list", help="Lister les lignes de la table Contract")
    list_parser.set_defaults(func=list_contract)

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
