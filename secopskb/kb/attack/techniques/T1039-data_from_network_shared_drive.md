---
mitre_id: "T1039"
mitre_name: "Data from Network Shared Drive"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--ae676644-d2d2-41b7-af7e-9bed1b55898c"
mitre_created: "2017-05-31T21:30:41.022Z"
mitre_modified: "2025-10-24T17:49:13.555Z"
mitre_version: "1.5"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1039/"
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
  - "TA0009"
d3fend_ids:
  - "D3-DNR"
  - "D3-NRAM"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[workspaces/index|Notes]]

---

Adversaries may search network shares on computers they have compromised to find files of interest. Sensitive data can be collected from remote systems via shared network drives (host shared directory, network file server, etc.) that are accessible from the current system prior to Exfiltration. Interactive command shells may be in use, and common functionality within [[cmd|cmd (S0106)]] may be used to gather information.

## Workspace

- [[workspaces/attack/techniques/T1039-data_from_network_shared_drive-note|Open workspace note]]

![[workspaces/attack/techniques/T1039-data_from_network_shared_drive-note]]

## Tactics

- [[TA0009-collection|TA0009: Collection]]

## D3FEND

- [[D3-DNR-decoy_network_resource|D3-DNR: Decoy Network Resource]]
- [[D3-NRAM-network_resource_access_mediation|D3-NRAM: Network Resource Access Mediation]]

## Platforms

- Linux
- macOS
- Windows

