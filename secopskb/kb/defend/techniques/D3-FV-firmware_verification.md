---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-FV"
d3fend_name: "Firmware Verification"
d3fend_ontology_id: "d3f:FirmwareVerification"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AFirmwareVerification/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-26 13:08:46"
build_source: "script"
attack_technique_ids:
  - "T1014"
  - "T1542"
  - "T1542.001"
  - "T1542.002"
  - "T1542.004"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

---

Cryptographically verifying firmware integrity.

## Workspace

- [[workspaces/defend/techniques/D3-FV-firmware_verification-note|Open workspace note]]

![[workspaces/defend/techniques/D3-FV-firmware_verification-note]]

## Parent Technique

- [[D3-PM-platform_monitoring|D3-PM: Platform Monitoring]]

## Child Techniques

- [[D3-PFV-peripheral_firmware_verification|D3-PFV: Peripheral Firmware Verification]]
- [[D3-SFV-system_firmware_verification|D3-SFV: System Firmware Verification]]

## Related ATT&CK Techniques

- [[T1014-rootkit|T1014: Rootkit]]
- [[T1542-pre-os_boot|T1542: Pre-OS Boot]]
- [[T1542-pre-os_boot#^t1542001-system-firmware|T1542.001: System Firmware]]
- [[T1542-pre-os_boot#^t1542002-component-firmware|T1542.002: Component Firmware]]
- [[T1542-pre-os_boot#^t1542004-rommonkit|T1542.004: ROMMONkit]]

## Knowledge Base Article

## How it works
Cryptographic hash values are computed for system and peripheral firmware. The hash values are compared against precomputed hash values for the identified firmware. A hash value mismatch may indicate that the firmware may have been tampered with or updated with a non-current release indicating a misconfiguration for the system.

## Considerations
* Requires cryptographically computed hash values of firmware
* Requires storage of precomputed firmware hash values

## Ontology Relationships

- [[D3-PM-platform_monitoring|D3-PM: Platform Monitoring]]

