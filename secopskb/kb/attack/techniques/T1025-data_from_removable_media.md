---
mitre_id: "T1025"
mitre_name: "Data from Removable Media"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--1b7ba276-eedc-4951-a762-0ceea2c030ec"
mitre_created: "2017-05-31T21:30:31.584Z"
mitre_modified: "2025-10-24T17:48:28.431Z"
mitre_version: "1.3"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1025/"
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
  - "D3-HCI"
  - "D3-IOPR"
  - "D3-RH"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

---

Adversaries may search connected removable media on computers they have compromised to find files of interest. Sensitive data can be collected from any removable media (optical disk drive, USB memory, etc.) connected to the compromised system prior to Exfiltration. Interactive command shells may be in use, and common functionality within [[cmd|cmd (S0106)]] may be used to gather information. 

Some adversaries may also use [[T1119-automated_collection|T1119: Automated Collection]] on removable media.

## Workspace

- [[workspaces/attack/techniques/T1025-data_from_removable_media-note|Open workspace note]]

![[workspaces/attack/techniques/T1025-data_from_removable_media-note]]

<!-- generated-detection-validation-start -->
## Detection & Validation

### Atomic Tests

- [[kb/atomic/tests/0b29f7e3_a050_44b7_bf05_9fb86af1ec2e-identify_documents_on_usb_and_removable_media_via_powershell|Identify Documents on USB and Removable Media via PowerShell (command_prompt; windows)]]

<!-- generated-detection-validation-end -->

## Tactics

- [[TA0009-collection|TA0009: Collection]]

## D3FEND

- [[D3-HCI-hardware_component_inventory|D3-HCI: Hardware Component Inventory]]
- [[D3-IOPR-io_port_restriction|D3-IOPR: IO Port Restriction]]
- [[D3-RH-radiation_hardening|D3-RH: Radiation Hardening]]

## Mitigations

- [[M1057-data_loss_prevention|M1057: Data Loss Prevention]]

## Platforms

- Linux
- macOS
- Windows

