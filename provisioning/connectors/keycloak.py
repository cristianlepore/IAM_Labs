import requests

from config import (
    KEYCLOAK_URL,
    KEYCLOAK_REALM,
    KEYCLOAK_ADMIN,
    KEYCLOAK_PASSWORD,
    TARGET_REALM,
)


def get_access_token():
    r = requests.post(
        f"{KEYCLOAK_URL}/realms/{KEYCLOAK_REALM}/protocol/openid-connect/token",
        data={
            "client_id": "admin-cli",
            "grant_type": "password",
            "username": KEYCLOAK_ADMIN,
            "password": KEYCLOAK_PASSWORD,
        },
        timeout=10,
    )

    r.raise_for_status()

    return r.json()["access_token"]


def get_users():

    token = get_access_token()

    r = requests.get(
        f"{KEYCLOAK_URL}/admin/realms/{TARGET_REALM}/users",
        headers={
            "Authorization": f"Bearer {token}"
        },
        timeout=10,
    )

    r.raise_for_status()

    users = []

    for user in r.json():

        users.append({
            "id": user["id"],
            "username": user["username"],
            "email": user.get("email"),
            "first_name": user.get("firstName"),
            "last_name": user.get("lastName"),
            "enabled": user["enabled"],
            "roles": get_realm_roles(user["id"], token)
        })

    return users


def get_realm_roles(user_id, token):

    r = requests.get(
        f"{KEYCLOAK_URL}/admin/realms/{TARGET_REALM}/users/{user_id}/role-mappings/realm",
        headers={
            "Authorization": f"Bearer {token}"
        },
        timeout=10,
    )

    r.raise_for_status()

    return {role["name"] for role in r.json()}


def get_usernames():
    users = get_users()
    return {user["username"] for user in users}
