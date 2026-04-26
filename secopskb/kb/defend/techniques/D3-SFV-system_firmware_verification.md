---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-SFV"
d3fend_name: "System Firmware Verification"
d3fend_ontology_id: "d3f:SystemFirmwareVerification"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3ASystemFirmwareVerification/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-26 13:08:46"
build_source: "script"
attack_technique_ids:
  - "T1542"
  - "T1542.001"
  - "T1542.004"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

Cryptographically verifying installed system firmware integrity.

## Workspace

- [[workspaces/defend/techniques/D3-SFV-system_firmware_verification-note|Open workspace note]]

![[workspaces/defend/techniques/D3-SFV-system_firmware_verification-note]]

## Parent Technique

- [[D3-FV-firmware_verification|D3-FV: Firmware Verification]]

## Related ATT&CK Techniques

- [[T1542-pre-os_boot|T1542: Pre-OS Boot]]
- [[T1542-pre-os_boot#^t1542001-system-firmware|T1542.001: System Firmware]]
- [[T1542-pre-os_boot#^t1542004-rommonkit|T1542.004: ROMMONkit]]

## Knowledge Base Article

## How it works
Cryptographic hash values are computed for system firmware. The hash values are compared against precomputed firmware hash values to determine if the firmware has been tampered with.

When system firmware verification fails a set of predefined responses is typically invoked. The responses may direct the system to disable some devices or operations.

## Considerations
* Requires the use of system provided security modules
* Secure hash values will need to be computed for firmware

## Ontology Relationships

- [[D3-FV-firmware_verification|D3-FV: Firmware Verification]]

