def add_collaborator():
    print('-------------------- Ajout collaborateur --------------------')
    print('Veuillez ajouter le collaborateur à notre base de données : ')
    name = input('Nom complet : ')
    email = input('Email : ')
    phone = input('Telephone : ')
    password = input('Mot de passe : ')
    team_type = input('Département (sale, support, management) : ')
    return name, email, phone, password, team_type

