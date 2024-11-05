def list_client():
    print('-------------------- Liste des clients --------------------')
    print('Selectionnez le tri que vous voulez appliquer : ')
    choice = input('1 - Par nom\n'
                   '2 - Par email\n'
                   '3 - Par telephone\n'
                   '4 - Par entreprise\n'
                   '5 - Ne pas appliquer de tri')
    return choice


def sorting_client_list():
    sorting = input('\nSelectionnez la commande de tri que vous souhaitez appliquer : ')
    return sorting
