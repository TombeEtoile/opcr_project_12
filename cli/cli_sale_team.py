from models.models import SaleTeam
from config.database import Session


def list_sale_team_collaborators(args):
    """
        Liste les collaborateurs de la table SaleTeam.

        Utilisation :
            python main.py sale_team list

        Affiche :
            Affiche la liste de la sale team, incluant le nom, l'email et le téléphone.
    """
    session = Session()
    users = session.query(SaleTeam).all()
    print('----- Sale team -----')
    for user in users:
        print(f'{user.name} | {user.email} | {user.phone}')
    session.close()


def add_sale_team_collaborator(args):
    """
        Ajoute un collaborateur dans la table SaleTeam.

        Utilisation :
            python main.py sale_team add "Nom" "email@example.com" "0123456789"

        Paramètres :
        ----------
        args : argparse.Namespace
            Les arguments contenant le nom, l'email et le téléphone de l'utilisateur.
        """
    session = Session()
    new_user = SaleTeam(name=args.name, email=args.email, phone=args.phone)
    session.add(new_user)
    session.commit()
    print(f'{new_user} a bien été ajouté à la table sale team')
    session.close()


def sale_team_parser(subparsers):
    cli_sale_parser = subparsers.add_parser("sale_team", help="Commandes pour SaleTeam")
    sale_team_subparsers = cli_sale_parser.add_subparsers(dest="action")

    add_parser = sale_team_subparsers.add_parser("add", help="Ajouter un utilisateur à SaleTeam")
    add_parser.add_argument("name", type=str, help="Nom de l'utilisateur")
    add_parser.add_argument("email", type=str, help="Email de l'utilisateur")
    add_parser.add_argument("phone", type=str, help="Téléphone de l'utilisateur")
    add_parser.set_defaults(func=add_sale_team_collaborator)

    list_parser = sale_team_subparsers.add_parser("list", help="Lister les utilisateurs de SaleTeam")
    list_parser.set_defaults(func=list_sale_team_collaborators)
