def gestion_menu_view():
    print('-------------------- Menu commercial --------------------')
    print('1 - Lister les clients\n'
          '2 - Lister les contrats\n'
          '3 - Lister les événements\n'
          '4 - Lister les événements sans support attitré\n'
          '5 - Ajouter un collaborateur\n'
          '6 - Ajouter un contrat\n'
          '7 - Modifier un collaborateur\n'
          '8 - Modifier un contrat\n'
          '9 - Modifier un événement dont vous êtes en charge\n'
          '10 - Supprimer un collaborateur\n'
          '11 - Déconnexion')
    answer_menu = input('choix : ')
    return answer_menu


"""
gestion_menu()
- list
   - list client
   - list contract
   - list event
   - filter --> un(supported) event
- add
   - collaborator
   - contract
- update
   - collaborator
   - contract
   - event(support lié)
- delete
   - collaborator
"""
