from models.models import Event, Client, Contract, SupportTeam
from config.database import Session
from datetime import datetime


def list_event(args):
    """
    Liste les events de la table Event

    Utilisation :
        python main.py event list

    Affiche :
        Affiche la liste des events incluant l'id du client relié, son nom, son email, son tel, la date de début de l'event, la date de fin, le contact du support (nom, email et tel), la localisation de l'event, et une note à propos de cet event.
    """
    session = Session()
    events = session.query(Event).all()
    print('----- Event -----')
    for event in events:
        print(f'{event.client_name} | {event.client_email} | {event.client_tel} | {event.event_date_start} | '
              f'{event.event_date_end} | {event.support_contact} | '
              f'{event.location} | {event.attendees} | {event.note}')
    session.close()


def add_event(args):
    """
       Ajoute un événement dans la table Event.

       Utilisation :
           python main.py event add "01/05/2024" "02/05/2024" "Paris" 150 "Célébration d'entreprise" 2 1 3

       Paramètres :
       ----------
       args : argparse.Namespace
           Les arguments contenant les informations de l'événement :
           - event_date_start (str) : Date de début de l'événement (format 'dd/mm/yyyy').
           - event_date_end (str) : Date de fin de l'événement (format 'dd/mm/yyyy').
           - location (str) : Lieu de l'événement.
           - attendees (int) : Nombre de participants attendus.
           - note (str) : Notes ou remarques spécifiques pour l'événement.
           - id_contract (int) : ID du contrat associé à l'événement.
           - id_client (int) : ID du client lié à l'événement.
           - id_support_team (int) : ID de l'équipe support responsable de l'événement.

       Actions :
       --------
       Vérifie que le contrat, le client et l'équipe support existent en base. Si tous sont présents, crée un nouvel enregistrement dans la table Event avec les informations fournies.
       """
    session = Session()

    event_date_start = datetime.strptime(args.event_date_start, "%d/%m/%Y").date()
    event_date_end = datetime.strptime(args.event_date_end, "%d/%m/%Y").date()

    contract = session.query(Contract).get(args.id_contract)
    if not contract:
        print(f"Erreur : Aucun contrat trouvé avec l'ID {args.id_contract}")
    client = session.query(Client).get(args.id_client)
    if not client:
        print(f"Erreur : Aucun client trouvé avec l'ID {args.id_client}")
    support_team = session.query(SupportTeam).get(args.id_support_team)
    if not support_team:
        print(f"Erreur : Aucun support trouvé avec l'ID {args.id_support_team}")

    if contract and client and support_team:
        new_event = Event(event_date_start=event_date_start,
                          event_date_end=event_date_end,
                          location=args.location,
                          attendees=args.attendees,
                          note=args.note,
                          id_contract=args.id_contract,
                          id_client=args.id_client,
                          id_support_team=args.id_support_team)
        session.add(new_event)
        session.commit()
        print(f'{new_event} a bien été ajouté à la table Contract')

    else:
        print(f"Erreur : Aucun contrat, commercial ou client n'a été trouvé avec les ID "
              f"{args.id_contract} {args.id_client} ou {args.id_support_team}")
        if not args.id_contract:
            print('id_contract manquant')
        if not args.id_client:
            print('id_client manquant')
        if not args.id_support_team:
            print('id_support_team manquant')

    session.close()


def event_parser(subparsers):
    cli_event_parser = subparsers.add_parser("event", help="Commandes pour Event")
    event_subparsers = cli_event_parser.add_subparsers(dest="action")

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

    list_parser = event_subparsers.add_parser("list", help="Lister les lignes de la table Contract")
    list_parser.set_defaults(func=list_event)
