---
mitre_id: "T1217"
mitre_name: "Browser Information Discovery"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--5e4a2073-9643-44cb-a0b5-e7f4048446c7"
mitre_created: "2018-04-18T17:59:24.739Z"
mitre_modified: "2025-10-24T17:48:50.561Z"
mitre_version: "2.0"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1217/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Linux"
  - "macOS"
  - "Windows"
mitre_tactic_ids:
  - "TA0007"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

Adversaries may enumerate information about browsers to learn more about compromised environments. Data saved by browsers (such as bookmarks, accounts, and browsing history) may reveal a variety of personal information about users (e.g., banking sites, relationships/interests, social media, etc.) as well as details about internal network resources such as servers, tools/dashboards, or other related infrastructure.(Citation: Kaspersky Autofill)

Browser information may also highlight additional targets after an adversary has access to valid credentials, especially [[T1552-unsecured_credentials#^t1552001-credentials-in-files|T1552.001: Credentials In Files]] associated with logins cached by a browser.

Specific storage locations vary based on platform and/or application, but browser information is typically stored in local files and databases (e.g., `%APPDATA%/Google/Chrome`).(Citation: Chrome Roaming Profiles)

## Workspace

- [[workspaces/attack/techniques/T1217-browser_information_discovery-note|Open workspace note]]

![[workspaces/attack/techniques/T1217-browser_information_discovery-note]]

## Tactics

- [[TA0007-discovery|TA0007: Discovery]]

## Tools

- [[empire|Empire (S0363)]]

## Platforms

- Linux
- macOS
- Windows

