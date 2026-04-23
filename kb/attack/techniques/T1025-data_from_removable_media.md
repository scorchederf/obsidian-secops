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
build_date: "2026-04-23 22:40:56"
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

# T1025: Data from Removable Media

Adversaries may search connected removable media on computers they have compromised to find files of interest. Sensitive data can be collected from any removable media (optical disk drive, USB memory, etc.) connected to the compromised system prior to Exfiltration. Interactive command shells may be in use, and common functionality within [[cmd|cmd]] may be used to gather information. 

Some adversaries may also use [[T1119-automated_collection|T1119: Automated Collection]] on removable media.

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

## Workspace

- [[kb/notes/attack/techniques/t1025-notes|Open workspace note]]

