---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-MBT"
d3fend_name: "Memory Boundary Tracking"
d3fend_ontology_id: "d3f:MemoryBoundaryTracking"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3AMemoryBoundaryTracking/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-25 14:47:22"
build_source: "script"
attack_technique_ids:
  - "T1055"
  - "T1055.012"
  - "T1056"
  - "T1056.004"
  - "T1068"
  - "T1203"
  - "T1210"
  - "T1211"
  - "T1212"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[notes/index|Notes]]

---

Analyzing a call stack for return addresses which point to unexpected  memory locations.

## Workspace

- [[notes/defend/techniques/D3-MBT-memory_boundary_tracking-note|Open workspace note]]

![[notes/defend/techniques/D3-MBT-memory_boundary_tracking-note]]

## Parent Technique

- [[D3-OSM-operating_system_monitoring|D3-OSM: Operating System Monitoring]]

## Related ATT&CK Techniques

- [[T1055-process_injection|T1055: Process Injection]]
- [[T1055-process_injection#^t1055012-process-hollowing|T1055.012: Process Hollowing]]
- [[T1056-input_capture|T1056: Input Capture]]
- [[T1056-input_capture#^t1056004-credential-api-hooking|T1056.004: Credential API Hooking]]
- [[T1068-exploitation_for_privilege_escalation|T1068: Exploitation for Privilege Escalation]]
- [[T1203-exploitation_for_client_execution|T1203: Exploitation for Client Execution]]
- [[T1210-exploitation_of_remote_services|T1210: Exploitation of Remote Services]]
- [[T1211-exploitation_for_defense_evasion|T1211: Exploitation for Defense Evasion]]
- [[T1212-exploitation_for_credential_access|T1212: Exploitation for Credential Access]]

## Knowledge Base Article

## How it works
This technique monitors for indicators of whether a return address is outside memory previously allocated for an object (i.e. function, module, process, or thread). If so, code that the return address points to is treated as malicious code.

## Considerations
Kernel malware can manipulate memory contents, for example modifying pointers to hide processes, and thereby impact the accuracy of memory allocation information used to perform the analysis.

## Ontology Relationships

- [[D3-OSM-operating_system_monitoring|D3-OSM: Operating System Monitoring]]

