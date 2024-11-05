#  Définition des tables avec SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, ForeignKey, Integer, String, Date, Boolean, Float
from sqlalchemy.orm import relationship


Base = declarative_base()


class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)
    event_date_start = Column(Date)
    event_date_end = Column(Date)
    location = Column(String)
    attendees = Column(Integer)
    note = Column(String)

    # ForeignKey to contract id
    id_contract = Column(Integer, ForeignKey('contracts.id'), nullable=True)
    contracts = relationship('Contract')

    # ForeignKey to client id
    id_client = Column(Integer, ForeignKey('clients.id'), nullable=True)
    client = relationship('Client')

    # ForeignKey to support_team id
    id_support_team = Column(Integer, ForeignKey('supports_team.id'), nullable=True)
    supports = relationship('SupportTeam')

    def __repr__(self):
        return f'Event n°{self.id}'


class Contract(Base):
    __tablename__ = 'contracts'

    id = Column(Integer, primary_key=True)
    contract_amount = Column(Float)
    remains_to_be_paid = Column(Float)
    contract_creation_date = Column(Date)
    contract_status = Column(Boolean, default=False)

    # ForeignKey to client id
    client_id = Column(Integer, ForeignKey('clients.id'), nullable=True)
    client = relationship('Client')

    # ForeignKey to sale id
    id_commercial_contact = Column(Integer, ForeignKey('sales_team.id'), nullable=True)
    sales_team = relationship('SaleTeam')

    # backref to event
    contract_to_event = relationship(Event, backref='backref_contract_to_event')

    def __repr__(self):
        return f'Contract n°{self.id}'


class Client(Base):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True)
    information = Column(String)
    name = Column(String)
    email = Column(String)
    phone = Column(String)
    company = Column(String)
    date_of_first_contract = Column(Date)
    last_maj = Column(Date)

    # ForeignKey to sales contact
    id_sale_contact = Column(Integer, ForeignKey('sales_team.id'), nullable=True)
    sales_team = relationship('SaleTeam')

    # backref to contract
    client_to_contract = relationship(Contract, backref='backref_client_to_contract')

    # backref to client
    client_to_event = relationship(Event, backref='backref_client_to_event')

    def __repr__(self):
        return f'Client - {self.name}'


class Collaborator(Base):
    __tablename__ = 'collaborators'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String, nullable=True)
    password = Column(String, nullable=False)
    team_type = Column(String, nullable=False)  # 'sale' 'support' 'management'
    id_team = Column(Integer)

    def __repr__(self):
        return f'Collaborator {self.name} (Team: {self.team_type}, ID: {self.id_team})'


class SaleTeam(Base):
    __tablename__ = 'sales_team'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    phone = Column(String)

    # backref to contract
    sale_team_to_contract = relationship(Contract, backref='backref_sale_team_to_contract')

    # backref to client
    sale_team_to_client = relationship(Client, backref='backref_sale_team_to_client')

    # Relation vers les collaborateurs (de type "sale")
    # sale_team_to_collaborators = relationship('Collaborator',
                                            # primaryjoin="and_(Collaborator.id_team == SaleTeam.id, "
                                                          # "Collaborator.team_type == 'sale')", viewonly=True)

    def __repr__(self):
        return f'Sales team {self.name}'


class SupportTeam(Base):
    __tablename__ = 'supports_team'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    phone = Column(String)

    # backref to event
    support_to_event = relationship(Event, backref='backref_support_to_event')

    # Relation vers les collaborateurs (de type "support")
    # support_to_collaborators = relationship('Collaborator',
                                            # primaryjoin="and_(Collaborator.id_team == SupportTeam.id, "
                                                        # "Collaborator.team_type == 'support')", viewonly=True)

    def __repr__(self):
        return f'Support team {self.name}'


class ManagementTeam(Base):
    __tablename__ = 'managements_team'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    phone = Column(String)

    # Relation vers les collaborateurs (de type "management")
    # management_to_collaborators = relationship('Collaborator',
                                               # primaryjoin="and_(Collaborator.id_team == ManagementTeam.id, "
                                                           # "Collaborator.team_type == 'management')", viewonly=True)

    def __repr__(self):
        return f'Management team {self.name}'

'''
engine = create_engine('sqlite:///database/epic_events_bdd.db', echo=True)
Base.metadata.create_all(engine)
'''
'''
OU


import os

# Définir le chemin absolu de la base de données
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_PATH = os.path.join(BASE_DIR, '../database/epic_events_bdd.db')

# Créer l'engine avec le chemin absolu
engine = create_engine(f'sqlite:///{DATABASE_PATH}', echo=True)
Base.metadata.create_all(engine)
'''
