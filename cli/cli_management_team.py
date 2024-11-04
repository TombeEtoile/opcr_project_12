from models.models import ManagementTeam
from config.database import Session


def list_management_team_collaborators(args):
    """
        Liste les collaborateurs de la table ManagementTeam.

        Utilisation :
            python main.py management_team list

        Affiche :
            Affiche la liste de la management team, incluant le nom, l'email et le téléphone.
    """
    session = Session()
    users = session.query(ManagementTeam).all()
    print('----- Management team -----')
    for user in users:
        print(f'{user.name} | {user.email} | {user.phone}')
    session.close()


def add_management_team_collaborator(args):
    """
    Ajoute un collaborateur dans la table ManagementTeam.

    Utilisation :
        python main.py management_team add "Nom" "email@example.com" "0123456789"

    Paramètres :
    ----------
    args : argparse.Namespace
        Les arguments contenant le nom, l'email et le téléphone de l'utilisateur.
    """

    session = Session()
    new_user = ManagementTeam(name=args.name, email=args.email, phone=args.phone)
    session.add(new_user)
    session.commit()
    print(f'{new_user} a bien été ajouté à la table management team')
    session.close()


def management_team_parser(subparsers):
    cli_management_parser = subparsers.add_parser("management_team", help="Commandes pour ManagementTeam")
    management_team_subparsers = cli_management_parser.add_subparsers(dest="action")

    add_parser = management_team_subparsers.add_parser("add", help="Ajouter un utilisateur à ManagementTeam")
    add_parser.add_argument("name", type=str, help="Nom de l'utilisateur")
    add_parser.add_argument("email", type=str, help="Email de l'utilisateur")
    add_parser.add_argument("phone", type=str, help="Téléphone de l'utilisateur")
    add_parser.set_defaults(func=add_management_team_collaborator)

    list_parser = management_team_subparsers.add_parser("list", help="Lister les utilisateurs de ManagementTeam")
    list_parser.set_defaults(func=list_management_team_collaborators)
