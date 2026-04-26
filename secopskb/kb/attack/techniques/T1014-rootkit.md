---
mitre_id: "T1014"
mitre_name: "Rootkit"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--0f20e3cb-245b-4a61-8a91-2d93f7cb0e9b"
mitre_created: "2017-05-31T21:30:26.496Z"
mitre_modified: "2025-10-24T17:48:24.032Z"
mitre_version: "1.3"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1014/"
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
  - "TA0005"
d3fend_ids:
  - "D3-AVE"
  - "D3-CF"
  - "D3-CM"
  - "D3-CQ"
  - "D3-DF"
  - "D3-FA"
  - "D3-FBA"
  - "D3-FE"
  - "D3-FEMC"
  - "D3-FEV"
  - "D3-FIM"
  - "D3-FV"
  - "D3-LFP"
  - "D3-RF"
  - "D3-RFAM"
  - "D3-RS"
  - "D3-SU"
  - "D3-SWI"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[workspaces/index|Notes]]

---

Adversaries may use rootkits to hide the presence of programs, files, network connections, services, drivers, and other system components. Rootkits are programs that hide the existence of malware by intercepting/hooking and modifying operating system API calls that supply system information. (Citation: Symantec Windows Rootkits) 

Rootkits or rootkit enabling functionality may reside at the user or kernel level in the operating system or lower, to include a hypervisor or [[T1542-pre-os_boot#^t1542001-system-firmware|T1542.001: System Firmware]]. (Citation: Wikipedia Rootkit) Rootkits have been seen for Windows, Linux, and Mac OS X systems. (Citation: CrowdStrike Linux Rootkit) (Citation: BlackHat Mac OSX Rootkit)

Rootkits that reside or modify boot sectors are known as [[T1542-pre-os_boot#^t1542003-bootkit|T1542.003: Bootkit]]s and specifically target the boot process of the operating system.

## Workspace

- [[workspaces/attack/techniques/T1014-rootkit-note|Open workspace note]]

![[workspaces/attack/techniques/T1014-rootkit-note]]

## Tactics

- [[TA0005-defense_evasion|TA0005: Defense Evasion]]

## D3FEND

- [[D3-AVE-asset_vulnerability_enumeration|D3-AVE: Asset Vulnerability Enumeration]]
- [[D3-CF-content_filtering|D3-CF: Content Filtering]]
- [[D3-CM-content_modification|D3-CM: Content Modification]]
- [[D3-CQ-content_quarantine|D3-CQ: Content Quarantine]]
- [[D3-DF-decoy_file|D3-DF: Decoy File]]
- [[D3-FA-file_analysis|D3-FA: File Analysis]]
- [[D3-FBA-firmware_behavior_analysis|D3-FBA: Firmware Behavior Analysis]]
- [[D3-FE-file_encryption|D3-FE: File Encryption]]
- [[D3-FEMC-firmware_embedded_monitoring_code|D3-FEMC: Firmware Embedded Monitoring Code]]
- [[D3-FEV-file_eviction|D3-FEV: File Eviction]]
- [[D3-FIM-file_integrity_monitoring|D3-FIM: File Integrity Monitoring]]
- [[D3-FV-firmware_verification|D3-FV: Firmware Verification]]
- [[D3-LFP-local_file_permissions|D3-LFP: Local File Permissions]]
- [[D3-RF-restore_file|D3-RF: Restore File]]
- [[D3-RFAM-remote_file_access_mediation|D3-RFAM: Remote File Access Mediation]]
- [[D3-RS-restore_software|D3-RS: Restore Software]]
- [[D3-SU-software_update|D3-SU: Software Update]]
- [[D3-SWI-software_inventory|D3-SWI: Software Inventory]]

## Tools

- [[htran|HTRAN (S0040)]]

## Platforms

- Linux
- macOS
- Windows

