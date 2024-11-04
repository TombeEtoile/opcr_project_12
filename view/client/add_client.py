def add_client():
    print('-------------------- Ajout client --------------------')
    print('Veuillez ajouter le client à notre base de données : ')
    name = input('Nom complet : ')
    email = input('Email : ')
    phone = input('Telephone : ')
    company = input('Entreprise : ')
    information = input('Informations : ')
    date_of_first_contract = input('Date du premier contrat (format jj/mm/aaaa) : ')
    last_maj = input('Nom complet : ')
    return name, email, phone, company, information, date_of_first_contract, last_maj

