---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-EMH"
d3fend_name: "Electromagnetic Radiation Hardening"
d3fend_ontology_id: "d3f:ElectromagneticRadiationHardening"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AElectromagneticRadiationHardening/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-26 13:08:46"
build_source: "script"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[workspaces/index|Notes]]

---

The application of physical and material-level design measures to electronic systems, components, or facilities to reduce their susceptibility to damage or disruption from electromagnetic threats.

## Workspace

- [[workspaces/defend/techniques/D3-EMH-electromagnetic_radiation_hardening-note|Open workspace note]]

![[workspaces/defend/techniques/D3-EMH-electromagnetic_radiation_hardening-note]]

## Parent Technique

- [[D3-RH-radiation_hardening|D3-RH: Radiation Hardening]]

## Child Techniques

- [[D3-RFS-rf_shielding|D3-RFS: RF Shielding]]

## Knowledge Base Article

## How it works
EM hardening operates on the principle of controlling the coupling path between an electromagnetic threat and the sensitive electronics it could affect. At the most fundamental level, this involves creating barriers that reflect, absorb, or redirect unwanted electromagnetic energy before it can induce damaging or disruptive currents in protected circuitry. The physical mechanisms exploited include the Faraday cage effect (conductive enclosures that attenuate external fields), skin-depth shielding (where conductive materials dissipate high-frequency fields before they penetrate), and transient suppression components (such as surge protectors and ferrite chokes) that clamp induced voltages at I/O interfaces.

For threats at higher energy levels or involving ionizing radiation, such as nuclear EMP (NEMP) or space radiation, hardening extends beyond shielding to encompass radiation-tolerant component selection, redundant circuit architectures, and layout practices that minimize antenna-like structures susceptible to field coupling. The approach is inherently defense-in-depth: no single measure provides complete protection, so hardened systems typically layer multiple techniques across the facility, chassis, board, and component levels.

## Considerations
* Threat scope must be defined early: design choices differ significantly between defending against ambient RFI, conducted EMI on power lines, intentional jamming, HEMP (High-Altitude EMP), or ionizing radiation in space or nuclear environments.
* Hardening can conflict with thermal management: fully sealed enclosures that maximize shielding often restrict airflow, requiring careful thermal design trade-offs.
* Testing and certification are mandatory for assurance: claimed shielding effectiveness must be validated through standardized testing (e.g., IEEE 299, MIL-STD-461) rather than inferred from design alone.
* Maintenance can degrade hardening: field modifications, connector re-terminations, or enclosure repairs can inadvertently introduce shielding gaps, necessitating re-verification procedures.


## Ontology Relationships

- [[D3-RH-radiation_hardening|D3-RH: Radiation Hardening]]

