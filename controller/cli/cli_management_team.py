from models.models import ManagementTeam
from config.database import Session


def list_management_team_collaborators(args):
    """
        Utilisation :
            python main.py management_team list
    """
    session = Session()
    users = session.query(ManagementTeam).all()
    print('----- Management team -----')
    for user in users:
        print(f'{user.name} | {user.email} | {user.phone}')
    session.close()


def add_management_team_collaborator(args):
    """
    Utilisation :
        python main.py management_team add "Nom" "email@example.com" "0123456789"
    """

    session = Session()
    new_user = ManagementTeam(name=args.name, email=args.email, phone=args.phone)
    session.add(new_user)
    session.commit()
    print(f'{new_user} a bien été ajouté à la table management team')
    session.close()


def delete_manager(args):
    """
    Utilisation :
        python main.py manager delete <id_manager>
    """
    session = Session()

    manager_to_delete = session.query(ManagementTeam).get(args.id_manager)

    if manager_to_delete:
        session.delete(manager_to_delete)
        session.commit()
        print("Manageur supprimé avec succès.")
    else:
        print("Manageur introuvable.")

    session.close()


def management_team_parser(subparsers):
    cli_management_parser = subparsers.add_parser("management_team", help="Commandes pour ManagementTeam")
    management_team_subparsers = cli_management_parser.add_subparsers(dest="action")

    list_parser = management_team_subparsers.add_parser("list", help="Lister les utilisateurs de ManagementTeam")
    list_parser.set_defaults(func=list_management_team_collaborators)

    add_parser = management_team_subparsers.add_parser("add", help="Ajouter un utilisateur à ManagementTeam")
    add_parser.add_argument("name", type=str, help="Nom de l'utilisateur")
    add_parser.add_argument("email", type=str, help="Email de l'utilisateur")
    add_parser.add_argument("phone", type=str, help="Téléphone de l'utilisateur")
    add_parser.set_defaults(func=add_management_team_collaborator)

    delete_parser = management_team_subparsers.add_parser("delete", help="Supprimer un manager à la table "
                                                                         "ManagementTeam")
    delete_parser.add_argument("id_manager", type=int, help="L'identifiant du manageur à supprimer")
    delete_parser.set_defaults(func=delete_manager)
