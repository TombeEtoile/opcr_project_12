from models.models import Collaborator, SaleTeam, SupportTeam, ManagementTeam
from config.database import Session
import bcrypt


def list_collaborators(args):
    """
        Liste tous les collaborateurs enregistrés dans la table Collaborator.

        Utilisation :
            python main.py collaborator list

        Affiche :
            Affiche la liste des collaborateurs, incluant l'id, le nom, l'email, le téléphone, le type d'équipe
            (sale, support, management) et l'id de l'équipe associée.

        Paramètres :
        ----------
        args : argparse.Namespace
            Les arguments de la ligne de commande fournis par argparse.
        """
    session = Session()
    collaborators = session.query(Collaborator).all()
    print('----- Collaborators -----')
    for collaborator in collaborators:
        team_info = None
        if collaborator.team_type == 'sale':
            team_info = session.query(SaleTeam).get(collaborator.id_team)
        elif collaborator.team_type == 'support':
            team_info = session.query(SupportTeam).get(collaborator.id_team)
        elif collaborator.team_type == 'management':
            team_info = session.query(ManagementTeam).get(collaborator.id_team)
        team_display = f"{team_info.name} ({team_info.email})" if team_info else "No associated team"
        print(
            f"{collaborator.id} | {collaborator.name} | {collaborator.email} | {collaborator.phone} | "
            f"{collaborator.team_type} | {team_display}")
    session.close()


def add_collaborator(args):
    """
        Ajoute un nouveau collaborateur dans la table Collaborator et l'associe à une équipe spécifique (sale, support, management).

        Utilisation :
            python main.py collaborator add "Nom" "email@example.com" "0123456789" "MotDePasse" "team_type"

        Paramètres :
        ----------
        args : argparse.Namespace
            Les arguments de la ligne de commande contenant :
            - name (str) : Nom du collaborateur.
            - email (str) : Adresse email unique du collaborateur.
            - phone (str) : Numéro de téléphone du collaborateur.
            - password (str) : Mot de passe du collaborateur, qui sera haché.
            - team_type (str) : Type d'équipe auquel le collaborateur est associé ('sale', 'support' ou 'management').

        Actions :
        --------
        - Hache le mot de passe fourni.
        - Crée une entrée dans la table d'équipe correspondante en fonction du type d'équipe.
        - Associe le collaborateur à l'id de l'équipe nouvellement créée.
        """
    session = Session()

    hashed_password = bcrypt.hashpw(args.password.encode('utf-8'), bcrypt.gensalt())

    # Créer un nouveau collaborateur
    new_collaborator = Collaborator(name=args.name,
                                    email=args.email,
                                    phone=args.phone,
                                    password=hashed_password.decode('utf-8'),
                                    team_type=args.team_type)

    # Ajouter l'utilisateur dans la table d'équipe correspondante
    if args.team_type == 'sale':
        new_team_member = SaleTeam(name=args.name, email=args.email, phone=args.phone)
        session.add(new_team_member)
        session.commit()
        new_collaborator.id_team = new_team_member.id

    elif args.team_type == 'support':
        new_team_member = SupportTeam(name=args.name, email=args.email, phone=args.phone)
        session.add(new_team_member)
        session.commit()
        new_collaborator.id_team = new_team_member.id

    elif args.team_type == 'management':
        new_team_member = ManagementTeam(name=args.name, email=args.email, phone=args.phone)
        session.add(new_team_member)
        session.commit()
        new_collaborator.id_team = new_team_member.id

    # Ajouter le collaborateur avec l'ID d'équipe mis à jour
    session.add(new_collaborator)
    session.commit()
    print(f"{new_collaborator} a bien été ajouté avec l'équipe {args.team_type}.")
    session.close()


def collaborator_parser(subparsers):
    """
        Configure les sous-commandes pour gérer les collaborateurs dans l'application CLI.

        Paramètres :
        ----------
        subparsers : argparse._SubParsersAction
            L'objet subparsers principal auquel les commandes "add" et "list" de Collaborator sont ajoutées.

        Actions :
        --------
        - Ajoute le sous-parseur pour la commande 'add' avec les arguments requis pour créer un collaborateur.
        - Ajoute le sous-parseur pour la commande 'list' pour afficher tous les collaborateurs.
        """
    cli_collaborator_parser = subparsers.add_parser("collaborator", help="Commandes pour Collaborator")
    collaborator_subparsers = cli_collaborator_parser.add_subparsers(dest="action")

    add_parser = collaborator_subparsers.add_parser("add", help="Ajouter un utilisateur à Collaborator")
    add_parser.add_argument("name", type=str, help="Nom de l'utilisateur")
    add_parser.add_argument("email", type=str, help="Email de l'utilisateur")
    add_parser.add_argument("phone", type=str, help="Téléphone de l'utilisateur")
    add_parser.add_argument("password", type=str, help="Password de l'utilisateur")
    add_parser.add_argument("team_type", type=str, help="Team associé à l'utilisateur")
    add_parser.set_defaults(func=add_collaborator)

    list_parser = collaborator_subparsers.add_parser("list", help="Lister les utilisateurs de Collaborator")
    list_parser.set_defaults(func=list_collaborators)
