import argparse
from cli.cli_support_team import support_team_parser
from cli.cli_management_team import management_team_parser
from cli.cli_sale_team import sale_team_parser
from cli.cli_client import client_parser
from cli.cli_contract import contract_parser
from cli.cli_event import event_parser
from cli.cli_collaborator import collaborator_parser

parser = argparse.ArgumentParser(description="Gestion de l'application CLI")
subparsers = parser.add_subparsers(dest="command")


# SUBPARSERS
# Client
client_parser(subparsers)
# Contract
contract_parser(subparsers)
# Event
event_parser(subparsers)
# Collaborator
collaborator_parser(subparsers)
# Sale team
sale_team_parser(subparsers)
# Support team
support_team_parser(subparsers)
# Management team
management_team_parser(subparsers)


# Éxécute la commande
args = parser.parse_args()
if hasattr(args, "func"):
    args.func(args)
else:
    parser.print_help()
