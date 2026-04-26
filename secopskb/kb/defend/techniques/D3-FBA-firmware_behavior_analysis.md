---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-FBA"
d3fend_name: "Firmware Behavior Analysis"
d3fend_ontology_id: "d3f:FirmwareBehaviorAnalysis"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AFirmwareBehaviorAnalysis/"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

Analyzing the behavior of embedded code in firmware and looking for anomalous behavior and suspicious activity.

## Workspace

- [[workspaces/defend/techniques/D3-FBA-firmware_behavior_analysis-note|Open workspace note]]

![[workspaces/defend/techniques/D3-FBA-firmware_behavior_analysis-note]]

## Parent Technique

- [[D3-PM-platform_monitoring|D3-PM: Platform Monitoring]]

## Related ATT&CK Techniques

- [[T1014-rootkit|T1014: Rootkit]]
- [[T1542-pre-os_boot|T1542: Pre-OS Boot]]
- [[T1542-pre-os_boot#^t1542001-system-firmware|T1542.001: System Firmware]]
- [[T1542-pre-os_boot#^t1542002-component-firmware|T1542.002: Component Firmware]]
- [[T1542-pre-os_boot#^t1542004-rommonkit|T1542.004: ROMMONkit]]

## Knowledge Base Article

## How it works
Firmware behavior analysis provides protections by ensuring that installed firmware has not been tampered with or modified. Firmware analysis applies to mutable firmware and immutable read-only memory (ROMs).

Firmware in deployed network devices is typically not analyzed and monitored for vulnerabilities and thus is subject to potential attacks. This technique makes use of known and measured behavioral attributes, including timing attributes, of analyzed firmware on deployed devices.

A behavioral method that employs known timing measurements may use the timing results from a challenge and response protocol to detect the presence of malware in embedded firmware. Firmware device timing measurements are made, specific to the installed device, and are used in the verifying function.

The original firmware image is modified by injecting a monitoring software component into the embedded firmware code. The injected software components will allow for a software root of trust, the challenge and response protocol, to be implement in the firmware.

A challenge-response is issued and includes a nonce so that replays are not allowed. The firmware will calculate a checksum over all of memory, including the nonce, and return the result. The verification system will compare the computed checksum and the time it took for the computation of the checksum to determine if the firmware has been modified.

## Considerations
* The firmware code will need to be modified to include the behavioral monitoring functionality.
* This technique is sensitive to the device the embedded firmware is hosted on and it is expected that the devices and firmware will need to be profiled and analyzed to determine timing estimation.
* This technique is not expected to be one hundred percent correct as you would expect in a hardware root of trust solution and may require some tuning.

## Ontology Relationships

- [[D3-PM-platform_monitoring|D3-PM: Platform Monitoring]]

