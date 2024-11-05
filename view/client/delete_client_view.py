def delete_client():
    print('-------------------- Supprimer client --------------------')
    id_client = int(input('Identifiant du client à supprimer : '))
    print(f"Êtes vous sur de vouloir supprimer le client à l'id {id_client} ?")
    confirmation_client_id = int(input("Confirmez l'identifiant pour supprimer le client de notre bdd "
                                       "ou appuyez sur entrer pour annuler la suppression : "))
    return confirmation_client_id

