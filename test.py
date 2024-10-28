from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

# Chemin vers ta base de données SQLite existante
engine = create_engine('sqlite:///epic_events.db')

# Créer une session pour interagir avec la base de données
Session = sessionmaker(bind=engine)
session = Session()

# Exemple de requête simple pour récupérer des données (si la table existe)
result = session.execute(text("SELECT * FROM Collaborator"))
for row in result:
    print(row)
