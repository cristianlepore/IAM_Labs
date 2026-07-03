# Architecture 0 – Local Authentication

## Business Scenario

ACME is a small software startup with fewer than ten employees.

Each application manages its own users independently through local accounts. Authentication and authorization are performed separately by every application, with no centralized identity management.

Although this approach is simple and inexpensive, it quickly becomes difficult to manage as the company grows and the number of enterprise applications increases.

## Business Problem

How can a small company manage user identities before adopting an Identity Provider?

## Learning Objectives

- Understand local authentication and authorization.
- Identify the limitations of application-managed identities.
- Understand why centralized identity becomes necessary as organizations grow.

## Technologies

- Gitea
- Local Users

## Architecture Overview

- Local authentication
- Local authorization
- Per-application identity management

## Learning Outcomes

After completing this architecture, learners will understand the limitations of local account management and the business motivations that lead organizations to adopt centralized Identity and Access Management solutions.
