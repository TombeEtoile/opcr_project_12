from view.client.add_client_view import add_client


def add_client_answer():
    user_answer = add_client()
    if user_answer == '1':
        return print("Lister les clients")
    elif user_answer == '2':
        return print("Ajouter un client")
    elif user_answer == '3':
        print("Modifier un client")
    elif user_answer == '4':
        return print('Supprimer un client')
    return print(f'Erreur : valeur non acceptée ({user_answer})')


# client_menu_answer()
