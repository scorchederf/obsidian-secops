---
mitre_id: "T1531"
mitre_name: "Account Access Removal"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--b24e2a20-3b3d-4bf0-823b-1ed765398fb0"
mitre_created: "2019-10-09T18:48:31.906Z"
mitre_modified: "2025-10-24T17:49:14.836Z"
mitre_version: "1.5"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1531/"
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
  - "SaaS"
  - "IaaS"
  - "Office Suite"
  - "ESXi"
mitre_tactic_ids:
  - "TA0040"
d3fend_ids:
  - "D3-AA"
  - "D3-AL"
  - "D3-AM"
  - "D3-CDP"
  - "D3-RUAA"
  - "D3-UAP"
  - "D3-ULA"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

Adversaries may interrupt availability of system and network resources by inhibiting access to accounts utilized by legitimate users. Accounts may be deleted, locked, or manipulated (ex: changed credentials, revoked permissions for SaaS platforms such as Sharepoint) to remove access to accounts.(Citation: Obsidian Security SaaS Ransomware June 2023) Adversaries may also subsequently log off and/or perform a [[T1529-system_shutdown_reboot|T1529: System Shutdown/Reboot]] to set malicious changes into place.(Citation: CarbonBlack LockerGoga 2019)(Citation: Unit42 LockerGoga 2019)

In Windows, [[net|Net (S0039)]] utility, `Set-LocalUser` and `Set-ADAccountPassword` [[T1059-command_and_scripting_interpreter#^t1059001-powershell|T1059.001: PowerShell]] cmdlets may be used by adversaries to modify user accounts. Accounts could also be disabled by Group Policy. In Linux, the `passwd` utility may be used to change passwords. On ESXi servers, accounts can be removed or modified via esxcli (`system account set`, `system account remove`).

Adversaries who use ransomware or similar attacks may first perform this and other Impact behaviors, such as [[T1485-data_destruction|T1485: Data Destruction]] and [[T1491-defacement|T1491: Defacement]], in order to impede incident response/recovery before completing the [[T1486-data_encrypted_for_impact|T1486: Data Encrypted for Impact]] objective. 

## Workspace

- [[workspaces/attack/techniques/T1531-account_access_removal-note|Open workspace note]]

![[workspaces/attack/techniques/T1531-account_access_removal-note]]

## Tactics

- [[TA0040-impact|TA0040: Impact]]

## D3FEND

- [[D3-AA-agent_authentication|D3-AA: Agent Authentication]]
- [[D3-AL-account_locking|D3-AL: Account Locking]]
- [[D3-AM-access_modeling|D3-AM: Access Modeling]]
- [[D3-CDP-change_default_password|D3-CDP: Change Default Password]]
- [[D3-RUAA-restore_user_account_access|D3-RUAA: Restore User Account Access]]
- [[D3-UAP-user_account_permissions|D3-UAP: User Account Permissions]]
- [[D3-ULA-unlock_account|D3-ULA: Unlock Account]]

## Platforms

- Linux
- macOS
- Windows
- SaaS
- IaaS
- Office Suite
- ESXi

