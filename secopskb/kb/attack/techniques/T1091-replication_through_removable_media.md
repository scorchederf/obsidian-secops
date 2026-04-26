---
mitre_id: "T1091"
mitre_name: "Replication Through Removable Media"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--3b744087-9945-4a6f-91e8-9dbceda417a4"
mitre_created: "2017-05-31T21:31:08.977Z"
mitre_modified: "2025-10-24T17:48:40.752Z"
mitre_version: "1.3"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1091/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Windows"
mitre_tactic_ids:
  - "TA0008"
  - "TA0001"
d3fend_ids:
  - "D3-HCI"
  - "D3-IOPR"
  - "D3-RH"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[workspaces/index|Notes]]

---

Adversaries may move onto systems, possibly those on disconnected or air-gapped networks, by copying malware to removable media and taking advantage of Autorun features when the media is inserted into a system and executes. In the case of Lateral Movement, this may occur through modification of executable files stored on removable media or by copying malware and renaming it to look like a legitimate file to trick users into executing it on a separate system. In the case of Initial Access, this may occur through manual manipulation of the media, modification of systems used to initially format the media, or modification to the media's firmware itself.

Mobile devices may also be used to infect PCs with malware if connected via USB.(Citation: Exploiting Smartphone USB ) This infection may be achieved using devices (Android, iOS, etc.) and, in some instances, USB charging cables.(Citation: Windows Malware Infecting Android)(Citation: iPhone Charging Cable Hack) For example, when a smartphone is connected to a system, it may appear to be mounted similar to a USB-connected disk drive. If malware that is compatible with the connected system is on the mobile device, the malware could infect the machine (especially if Autorun features are enabled).

## Workspace

- [[workspaces/attack/techniques/T1091-replication_through_removable_media-note|Open workspace note]]

![[workspaces/attack/techniques/T1091-replication_through_removable_media-note]]

## Tactics

- [[TA0008-lateral_movement|TA0008: Lateral Movement]]
- [[TA0001-initial_access|TA0001: Initial Access]]

## D3FEND

- [[D3-HCI-hardware_component_inventory|D3-HCI: Hardware Component Inventory]]
- [[D3-IOPR-io_port_restriction|D3-IOPR: IO Port Restriction]]
- [[D3-RH-radiation_hardening|D3-RH: Radiation Hardening]]

## Mitigations

- [[M1034-limit_hardware_installation|M1034: Limit Hardware Installation]]
- [[M1040-behavior_prevention_on_endpoint|M1040: Behavior Prevention on Endpoint]]
- [[M1042-disable_or_remove_feature_or_program|M1042: Disable or Remove Feature or Program]]

## Platforms

- Windows

