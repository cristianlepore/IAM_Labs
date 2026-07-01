from dotenv import load_dotenv
import os

load_dotenv()

# Gitea
GITEA_URL = os.getenv("GITEA_URL")
GITEA_TOKEN = os.getenv("GITEA_TOKEN")

# Keycloak
KEYCLOAK_URL = os.getenv("KEYCLOAK_URL")
KEYCLOAK_REALM = os.getenv("KEYCLOAK_REALM")
KEYCLOAK_ADMIN = os.getenv("KEYCLOAK_ADMIN")
KEYCLOAK_PASSWORD = os.getenv("KEYCLOAK_PASSWORD")
TARGET_REALM = os.getenv("TARGET_REALM")
