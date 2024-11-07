from view.menu_view import menu
from view.collaborator.collaborator_menu_view import collaborator_menu
from controller.cli.cli_collaborator import (list_collaborators, add_collaborator, update_collaborator,
                                             delete_collaborator)
import bcrypt


def collaborator_menu_answer():
    user_answer = collaborator_menu()
    if user_answer == '1':  # list
        list_collaborators()
        menu()
    elif user_answer == '2':  # add
        add_collaborator_prompt()
    elif user_answer == '3':  # update
        update_collaborator_prompt()
        menu()
    elif user_answer == '4':  # delete
        delete_collaborator_prompt()
        menu()
    elif user_answer == '5':  # menu
        menu()
    return print(f'Erreur : valeur non acceptée ({user_answer})')


def add_collaborator_prompt():
    name = input('Nom : ')
    email = input('Email : ')
    phone = input('Tel : ')
    password = input('Mot de passe : ')
    team_type = input('Équipe (commercial/support/gestion) : ')

    add_collaborator(name, email,  phone, password, team_type)


def update_collaborator_prompt():
    collaborator_id = input('ID du collaborateur à modifier : ')

    print('Laissez vide pour garder la valeur initiale')
    name = input('Nom : ')
    email = input('Email : ')
    phone = input('Tel : ')
    password = input('Mot de passe : ')
    team_type = input('Équipe (commercial/support/gestion)')

    update_collaborator(
        collaborator_id=int(collaborator_id),
        name=name if name else None,
        email=email if email else None,
        phone=phone if phone else None,
        password=password if password else None,
        team_type=team_type if team_type else None
    )


def delete_collaborator_prompt():
    collaborator_to_delete = int(input('ID du collaborateur à supprimer : '))

    delete_collaborator(collaborator_to_delete)
