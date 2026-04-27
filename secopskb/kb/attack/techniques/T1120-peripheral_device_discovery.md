---
mitre_id: "T1120"
mitre_name: "Peripheral Device Discovery"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--348f1eef-964b-4eb6-bb53-69b3dcb0c643"
mitre_created: "2017-05-31T21:31:28.471Z"
mitre_modified: "2025-10-24T17:48:37.563Z"
mitre_version: "1.4"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1120/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Linux"
  - "Windows"
  - "macOS"
mitre_tactic_ids:
  - "TA0007"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

---

Adversaries may attempt to gather information about attached peripheral devices and components connected to a computer system.(Citation: Peripheral Discovery Linux)(Citation: Peripheral Discovery macOS) Peripheral devices could include auxiliary resources that support a variety of functionalities such as keyboards, printers, cameras, smart card readers, or removable storage. The information may be used to enhance their awareness of the system and network environment or may be used for further actions.

## Workspace

- [[workspaces/attack/techniques/T1120-peripheral_device_discovery-note|Open workspace note]]

![[workspaces/attack/techniques/T1120-peripheral_device_discovery-note]]

<!-- generated-detection-validation-start -->
## Detection & Validation

### Atomic Tests

- [[kb/atomic/tests/2cb4dbf2_2dca_4597_8678_4d39d207a3a5-win32_pnpentity_hardware_inventory|Win32_PnPEntity Hardware Inventory (powershell; windows)]]
- [[kb/atomic/tests/424e18fd_48b8_4201_8d3a_bf591523a686-peripheral_device_discovery_via_fsutil|Peripheral Device Discovery via fsutil (command_prompt; windows)]]
- [[kb/atomic/tests/5c876daf_db1e_41cf_988d_139a7443ccd4-get_printer_device_list_via_powershell_command|Get Printer Device List via PowerShell Command (powershell; windows)]]
- [[kb/atomic/tests/cb6e76ca_861e_4a7f_be08_564caa3e6f75-winpwn_printercheck|WinPwn - printercheck (powershell; windows)]]

<!-- generated-detection-validation-end -->

## Tactics

- [[TA0007-discovery|TA0007: Discovery]]

## Platforms

- Linux
- Windows
- macOS

