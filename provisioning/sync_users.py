"""
sync_users.py

Provisioning Engine

- legge gli utenti da Keycloak
- legge gli utenti da Gitea
- costruisce il provisioning plan
- opzionalmente esegue il piano
"""

from connectors.keycloak import get_users
from connectors.gitea import get_usernames

from planner import build_plan, print_plan
from executor import execute

import sys


def main():

    # True se viene passato --apply
    apply = "--apply" in sys.argv

    # Discovery
    keycloak_users = get_users()
    gitea_users = get_usernames()

    # Account locale di emergenza
    gitea_users.discard("admin")

    # Decision
    plan = build_plan(
        keycloak_users,
        gitea_users
    )

    # Mostra il piano
    print_plan(plan)

    # Execution
    if apply:

        print()
        print("Applying provisioning plan...")
        print()

        execute(plan)

    else:

        print()
        print("Dry run completed.")
        print("No changes have been applied.")
        print("Run with '--apply' to execute the provisioning plan.")


if __name__ == "__main__":
    main()