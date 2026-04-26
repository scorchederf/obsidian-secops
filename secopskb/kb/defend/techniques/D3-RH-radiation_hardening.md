---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-RH"
d3fend_name: "Radiation Hardening"
d3fend_ontology_id: "d3f:RadiationHardening"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3ARadiationHardening/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-26 13:08:46"
build_source: "script"
attack_technique_ids:
  - "T1025"
  - "T1052"
  - "T1052.001"
  - "T1056"
  - "T1056.001"
  - "T1091"
  - "T1092"
  - "T1111"
  - "T1123"
  - "T1125"
  - "T1195"
  - "T1195.003"
  - "T1200"
  - "T1619"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

---

Radiation hardening is the process of making electronic components and circuits resistant to damage or malfunction caused by high levels of ionizing radiation.

## Workspace

- [[workspaces/defend/techniques/D3-RH-radiation_hardening-note|Open workspace note]]

![[workspaces/defend/techniques/D3-RH-radiation_hardening-note]]

## Parent Technique

- [[D3-PH-platform_hardening|D3-PH: Platform Hardening]]

## Child Techniques

- [[D3-EMH-electromagnetic_radiation_hardening|D3-EMH: Electromagnetic Radiation Hardening]]

## Related ATT&CK Techniques

- [[T1025-data_from_removable_media|T1025: Data from Removable Media]]
- [[T1052-exfiltration_over_physical_medium|T1052: Exfiltration Over Physical Medium]]
- [[T1052-exfiltration_over_physical_medium#^t1052001-exfiltration-over-usb|T1052.001: Exfiltration over USB]]
- [[T1056-input_capture|T1056: Input Capture]]
- [[T1056-input_capture#^t1056001-keylogging|T1056.001: Keylogging]]
- [[T1091-replication_through_removable_media|T1091: Replication Through Removable Media]]
- [[T1092-communication_through_removable_media|T1092: Communication Through Removable Media]]
- [[T1111-multi-factor_authentication_interception|T1111: Multi-Factor Authentication Interception]]
- [[T1123-audio_capture|T1123: Audio Capture]]
- [[T1125-video_capture|T1125: Video Capture]]
- [[T1195-supply_chain_compromise|T1195: Supply Chain Compromise]]
- [[T1195-supply_chain_compromise#^t1195003-compromise-hardware-supply-chain|T1195.003: Compromise Hardware Supply Chain]]
- [[T1200-hardware_additions|T1200: Hardware Additions]]
- [[T1619-cloud_storage_object_discovery|T1619: Cloud Storage Object Discovery]]

## Knowledge Base Article

## How it works

There are three core radiation hardening methodologies:

1. Radiation Hardening by Process (RHBP): modifying the physical fabrication of a semiconductor (e.g., using SOI - Silicon on Insulator), offering the highest intrinsic protection. Usually the most expensive option as it requires a specialized semiconducter fabrication plant.
2. Radiation Hardening by Design (RHBD): modifying circuit topology and physical layout using techniques such as Triple Modular Redundancy (TMM). A more cost-effective option, with the constraint of potentially increasing chip area and power.
3. Radiation Hardening by Shielding (RHBS): using physical materials (e.g., aluminum or tantalum) to block ionizing particles. Simple to implement, with the constraint of increasing size and weight.

## Ontology Relationships

- [[D3-PH-platform_hardening|D3-PH: Platform Hardening]]

