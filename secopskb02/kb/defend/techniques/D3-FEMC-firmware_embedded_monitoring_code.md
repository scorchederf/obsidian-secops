---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-FEMC"
d3fend_name: "Firmware Embedded Monitoring Code"
d3fend_ontology_id: "d3f:FirmwareEmbeddedMonitoringCode"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AFirmwareEmbeddedMonitoringCode/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-25 20:43:29"
build_source: "script"
attack_technique_ids:
  - "T1014"
  - "T1542"
  - "T1542.001"
  - "T1542.002"
  - "T1542.004"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

Monitoring code is injected into firmware for integrity monitoring of firmware and firmware data.

## Workspace

- [[workspaces/defend/techniques/D3-FEMC-firmware_embedded_monitoring_code-note|Open workspace note]]

![[workspaces/defend/techniques/D3-FEMC-firmware_embedded_monitoring_code-note]]

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
Firmware in deployed network devices is typically not monitored for malicious changes. This technique provides a method to embed a software security component into the deployed firmware which provides a near real-time monitoring hook. The exception handling code, in the firmware, is typically used to expose any detected vulnerabilities.

The injected software components provide a feature similar to intrusion detection systems for the firmware by detecting unauthorized modifications of the embedded firmware. The integrity of static code and firmware data are monitored continuously in the hosted devices. Comparisons are made to monitored elements like firmware memory addresses and data segments. Memory pages are scanned and if a modification is detected the software component may lock the page. This will protect subsequent attempted modifications to the firmware. The software component may utilize the exception handling code and thus be able to disclose the exact address of the modified memory.

The injected software components are inserted during the firmware imaging process. The injected software is assumed to have knowledge of both the embedded code and the current execution state of the host program. The injected software will monitor and alert, in near real-time, on potential suspicious activity. The injected code is run alongside of the embedded code in the host. The injected software operates as an independent entity and is not dependent on the host software.

Finally, this technique may implement other countermeasure techniques as part of their analytical processes. These should be identified by referencing other countermeasure techniques directly as necessary.

## Considerations
* The firmware code will need to be modified and re-hosted on the device.
* Exposing monitoring hooks to the injected code may introduce additional risk.

## Ontology Relationships

- [[D3-PM-platform_monitoring|D3-PM: Platform Monitoring]]

