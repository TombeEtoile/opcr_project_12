from models.models import Event, Client, Contract, SupportTeam
from config.database import Session
from datetime import datetime
from controller.permissions import has_permission
import json


def get_current_user_id():
    """Récupère l'ID de l'utilisateur connecté depuis le fichier de session."""
    try:
        with open("session_token.json", "r") as file:
            session_data = json.load(file)
            return session_data.get("id")
    except (FileNotFoundError, KeyError):
        print("Aucun utilisateur connecté.")
        return None


class ListEvent:
    @staticmethod
    def list_event():
        """
        Utilisation :
            python main.py event list
        """
        session = Session()

        if not has_permission("view_all_events"):
            print("Vous n'avez pas la permission de voir les événements.")
            return

        events = session.query(Event).all()
        print('----- Event -----')
        for event in events:
            print(f'{event.client_name} | {event.client_email} | {event.client_tel} | {event.event_date_start} | '
                  f'{event.event_date_end} | {event.support_contact} | '
                  f'{event.location} | {event.attendees} | {event.note}')
        session.close()

    @staticmethod
    def list_event_without_support():
        session = Session()
        events = session.query(Event).filter(Event.id_support_team == '').all()

        if not events:
            print("Aucun événements n'ayant aucun support atitré n'a été trouvé.")
        else:
            print("'----- Évenement(s) n'ayant aucun support atitré -----'")
            for event in events:
                print(f'{event.client_name} | {event.client_email} | {event.client_tel} | {event.event_date_start} | '
                      f'{event.event_date_end} | {event.location} | {event.attendees} | {event.note}')

        session.close()

    @staticmethod
    def list_event_dedicated_to_a_support():
        session = Session()
        events = session.query(Event).filter(Event.id_support_team == SupportTeam.id).all()

        if not events:
            print("Vous n'avez pas d'événements qui vous sont atitrés.")
        else:
            print("'----- Évenement(s) vous étant atitré(s) -----'")
            for event in events:
                print(f'{event.client_name} | {event.client_email} | {event.client_tel} | {event.event_date_start} | '
                      f'{event.event_date_end} | {event.location} | {event.attendees} | {event.note}')


def add_event(event_date_start, event_date_end, location, attendees, note, id_contract, id_client, id_support_team):
    """
       Utilisation :
           python main.py event add "01/05/2024" "02/05/2024" "Paris" 150 "Célébration d'entreprise" 2 1 3
       """
    session = Session()

    event_date_start = datetime.strptime(event_date_start, "%d/%m/%Y").date()
    event_date_end = datetime.strptime(event_date_end, "%d/%m/%Y").date()

    contract = session.query(Contract).get(id_contract)
    if not contract:
        print(f"Erreur : Aucun contrat trouvé avec l'ID {id_contract}")
    client = session.query(Client).get(id_client)
    if not client:
        print(f"Erreur : Aucun client trouvé avec l'ID {id_client}")
    support_team = session.query(SupportTeam).get(id_support_team)
    if not support_team:
        print(f"Erreur : Aucun support trouvé avec l'ID {id_support_team}")

    if contract and client and support_team:
        new_event = Event(event_date_start=event_date_start,
                          event_date_end=event_date_end,
                          location=location,
                          attendees=attendees,
                          note=note,
                          id_contract=id_contract,
                          id_client=id_client,
                          id_support_team=id_support_team)
        session.add(new_event)
        session.commit()
        print(f'{new_event} a bien été ajouté à la table Contract')

    else:
        print(f"Erreur : Aucun contrat, commercial ou client n'a été trouvé avec les ID "
              f"{id_contract} {id_client} ou {id_support_team}")
        if not id_contract:
            print('id_contract manquant')
        if not id_client:
            print('id_client manquant')
        if not id_support_team:
            print('id_support_team manquant')

    session.close()


