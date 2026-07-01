from connectors.gitea import create_user

def execute(plan):

    print("\nExecuting provisioning plan...\n")

    for user in plan["create"]:

        print(f"[CREATE] {user['username']}")

        create_user(user)

    print("\nProvisioning completed.")