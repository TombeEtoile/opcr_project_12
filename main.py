import argparse
from controller.cli.cli_support_team import support_team_parser
from controller.cli.cli_management_team import management_team_parser
from controller.cli.cli_sale_team import sale_team_parser
from controller.cli.cli_client import client_parser
from controller.cli.cli_contract import contract_parser
from controller.cli.cli_event import event_parser
from controller.cli.cli_collaborator import collaborator_parser
from controller.user_route.registration import login
from controller.user_route.logout import logout

parser = argparse.ArgumentParser(description="Gestion de l'application CLI")
subparsers = parser.add_subparsers(dest="command")

# SUBPARSERS
client_parser(subparsers)
contract_parser(subparsers)
event_parser(subparsers)
collaborator_parser(subparsers)
sale_team_parser(subparsers)
support_team_parser(subparsers)
management_team_parser(subparsers)

# Connexion et Déconnexion
subparsers.add_parser("login", help="Connexion d'un utilisateur").set_defaults(func=login)
subparsers.add_parser("logout", help="Déconnexion de l'utilisateur").set_defaults(func=logout)

# Exécute la commande
args = parser.parse_args()
if hasattr(args, "func"):
    args.func(args)
else:
    parser.print_help()

login()
