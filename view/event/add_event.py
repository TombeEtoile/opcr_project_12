def add_event():
    print('-------------------- Ajout événement --------------------')
    print("Veuillez ajouter l'événement à notre base de données : ")
    event_date_start = input("Date de début (format jj/mm/aaaa) : ")
    event_date_end = input("Date de fin (format jj/mm/aaaa) : ")
    location = input('Localisation : ')
    attendees = input('Nombre de participants : ')
    note = input('Note : ')
    id_contract = input('Identifiant du contrat lié : ')
    id_client = input('Identifiant du client lié : ')
    id_support_team = input('Identifiant du support en charge : ')
    return (event_date_start, event_date_end,
            location, attendees, note,
            id_contract, id_client, id_support_team)
