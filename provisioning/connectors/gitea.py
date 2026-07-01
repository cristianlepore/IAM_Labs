import requests

from config import GITEA_URL, GITEA_TOKEN


headers = {
    "Authorization": f"token {GITEA_TOKEN}",
    "Accept": "application/json",
    "Content-Type": "application/json",
}


def get_users():
    """
    Restituisce tutti gli utenti presenti in Gitea.
    """

    r = requests.get(
        f"{GITEA_URL}/api/v1/admin/users",
        headers=headers,
        timeout=10,
    )

    r.raise_for_status()

    return r.json()


def get_usernames():
    """
    Restituisce l'insieme dei login presenti in Gitea.
    """

    return {user["login"] for user in get_users()}


def create_user(user):
    """
    Crea un nuovo utente in Gitea.
    """

    payload = {
        "username": user["username"],
        "email": user["email"] or f"{user['username']}@acme.local",

        # Password temporanea richiesta dall'API
        "password": "TemporaryPassword123!",

        # L'utente accederà tramite OIDC
        "must_change_password": True,
        "send_notify": False,
    }

    r = requests.post(
        f"{GITEA_URL}/api/v1/admin/users",
        headers=headers,
        json=payload,
        timeout=10,
    )

    if r.status_code == 201:
        print(f"✓ Created {user['username']}")
        return

    print(r.status_code)
    print(r.text)

    r.raise_for_status()