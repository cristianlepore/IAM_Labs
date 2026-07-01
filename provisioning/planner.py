"""
planner.py

Costruisce il piano di provisioning.
"""


def build_plan(keycloak_users, gitea_users):

    plan = {
        "create": [],
        "update": [],
        "disable": []
    }

    for user in keycloak_users:

        username = user["username"]

        # Ignora utenti disabilitati
        if not user["enabled"]:
            continue

        # Ignora utenti che non devono usare Gitea
        if "gitea-user" not in user["roles"]:
            continue

        # Utente non presente in Gitea
        if username not in gitea_users:

            plan["create"].append(user)

            continue

        # TODO
        # Qui più avanti confronteremo email, nome, cognome
        # Se diversi -> plan["update"]

    # TODO
    # Qui individueremo gli utenti presenti in Gitea
    # ma non più autorizzati -> plan["disable"]

    return plan


def print_plan(plan):

    print()
    print("=" * 60)
    print("Provisioning Plan")
    print("=" * 60)

    for action in ("create", "update", "disable"):

        print()
        print(action.upper())
        print("-" * 20)

        if not plan[action]:
            print("None")
            continue

        for user in plan[action]:

            print(
                f"{user['username']} "
                f"({user['email']})"
            )