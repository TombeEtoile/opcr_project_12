def add_contract():
    print('-------------------- Ajout contrat --------------------')
    print('Veuillez ajouter le contrat à notre base de données : ')
    contract_amount = input('Montant du contrat : ')
    remains_to_be_paid = input('Reste à payer : ')
    contract_creation_date = input('Date de création du contrat (format jj/mm/aaaa) : ')
    contract_status = input('Statut du contrat ()')
    client_id = input('Identifiant du client lié : ')
    id_commercial_contact = input('Identifiant du commercial en charge : ')
    return (contract_amount, remains_to_be_paid, contract_creation_date, contract_status,
            client_id, id_commercial_contact)

