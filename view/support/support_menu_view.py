def support_menu_view():
    print('-------------------- Menu commercial --------------------')
    print('1 - Lister les clients\n'
          '2 - Lister les contrats\n'
          '3 - Lister les événements\n'
          '4 - Lister les événements dont vous êtes responsable\n'
          '5 - Modifier un événement dont vous êtes responsable\n'
          '6 - Déconnexion')
    answer_menu = input('choix : ')
    return answer_menu


"""
support_menu()
- list
   - list client
   - filter --> his events
   - list contract
   - list event
- update
   - his events
"""