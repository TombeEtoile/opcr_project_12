from view.client.client_menu_view import client_menu


def client_menu_answer():
    user_answer = client_menu()
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
