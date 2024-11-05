from view.collaborator.collaborator_menu_view import collaborator_menu


def collaborator_menu_answer():
    user_answer = collaborator_menu()
    if user_answer == '1':
        return print("Lister les collaborateurs")
    elif user_answer == '2':
        return print("Ajouter un collaborateur")
    elif user_answer == '3':
        print("Modifier un collaborateur")
    elif user_answer == '4':
        return print('Supprimer un collaborateur')
    return print(f'Erreur : valeur non acceptée ({user_answer})')


# collaborator_menu_answer()
