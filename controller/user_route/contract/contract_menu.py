from view.contract.contract_menu_view import contract_menu


def contract_menu_answer():
    user_answer = contract_menu()
    if user_answer == '1':
        return print("Lister les contrats")
    elif user_answer == '2':
        return print("Ajouter un contrat")
    elif user_answer == '3':
        print("Modifier un contrat")
    elif user_answer == '4':
        return print('Supprimer un contrat')
    return print(f'Erreur : valeur non acceptée ({user_answer})')


# contract_menu_answer()
