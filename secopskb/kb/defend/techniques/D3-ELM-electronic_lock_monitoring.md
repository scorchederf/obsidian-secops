---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-ELM"
d3fend_name: "Electronic Lock Monitoring"
d3fend_ontology_id: "d3f:ElectronicLockMonitoring"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AElectronicLockMonitoring/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-26 13:08:46"
build_source: "script"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

---

Monitoring electronic lock and door hardware states and access events (e.g., locked/unlocked, access granted/denied, door forced/held, tamper) to detect and respond to unauthorized entry.

## Workspace

- [[workspaces/defend/techniques/D3-ELM-electronic_lock_monitoring-note|Open workspace note]]

![[workspaces/defend/techniques/D3-ELM-electronic_lock_monitoring-note]]

## Parent Technique

- [[D3-PHAM-physical_access_monitoring|D3-PHAM: Physical Access Monitoring]]

## Knowledge Base Article

## How it works

Electronic lock monitoring collects status and events from door controllers, readers (badge/PIV, keypad), and door hardware (door position switch, request-to-exit, bolt/latch, tamper). The physical access control system (PACS) logs access decisions, correlates door-held/forced conditions, and generates alarms for response. Secure, supervised reader links, such as Open Supervised Device Protocol (OSDP), help detect wiring faults and reduce credential interception. Integration with video systems can pop relevant camera views on lock-related alarms.

## Considerations

* Use encrypted, supervised reader-to-controller protocols to protect credentials and detect wiring faults.
* Harden door controllers and isolate the PACS network to limit the attack surface.
* Configure fail-safe or fail-secure behavior and emergency release to meet life-safety requirements.
* Tune alarms for door-held, door-forced, and invalid retries to reduce noise while catching misuse.
* Supervise inputs, provide backup power, and regularly test door, bolt, and tamper sensors to ensure reliability.

## Ontology Relationships

- [[D3-PHAM-physical_access_monitoring|D3-PHAM: Physical Access Monitoring]]

