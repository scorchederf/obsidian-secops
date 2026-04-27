---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-PFV"
d3fend_name: "Peripheral Firmware Verification"
d3fend_ontology_id: "d3f:PeripheralFirmwareVerification"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3APeripheralFirmwareVerification/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-26 13:08:46"
build_source: "script"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

---

Cryptographically verifying peripheral firmware integrity.

## Workspace

- [[workspaces/defend/techniques/D3-PFV-peripheral_firmware_verification-note|Open workspace note]]

![[workspaces/defend/techniques/D3-PFV-peripheral_firmware_verification-note]]

## Parent Technique

- [[D3-FV-firmware_verification|D3-FV: Firmware Verification]]

## Knowledge Base Article

# How it works
Peripherial firmware is collected and  analyzed on a host either periodically or on demand. This information may be collected for future comparisons.

Changes in firmware hash values may indicate that the firmware has been tampered with or that firmware images are not maintained to current baselined versions, or even known vulnerable versions are deployed.

## Considerations
* Trust baselines will need to be generated for specific devices
* Changes to trusted configurations will need to be managed across the enterprise

## Ontology Relationships

- [[D3-FV-firmware_verification|D3-FV: Firmware Verification]]

