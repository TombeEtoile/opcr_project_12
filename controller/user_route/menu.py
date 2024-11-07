from view.menu_view import menu
from controller.user_route.contract.contract_menu import contract_menu_answer
from controller.user_route.event.event_menu import event_menu_answer
from controller.user_route.client.client_menu import client_menu_answer
from controller.user_route.collaborator.collaborator_menu import collaborator_menu_answer
from controller.user_route.logout import logout


def menu_answer():
    while True:
        user_answer = menu()
        if user_answer == '1':
            contract_menu_answer()
        elif user_answer == '2':
            event_menu_answer()
        elif user_answer == '3':
            client_menu_answer()
        elif user_answer == '4':
            collaborator_menu_answer()
        elif user_answer == '5':
            print('-------------------- Déconnexion réussie --------------------')
            logout()
            break
        else:
            print(f'Erreur : valeur non acceptée ({user_answer})')

