from models.models import SaleTeam
from config.database import Session


def list_sale_team_collaborators(args):
    """
        Utilisation :
            python main.py sale_team list
    """
    session = Session()
    users = session.query(SaleTeam).all()
    print('----- Sale team -----')
    for user in users:
        print(f'{user.name} | {user.email} | {user.phone}')
    session.close()


def add_sale_team_collaborator(args):
    """
        Utilisation :
            python main.py sale_team add "Nom" "email@example.com" "0123456789"
        """
    session = Session()
    new_user = SaleTeam(name=args.name, email=args.email, phone=args.phone)
    session.add(new_user)
    session.commit()
    print(f'{new_user} a bien été ajouté à la table sale team')
    session.close()


def delete_sale(args):
    """
    Utilisation :
        python main.py sale delete <id_sale>
    """
    session = Session()

    sale_to_delete = session.query(SaleTeam).get(args.id_sale)

    if sale_to_delete:
        session.delete(sale_to_delete)
        session.commit()
        print("Commercial supprimé avec succès.")
    else:
        print("Commercial introuvable.")

    session.close()


def sale_team_parser(subparsers):
    cli_sale_parser = subparsers.add_parser("sale_team", help="Commandes pour SaleTeam")
    sale_team_subparsers = cli_sale_parser.add_subparsers(dest="action")

    list_parser = sale_team_subparsers.add_parser("list", help="Lister les utilisateurs de SaleTeam")
    list_parser.set_defaults(func=list_sale_team_collaborators)

    add_parser = sale_team_subparsers.add_parser("add", help="Ajouter un utilisateur à SaleTeam")
    add_parser.add_argument("name", type=str, help="Nom de l'utilisateur")
    add_parser.add_argument("email", type=str, help="Email de l'utilisateur")
    add_parser.add_argument("phone", type=str, help="Téléphone de l'utilisateur")
    add_parser.set_defaults(func=add_sale_team_collaborator)

    delete_parser = sale_team_subparsers.add_parser("delete", help="Supprimer un commercial à la table SaleTeam")
    delete_parser.add_argument("id_sale", type=int, help="L'identifiant du commerciel à supprimer")
    delete_parser.set_defaults(func=delete_sale)
