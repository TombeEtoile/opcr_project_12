from config.database import Session
session = Session()
print("Connexion réussie !")
session.close()
