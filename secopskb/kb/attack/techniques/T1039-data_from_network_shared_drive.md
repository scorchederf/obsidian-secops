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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

---

Adversaries may search network shares on computers they have compromised to find files of interest. Sensitive data can be collected from remote systems via shared network drives (host shared directory, network file server, etc.) that are accessible from the current system prior to Exfiltration. Interactive command shells may be in use, and common functionality within [[cmd|cmd (S0106)]] may be used to gather information.

## Workspace

- [[workspaces/attack/techniques/T1039-data_from_network_shared_drive-note|Open workspace note]]

![[workspaces/attack/techniques/T1039-data_from_network_shared_drive-note]]

<!-- generated-detection-validation-start -->
## Detection & Validation

### CAR Analytics

- [[kb/car/analytics/CAR-2013-01-003-smb_events_monitoring|CAR-2013-01-003: SMB Events Monitoring]]

### Atomic Tests

- [[kb/atomic/tests/6ed67921_1774_44ba_bac6_adb51ed60660-copy_a_sensitive_file_over_administrative_share_with_copy|Copy a sensitive File over Administrative share with copy (command_prompt; windows)]]
- [[kb/atomic/tests/7762e120_5879_44ff_97f8_008b401b9a98-copy_a_sensitive_file_over_administrative_share_with_powershell|Copy a sensitive File over Administrative share with Powershell (powershell; windows)]]

<!-- generated-detection-validation-end -->

## Tactics

- [[TA0009-collection|TA0009: Collection]]

## D3FEND

- [[D3-DNR-decoy_network_resource|D3-DNR: Decoy Network Resource]]
- [[D3-NRAM-network_resource_access_mediation|D3-NRAM: Network Resource Access Mediation]]

## Platforms

- Linux
- macOS
- Windows

