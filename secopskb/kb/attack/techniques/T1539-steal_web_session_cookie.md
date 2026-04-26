---
mitre_id: "T1539"
mitre_name: "Steal Web Session Cookie"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--10ffac09-e42d-4f56-ab20-db94c67d76ff"
mitre_created: "2019-10-08T20:04:35.508Z"
mitre_modified: "2025-10-24T17:48:25.272Z"
mitre_version: "1.5"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1539/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Linux"
  - "Office Suite"
  - "SaaS"
  - "Windows"
  - "macOS"
mitre_tactic_ids:
  - "TA0006"
d3fend_ids:
  - "D3-ANCI"
  - "D3-CCSA"
  - "D3-CH"
  - "D3-CR"
  - "D3-CRO"
  - "D3-CTS"
  - "D3-DUC"
  - "D3-MFA"
  - "D3-RIC"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

An adversary may steal web application or service session cookies and use them to gain access to web applications or Internet services as an authenticated user without needing credentials. Web applications and services often use session cookies as an authentication token after a user has authenticated to a website.

Cookies are often valid for an extended period of time, even if the web application is not actively used. Cookies can be found on disk, in the process memory of the browser, and in network traffic to remote systems. Additionally, other applications on the targets machine might store sensitive authentication cookies in memory (e.g. apps which authenticate to cloud services). Session cookies can be used to bypasses some multi-factor authentication protocols.(Citation: Pass The Cookie)

There are several examples of malware targeting cookies from web browsers on the local system.(Citation: Kaspersky TajMahal April 2019)(Citation: Unit 42 Mac Crypto Cookies January 2019) Adversaries may also steal cookies by injecting malicious JavaScript content into websites or relying on [[T1204-user_execution|T1204: User Execution]] by tricking victims into running malicious JavaScript in their browser.(Citation: Talos Roblox Scam 2023)(Citation: Krebs Discord Bookmarks 2023)

There are also open source frameworks such as `Evilginx2` and `Muraena` that can gather session cookies through a malicious proxy (e.g., [[T1557-adversary-in-the-middle|T1557: Adversary-in-the-Middle]]) that can be set up by an adversary and used in phishing campaigns.(Citation: Github evilginx2)(Citation: GitHub Mauraena)

After an adversary acquires a valid cookie, they can then perform a [[T1550-use_alternate_authentication_material#^t1550004-web-session-cookie|T1550.004: Web Session Cookie]] technique to login to the corresponding web application.

## Workspace

- [[workspaces/attack/techniques/T1539-steal_web_session_cookie-note|Open workspace note]]

![[workspaces/attack/techniques/T1539-steal_web_session_cookie-note]]

## Tactics

- [[TA0006-credential_access|TA0006: Credential Access]]

## D3FEND

- [[D3-ANCI-authentication_cache_invalidation|D3-ANCI: Authentication Cache Invalidation]]
- [[D3-CCSA-credential_compromise_scope_analysis|D3-CCSA: Credential Compromise Scope Analysis]]
- [[D3-CH-credential_hardening|D3-CH: Credential Hardening]]
- [[D3-CR-credential_revocation|D3-CR: Credential Revocation]]
- [[D3-CRO-credential_rotation|D3-CRO: Credential Rotation]]
- [[D3-CTS-credential_transmission_scoping|D3-CTS: Credential Transmission Scoping]]
- [[D3-DUC-decoy_user_credential|D3-DUC: Decoy User Credential]]
- [[D3-MFA-multi-factor_authentication|D3-MFA: Multi-factor Authentication]]
- [[D3-RIC-reissue_credential|D3-RIC: Reissue Credential]]

## Mitigations

- [[M1017-user_training|M1017: User Training]]
- [[M1021-restrict_web-based_content|M1021: Restrict Web-Based Content]]
- [[M1032-multi-factor_authentication|M1032: Multi-factor Authentication]]
- [[M1047-audit|M1047: Audit]]
- [[M1051-update_software|M1051: Update Software]]
- [[M1054-software_configuration|M1054: Software Configuration]]

## Platforms

- Linux
- Office Suite
- SaaS
- Windows
- macOS