def delete_event(event_id):
    """
    Utilisation :
        python main.py event delete <id_event>
    """
    session = Session()

    event_to_delete = session.query(Event).get(event_id)

    if event_to_delete:
        session.delete(event_to_delete)
        session.commit()
        print("Event supprimé avec succès.")
    else:
        print("Event introuvable.")

    session.close()


def update_event(event_id, event_date_start, event_date_end, location, attendees, note, id_contract,
                 id_client, id_support_team):
    """
    Utilisation :
        python main.py event modify <event>
    """
    if has_permission('update_event_assigned'):
        print("Vous n'avez pas la permission de modifier cet événement.")
        return

    session = Session()
    current_user_id = get_current_user_id()

    event = session.query(Event).filter_by(id=event_id, id_support_team=current_user_id).first()

    if not event:
        print(f"Erreur : Aucun événement trouvé avec l'ID {event_id} ou il n'est pas attribué à cet utilisateur.")
        session.close()
        return

    if event_date_start:
        event.event_date_start = event_date_start
    if event_date_end:
        event.event_date_end = event_date_end
    if location:
        event.location = location
    if attendees:
        event.attendees = attendees
    if note:
        event.note = note
    if id_contract:
        event.id_contract = id_contract
    if id_client:
        event.id_client = id_client
    if id_support_team:
        event.id_support_team = id_support_team

    session.commit()
    print(f"Événement {event.id} mis à jour avec succès : {event}")
    session.close()


def event_parser(subparsers):
    cli_event_parser = subparsers.add_parser("event", help="Commandes pour Event")
    event_subparsers = cli_event_parser.add_subparsers(dest="action")

    list_parser = event_subparsers.add_parser("list", help="Lister les lignes de la table Contract")
    list_parser.set_defaults(func=ListEvent.list_event)

    add_parser = event_subparsers.add_parser("add", help="Ajouter un event à la table Event")
    add_parser.add_argument("event_date_start", type=str,
                            help="Date de début de l'event (format 'dd/mm/yyyy')")
    add_parser.add_argument("event_date_end", type=str,
                            help="Date de fin de l'event (format 'dd/mm/yyyy')")
    add_parser.add_argument("location", type=str, help="Localisation de l'event")
    add_parser.add_argument("attendees", type=int, help="Nombre de participants à l'event")
    add_parser.add_argument("note", type=str, help="Notes à propos de l'event")
    add_parser.add_argument("id_contract", type=int, nargs='?', default=None, help="ID du contrat lié")
    add_parser.add_argument("id_client", type=int, nargs='?', default=None, help="ID du client lié")
    add_parser.add_argument("id_support_team", type=int, nargs='?', default=None, help="ID du support lié")
    add_parser.set_defaults(func=add_event)

    delete_parser = event_subparsers.add_parser("delete", help="Supprimer un événement à la table Event")
    delete_parser.add_argument("id_event", type=int, help="L'identifiant de l'événement à supprimer")
    delete_parser.set_defaults(func=delete_event)

    update_parser = event_subparsers.add_parser("update", help="Modifier les données d'un événement "
                                                               "de la table Event")
    update_parser.add_argument("event_id", type=int, help="ID de l'événement à mettre à jour")
    update_parser.add_argument("--event_date_start", type=str, help="Date de début de l'événement")
    update_parser.add_argument("--event_date_end", type=str, help="Date de fin de l'événement")
    update_parser.add_argument("--location", type=str, help="Localisation de l'événement")
    update_parser.add_argument("--attendees", type=int, help="Nombre de participant attendus à l'événement")
    update_parser.add_argument("--note", type=str, help="Informations à propos de l'événement")
    update_parser.add_argument("--id_contract", type=int, help="ID du contrat lié")
    update_parser.add_argument("--id_client", type=int, help="ID du client lié")
    update_parser.add_argument("--id_support_team", type=int, help="ID du support en charge")
    update_parser.set_defaults(func=update_event)
