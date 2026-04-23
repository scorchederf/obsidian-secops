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
build_date: "2026-04-23 22:40:56"
build_source: "script"
---

# D3-PFV: Peripheral Firmware Verification

Cryptographically verifying peripheral firmware integrity.

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

## Workspace

- [[kb/notes/d3fend/techniques/d3-pfv-notes|Open workspace note]]

