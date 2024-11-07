from models.models import Client, SaleTeam
from config.database import Session
from datetime import datetime


def list_client():
    """
        Utilisation :
            python main.py client list
    """
    session = Session()
    clients = session.query(Client).all()
    print('----- Client -----')
    for client in clients:
        print(f'{client.id} |{client.name} | {client.email} | {client.phone} | {client.company} | '
              f'{client.information}')
    session.close()


def add_client(name, email, phone, company, information, date_of_first_contract, last_maj, sale_contact_id):
    """
        Utilisation :
            python main.py client add "Nom Client" "email@example.com" "0123456789" "Nom Entreprise" "Informations" 23/05/2024 23/05/2024 1
    """
    session = Session()

    # Conversion des dates
    date_of_first_contract = datetime.strptime(date_of_first_contract, "%d/%m/%Y").date()
    last_maj = datetime.strptime(last_maj, "%d/%m/%Y").date()

    sale_contact = session.query(SaleTeam).get(sale_contact_id)

    if sale_contact:
        new_client = Client(name=name,
                            email=email,
                            phone=phone,
                            company=company,
                            information=information,
                            date_of_first_contract=date_of_first_contract,
                            last_maj=last_maj,
                            id_sale_contact=sale_contact_id)
        session.add(new_client)
        session.commit()
        print(f'{new_client} a bien été ajouté à la table Client')

    else:
        print(f"Erreur : Aucun commercial trouvé avec l'ID {sale_contact_id}")

    session.close()


def delete_client(id_client):
    """
    Utilisation :
        python main.py client delete <id_client>
    """
    session = Session()

    client_to_delete = session.query(Client).get(id_client)

    if client_to_delete:
        session.delete(client_to_delete)
        session.commit()
        print("Client supprimé avec succès.")
    else:
        print("Client introuvable.")

    session.close()


def update_client(client_id, name, email, phone, company, information, date_of_first_contract, last_maj, sale_contact_id):
    """
    Utilisation :
        python main.py client update <id_client>
    """
    session = Session()

    client = session.query(Client).get(client_id)

    if not client:
        print(f"Erreur : Aucun client trouvé avec l'ID {client_id}")
        session.close()
        return

    if name:
        client.name = name
    if email:
        client.email = email
    if phone:
        client.phone = phone
    if company:
        client.company = company
    if information:
        client.information = information
    if date_of_first_contract:
        client.date_of_first_contract = date_of_first_contract
    if last_maj:
        client.last_maj = last_maj

    session.commit()
    print(f"Client {client.id} mis à jour avec succès : {client}")
    session.close()


def client_parser(subparsers):
    cli_client_parser = subparsers.add_parser("client", help="Commandes pour SaleTeam")
    client_subparsers = cli_client_parser.add_subparsers(dest="action")

    list_parser = client_subparsers.add_parser("list", help="Lister les utilisateurs de SaleTeam")
    list_parser.set_defaults(func=list_client)

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

    delete_parser = client_subparsers.add_parser("delete", help="Supprimer un client à la table Client")
    delete_parser.add_argument("id_client", type=int, help="L'identifiant du client à supprimer")
    delete_parser.set_defaults(func=delete_client)

    update_parser = client_subparsers.add_parser("update", help="Modifier les données d'un client de la table Client")
    update_parser.add_argument("client_id", type=int, help="ID du client à mettre à jour")
    update_parser.add_argument("--name", type=str, help="Nouveau nom du client")
    update_parser.add_argument("--email", type=str, help="Nouvel email du client")
    update_parser.add_argument("--phone", type=str, help="Nouveau téléphone du client")
    update_parser.add_argument("--company", type=str, help="Nouvelle société du client")
    update_parser.add_argument("--information", type=str, help="Informations du client")
    update_parser.add_argument("--date_of_first_contract", type=str, help="Date du premier contrat du client")
    update_parser.add_argument("--last_maj", type=str, help="Date de la dernière maj du client")
    update_parser.set_defaults(func=update_client)
