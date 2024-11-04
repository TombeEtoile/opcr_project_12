from models.models import Client, SaleTeam
from config.database import Session
from datetime import datetime


def list_client(args):
    """
        Liste les clients de la table Client.

        Utilisation :
            python main.py client list

        Affiche :
            Affiche la liste des clients, incluant le nom, l'email, le téléphone, l'entreprise et les informations supplémentaires.
    """
    session = Session()
    clients = session.query(Client).all()
    print('----- Client -----')
    for client in clients:
        print(f'{client.name} | {client.email} | {client.phone} | {client.company} | {client.information}')
    session.close()


def add_client(args):
    """
        Ajoute un client dans la table Client.

        Utilisation :
            python main.py client add "Nom Client" "email@example.com" "0123456789" "Nom Entreprise" "Informations" 23/05/2024 23/05/2024 1

        Paramètres :
        ----------
        args : argparse.Namespace
            Les arguments contenant les informations du client :
            - name (str) : Nom du client.
            - email (str) : Email du client.
            - phone (str) : Téléphone du client.
            - company (str) : Nom de l'entreprise du client.
            - information (str) : Informations supplémentaires sur le client.
            - date_of_first_contract (str) : Date du premier contrat.
            - last_maj (str) : Date de la dernière mise à jour.
        """
    session = Session()

    # Conversion des dates
    date_of_first_contract = datetime.strptime(args.date_of_first_contract, "%d/%m/%Y").date()
    last_maj = datetime.strptime(args.last_maj, "%d/%m/%Y").date()

    sale_contact = session.query(SaleTeam).get(args.sale_contact_id)

    if sale_contact:
        new_client = Client(name=args.name,
                            email=args.email,
                            phone=args.phone,
                            company=args.company,
                            information=args.information,
                            date_of_first_contract=date_of_first_contract,
                            last_maj=last_maj,
                            id_sale_contact=args.sale_contact_id)
        session.add(new_client)
        session.commit()
        print(f'{new_client} a bien été ajouté à la table Client')

    else:
        print(f"Erreur : Aucun commercial trouvé avec l'ID {args.sale_contact_id}")

    session.close()


def client_parser(subparsers):
    cli_client_parser = subparsers.add_parser("client", help="Commandes pour SaleTeam")
    client_subparsers = cli_client_parser.add_subparsers(dest="action")

    add_parser = client_subparsers.add_parser("add", help="Ajouter un client à la table Client")
    add_parser.add_argument("name", type=str, help="Nom du client")
    add_parser.add_argument("email", type=str, help="Email du client")
    add_parser.add_argument("phone", type=str, help="Téléphone du client")
    add_parser.add_argument("company", type=str, help="Entreprise du client")
    add_parser.add_argument("information", type=str, help="Informations à propos du client")
    add_parser.add_argument("date_of_first_contract", type=str,
                            help="Date du premier contrat du client (format 'dd/mm/yyyy')")
    add_parser.add_argument("last_maj", type=str, help="Date de la dernière mise à jour (format 'dd/mm/yyyy')")
    add_parser.add_argument("sale_contact_id", type=int, help="ID du commercial dans SaleTeam")
    add_parser.set_defaults(func=add_client)

    list_parser = client_subparsers.add_parser("list", help="Lister les utilisateurs de SaleTeam")
    list_parser.set_defaults(func=list_client)
