---
mitre_id: "T1135"
mitre_name: "Network Share Discovery"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--3489cfc5-640f-4bb3-a103-9137b97de79f"
mitre_created: "2017-12-14T16:46:06.044Z"
mitre_modified: "2025-10-24T17:48:37.475Z"
mitre_version: "3.2"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1135/"
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

Adversaries may look for folders and drives shared on remote systems as a means of identifying sources of information to gather as a precursor for Collection and to identify potential systems of interest for Lateral Movement. Networks often contain shared network drives and folders that enable users to access file directories on various systems across a network. 

File sharing over a Windows network occurs over the SMB protocol. (Citation: Wikipedia Shared Resource) (Citation: TechNet Shared Folder) [[net|Net (S0039)]] can be used to query a remote system for available shared drives using the `net view \\\\remotesystem` command. It can also be used to query shared drives on the local system using `net share`. For macOS, the `sharing -l` command lists all shared points used for smb services.

## Workspace

- [[workspaces/attack/techniques/T1135-network_share_discovery-note|Open workspace note]]

![[workspaces/attack/techniques/T1135-network_share_discovery-note]]

## Tactics

- [[TA0007-discovery|TA0007: Discovery]]

## Mitigations

- [[M1028-operating_system_configuration|M1028: Operating System Configuration]]

## Tools
- [[crackmapexec|CrackMapExec (S0488)]]
- [[empire|Empire (S0363)]]
- [[koadic|Koadic (S0250)]]
- [[net|Net (S0039)]]
- [[pupy|Pupy (S0192)]]
- [[silenttrinity|SILENTTRINITY (S0692)]]


## Platforms

- Linux
- macOS
- Windows

