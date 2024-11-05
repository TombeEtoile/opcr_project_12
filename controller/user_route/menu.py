from view.menu_view import menu
from controller.user_route.contract.contract_menu import contract_menu_answer
from controller.user_route.event.event_menu import event_menu_answer
from controller.user_route.client.client_menu import client_menu_answer
from controller.user_route.collaborator.collaborator_menu import collaborator_menu_answer


def menu_answer():
    user_answer = menu()
    if user_answer == '1':
        return contract_menu_answer()
    elif user_answer == '2':
        return event_menu_answer()
    elif user_answer == '3':
        return client_menu_answer()
    elif user_answer == '4':
        return collaborator_menu_answer()
    return print(f'Erreur : valeur non acceptée ({user_answer})')


# menu_answer()
