from models.models import SupportTeam
from config.database import Session


def list_support_team_collaborators(args):
    """
        Liste les collaborateurs de la table SupportTeam.

        Utilisation :
            python main.py support_team list

        Affiche :
            Affiche la liste de la support team, incluant le nom, l'email et le téléphone.
    """
    session = Session()
    users = session.query(SupportTeam).all()
    print('----- Support team -----')
    for user in users:
        print(f'{user.name} | {user.email} | {user.phone}')
    session.close()


def add_support_team_collaborator(args):
    """
        Ajoute un collaborateur dans la table SupportTeam.

        Utilisation :
            python main.py support_team add "Nom" "email@example.com" "0123456789"

        Paramètres :
        ----------
        args : argparse.Namespace
            Les arguments contenant le nom, l'email et le téléphone de l'utilisateur.
        """
    session = Session()
    new_user = SupportTeam(name=args.name, email=args.email, phone=args.phone)
    session.add(new_user)
    session.commit()
    print(f'{new_user} a bien été ajouté à la table support team')
    session.close()


def support_team_parser(subparsers):
    cli_support_team_parser = subparsers.add_parser("support_team", help="Commandes pour SupportTeam")
    support_team_subparsers = cli_support_team_parser.add_subparsers(dest="action")

    add_parser = support_team_subparsers.add_parser("add", help="Ajouter un utilisateur à SupportTeam")
    add_parser.add_argument("name", type=str, help="Nom de l'utilisateur")
    add_parser.add_argument("email", type=str, help="Email de l'utilisateur")
    add_parser.add_argument("phone", type=str, help="Téléphone de l'utilisateur")
    add_parser.set_defaults(func=add_support_team_collaborator)

    list_parser = support_team_subparsers.add_parser("list", help="Lister les utilisateurs de SupportTeam")
    list_parser.set_defaults(func=list_support_team_collaborators)
