---
mitre_id: "DC0079"
mitre_name: "Driver Load"
mitre_type: "x-mitre-data-component"
mitre_stix_id: "x-mitre-data-component--3551476e-14f5-4e48-a518-e82135329e03"
mitre_created: "2021-10-20T15:05:19.274Z"
mitre_modified: "2025-11-12T22:03:39.105Z"
mitre_version: "2.0"
mitre_domains:
  - "enterprise-attack"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "data-component"
tags:
  - "attack"
  - "data-component"
  - "detection"
  - "telemetry"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

The process of attaching a driver, which is a software component that allows the operating system and applications to interact with hardware devices, to either user-mode or kernel-mode of a system. This can include benign actions (e.g., hardware drivers) or malicious behavior (e.g., rootkits or unsigned drivers). Examples: 

- Legitimate Driver Loading: A new graphics driver from a vendor like NVIDIA or AMD is loaded into the system.
- Unsigned Driver Loading: A driver without a valid digital signature is loaded into the kernel.
- Rootkit Installation: A malicious rootkit driver is loaded to manipulate kernel-mode processes.
- Anti-Virus or EDR Driver Loading: An Endpoint Detection and Response (EDR) solution loads its driver to monitor system activities.
- Driver Misuse: A legitimate driver is loaded and exploited to execute malicious actions, such as using vulnerable drivers for bypassing defenses (e.g., Bring Your Own Vulnerable Driver (BYOVD) attacks).

## Workspace

- [[workspaces/attack/data-components/DC0079-driver_load-note|Open workspace note]]

![[workspaces/attack/data-components/DC0079-driver_load-note]]

