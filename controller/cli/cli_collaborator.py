from models.models import Collaborator, SaleTeam, SupportTeam, ManagementTeam
from config.database import Session
import bcrypt
from controller.permissions import has_permission


def list_collaborators():
    """
        Utilisation :
            python main.py collaborator list
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


def add_collaborator(name, email, phone, password, team_type):
    """
        Utilisation :
            python main.py collaborator add "Nom" "email@example.com" "0123456789" "MotDePasse" "team_type"
        """
    session = Session()

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    # Créer un nouveau collaborateur
    new_collaborator = Collaborator(name=name,
                                    email=email,
                                    phone=phone,
                                    password=hashed_password.decode('utf-8'),
                                    team_type=team_type)

    # Ajouter l'utilisateur dans la table d'équipe correspondante
    if team_type == 'commercial':
        new_team_member = SaleTeam(name=name, email=email, phone=phone)
        session.add(new_team_member)
        session.commit()
        new_collaborator.id_team = new_team_member.id

    elif team_type == 'support':
        new_team_member = SupportTeam(name=name, email=email, phone=phone)
        session.add(new_team_member)
        session.commit()
        new_collaborator.id_team = new_team_member.id

    elif team_type == 'gestion':
        new_team_member = ManagementTeam(name=name, email=email, phone=phone)
        session.add(new_team_member)
        session.commit()
        new_collaborator.id_team = new_team_member.id

    # Ajouter le collaborateur avec l'ID d'équipe mis à jour
    session.add(new_collaborator)
    session.commit()
    print(f"{new_collaborator} a bien été ajouté avec l'équipe {team_type}.")
    session.close()


def delete_collaborator(id_collaborator):
    """
    Utilisation :
        python main.py collaborator delete <id_collaborator>
    """
    session = Session()

    collaborator_to_delete = session.query(Collaborator).get(id_collaborator)

    if collaborator_to_delete:
        session.delete(collaborator_to_delete)
        session.commit()
        print("collaborator supprimé avec succès.")
    else:
        print("collaborator introuvable.")

    session.close()


def update_collaborator(collaborator_id, name, email, phone, password, team_type):
    """
    Utilisation :
        python main.py collaborator modify <id_collaborator>
    """
    session = Session()

    collaborator = session.query(Collaborator).get(collaborator_id)

    if not collaborator:
        print(f"Erreur : Aucun collaborateur trouvé avec l'ID {collaborator_id}")
        session.close()
        return

    if name:
        collaborator.name = name
    if email:
        collaborator.email = email
    if phone:
        collaborator.phone = phone
    if password:
        collaborator.password = password
    if team_type:
        collaborator.team_type = team_type

    session.commit()
    print(f"Événement {collaborator.id} mis à jour avec succès : {collaborator}")
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

    list_parser = collaborator_subparsers.add_parser("list", help="Lister les utilisateurs de Collaborator")
    list_parser.set_defaults(func=list_collaborators)

    add_parser = collaborator_subparsers.add_parser("add", help="Ajouter un utilisateur à Collaborator")
    add_parser.add_argument("name", type=str, help="Nom de l'utilisateur")
    add_parser.add_argument("email", type=str, help="Email de l'utilisateur")
    add_parser.add_argument("phone", type=str, help="Téléphone de l'utilisateur")
    add_parser.add_argument("password", type=str, help="Password de l'utilisateur")
    add_parser.add_argument("team_type", type=str, help="Team associé à l'utilisateur")
    add_parser.set_defaults(func=add_collaborator)

    delete_parser = collaborator_subparsers.add_parser("delete", help="Supprimer un collaborator à "
                                                                      "la table Collaborator")
    delete_parser.add_argument("id_collaborator", type=int, help="L'identifiant du collaborator à supprimer")
    delete_parser.set_defaults(func=delete_collaborator)

    update_parser = collaborator_subparsers.add_parser("update", help="Modifier les données d'un événement "
                                                                      "de la table Collaborator")
    update_parser.add_argument("collaborator_id", type=int, help="ID du collaborateur à mettre à jour")
    update_parser.add_argument("--name", type=str, help="Nom du collaborateur")
    update_parser.add_argument("--email", type=str, help="Email du collaborateur")
    update_parser.add_argument("--phone", type=str, help="Téléphone du collaborateur")
    update_parser.add_argument("--password", type=str, help="mot de passe du collaborateur")
    update_parser.add_argument("--team_type", type=str, help="Équipe du collaborateur")
    update_parser.set_defaults(func=update_collaborator)

