import sqlite3 as sqlite
import sqlalchemy as alchemy

conn = sqlite.connect('epic_events.db')
cursor = conn.cursor()

# Équipe Commercial
sales_team = [
    ('Vincent Lemart', 'vincent.lemart@gmail.com', '07 89 37 26 74'),
    ('Victoire Bourgeat', 'victoire.bourgeat@gmail.com', '07 49 38 56 70'),
    ('Mathieu Delafont', 'mathieu.delafont@gmail.com', '06 45 33 27 89'),
    ('Julie Renaud', 'julie.renaud@gmail.com', '07 32 47 58 90'),
    ('Pauline Châtelain', 'pauline.chatelain@gmail.com', '07 56 23 78 45')
]

# Équipe Support
support_team = [
    ('Laura Menard', 'laura.menard@gmail.com', '06 54 21 34 78'),
    ('Antoine Forestier', 'antoine.forestier@gmail.com', '06 78 90 34 21'),
    ('Emma Leclerc', 'emma.leclerc@gmail.com', '07 89 65 23 78'),
    ('Olivier Delmas', 'olivier.delmas@gmail.com', '06 56 78 34 21'),
    ('Claire Dupont', 'claire.dupont@gmail.com', '07 34 56 78 90')
]

# Équipe Gestion
management_team = [
    ('Louis Martin', 'louis.martin@gmail.com', '06 45 78 90 12'),
    ('Marie Lefebvre', 'marie.lefebvre@gmail.com', '07 23 45 67 89'),
    ('Hugo Dubois', 'hugo.dubois@gmail.com', '06 78 12 45 90'),
    ('Nathalie Bernard', 'nathalie.bernard@gmail.com', '07 45 67 23 12'),
    ('Thomas Durant', 'thomas.durant@gmail.com', '06 54 34 78 90')
]

cursor.execute("""CREATE TABLE Contract (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER,
    collaborator_id INTEGER, 
    contract_amount INTEGER,
    remains_to_be_paid INTEGER,
    contract_creation_date TEXT,
    contract_status INTEGER NOT NULL DEFAULT 0 CHECK (contract_status IN (0, 1)))
""")

conn.commit()
conn.close()
