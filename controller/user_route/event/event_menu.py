from view.event.event_menu_view import event_menu


def event_menu_answer():
    user_answer = event_menu()
    if user_answer == '1':
        return print("Lister les événements")
    elif user_answer == '2':
        return print("Ajouter un événement")
    elif user_answer == '3':
        print("Modifier un événement")
    elif user_answer == '4':
        return print('Supprimer un événement')
    return print(f'Erreur : valeur non acceptée ({user_answer})')


# event_menu_answer()
