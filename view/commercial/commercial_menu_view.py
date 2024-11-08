def commercial_menu_view():
    print('-------------------- Menu commercial --------------------')
    print('1 - Lister les clients\n'
          '2 - Lister les contrats\n'
          '3 - Lister les contrats non signés\n'
          '4 - Lister les contrats non payés'
          '5 - Lister les événements\n'
          '6 - Ajouter un client\n'
          '7 - Ajouter un événement pour un de vos clients\n'
          '8 - Modifier un client\n'
          '9 - Déconnexion')
    answer_menu = input('choix : ')
    return answer_menu


"""
- list
   - list client
   - list contract
   - filter --> unsigned contract
   - filter --> unpayed contract
   - list event
- add
   - add client
   - add event for his client
- update
   - client
"""