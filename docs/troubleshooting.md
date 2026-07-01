# Troubleshooting

This document summarizes the most common issues encountered during the development and configuration of the IAM Labs environment.

---

# Invalid `redirect_uri`

## Problem

After authentication, Keycloak displays an error similar to:

```text
Invalid parameter: redirect_uri
```

## Cause

The redirect URI configured in the Keycloak client does not match the callback URL used by Gitea.

## Solution

Verify the **Valid Redirect URIs** configured in the Keycloak client.

Example:

```text
http://192.168.1.11:3000/*
```

Also verify that Gitea is configured with the correct `ROOT_URL`.

---

# OpenID Connect Login Fails

## Problem

Users are redirected to Keycloak but cannot successfully authenticate.

## Cause

The OpenID Connect client is incorrectly configured.

Possible causes include:

- incorrect Client ID
- incorrect Client Secret
- invalid Discovery URL
- disabled client

## Solution

Verify the OpenID Connect configuration in both Keycloak and Gitea.

---

# Link Existing Account

## Problem

During the first login Gitea displays the **Link Account** page.

## Cause

A local Gitea account already exists.

For security reasons Gitea requires confirmation before linking the local account to the external OpenID Connect identity.

## Solution

Complete the account linking process.

This operation is required only once.

Subsequent logins occur transparently through Keycloak.

---

# User Cannot Login

## Problem

The user exists in both Keycloak and Gitea but authentication fails.

## Cause

Possible causes include:

- missing realm role
- incorrect OpenID Connect configuration
- account not linked
- user disabled

## Solution

Verify:

- the user exists in Keycloak
- the user exists in Gitea
- the `gitea-user` role is assigned
- the account has been linked successfully

---

# User Not Provisioned

## Problem

The provisioning engine does not create a user in Gitea.

## Cause

The user does not satisfy the provisioning policy.

## Solution

Verify that the user has been assigned the Keycloak realm role:

```text
gitea-user
```

Only users with this role are included in the provisioning plan.

---

# No Changes in Provisioning Plan

## Problem

The provisioning engine reports:

```text
CREATE

None

UPDATE

None

DISABLE

None
```

## Cause

Keycloak and Gitea are already synchronized.

## Solution

No action is required.

---

# ModuleNotFoundError

## Problem

Python reports:

```text
ModuleNotFoundError
```

## Cause

Required dependencies are missing or the project structure is incorrect.

## Solution

Install the project dependencies.

```bash
pip install -r requirements.txt
```

Verify that commands are executed from the `provisioning` directory.

---

# Missing python-dotenv

## Problem

Python reports:

```text
ModuleNotFoundError: No module named 'dotenv'
```

## Cause

The required package is not installed.

## Solution

Install the dependency.

```bash
pip install python-dotenv
```

or

```bash
pip install -r requirements.txt
```

---

# Import Errors

## Problem

Python cannot import local modules.

Example:

```text
ImportError

ModuleNotFoundError
```

## Cause

Incorrect project structure or invalid import statements.

## Solution

Run the provisioning engine from the project directory and use consistent package imports.

---

# REST API Authentication Fails

## Problem

The provisioning engine cannot communicate with Gitea.

## Cause

The administrator Personal Access Token is missing or invalid.

## Solution

Generate a new administrator Personal Access Token and update the configuration.

---

# Provisioning Creates No Users

## Problem

The provisioning engine completes successfully but no users are created.

## Cause

No provisioning actions were generated.

## Solution

Run the engine in dry-run mode and inspect the provisioning plan before applying changes.

```bash
python sync_users.py
```

---

# Summary

Most issues are related to one of the following areas:

- OpenID Connect configuration
- Role assignment
- Provisioning policy
- Python environment
- REST API authentication

Verifying these components usually resolves the majority of deployment and configuration problems.