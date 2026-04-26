---
mitre_id: "T1092"
mitre_name: "Communication Through Removable Media"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--64196062-5210-42c3-9a02-563a0d1797ef"
mitre_created: "2017-05-31T21:31:09.379Z"
mitre_modified: "2025-10-24T17:48:52.106Z"
mitre_version: "1.0"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1092/"
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
  - "TA0011"
d3fend_ids:
  - "D3-HCI"
  - "D3-IOPR"
  - "D3-RH"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

Adversaries can perform command and control between compromised hosts on potentially disconnected networks using removable media to transfer commands from system to system.(Citation: ESET Sednit USBStealer 2014) Both systems would need to be compromised, with the likelihood that an Internet-connected system was compromised first and the second through lateral movement by [[T1091-replication_through_removable_media|T1091: Replication Through Removable Media]]. Commands and files would be relayed from the disconnected system to the Internet-connected system to which the adversary has direct access.

## Workspace

- [[workspaces/attack/techniques/T1092-communication_through_removable_media-note|Open workspace note]]

![[workspaces/attack/techniques/T1092-communication_through_removable_media-note]]

## Tactics

- [[TA0011-command_and_control|TA0011: Command and Control]]

## D3FEND

- [[D3-HCI-hardware_component_inventory|D3-HCI: Hardware Component Inventory]]
- [[D3-IOPR-io_port_restriction|D3-IOPR: IO Port Restriction]]
- [[D3-RH-radiation_hardening|D3-RH: Radiation Hardening]]

## Mitigations

- [[M1028-operating_system_configuration|M1028: Operating System Configuration]]
- [[M1042-disable_or_remove_feature_or_program|M1042: Disable or Remove Feature or Program]]

## Platforms

- Linux
- macOS
- Windows

