from models.models import SupportTeam
from config.database import Session


def list_support_team_collaborators(args):
    """
        Utilisation :
            python main.py support_team list
    """
    session = Session()
    users = session.query(SupportTeam).all()
    print('----- Support team -----')
    for user in users:
        print(f'{user.name} | {user.email} | {user.phone}')
    session.close()


def add_support_team_collaborator(args):
    """
        Utilisation :
            python main.py support_team add "Nom" "email@example.com" "0123456789"
        """
    session = Session()
    new_user = SupportTeam(name=args.name, email=args.email, phone=args.phone)
    session.add(new_user)
    session.commit()
    print(f'{new_user} a bien été ajouté à la table support team')
    session.close()


def delete_support(args):
    """
    Utilisation :
        python main.py support delete <id_support>
    """
    session = Session()

    support_to_delete = session.query(Support).get(args.id_support)

    if support_to_delete:
        session.delete(support_to_delete)
        session.commit()
        print("Support supprimé avec succès.")
    else:
        print("Support introuvable.")

    session.close()


def support_team_parser(subparsers):
    cli_support_team_parser = subparsers.add_parser("support_team", help="Commandes pour SupportTeam")
    support_team_subparsers = cli_support_team_parser.add_subparsers(dest="action")

    list_parser = support_team_subparsers.add_parser("list", help="Lister les utilisateurs de SupportTeam")
    list_parser.set_defaults(func=list_support_team_collaborators)

    add_parser = support_team_subparsers.add_parser("add", help="Ajouter un utilisateur à SupportTeam")
    add_parser.add_argument("name", type=str, help="Nom de l'utilisateur")
    add_parser.add_argument("email", type=str, help="Email de l'utilisateur")
    add_parser.add_argument("phone", type=str, help="Téléphone de l'utilisateur")
    add_parser.set_defaults(func=add_support_team_collaborator)

    delete_parser = support_team_subparsers.add_parser("delete", help="Supprimer un support à la table SupportTeam")
    delete_parser.add_argument("id_support", type=int, help="L'identifiant du support à supprimer")
    delete_parser.set_defaults(func=delete_support)
