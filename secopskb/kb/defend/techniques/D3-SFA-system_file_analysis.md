---
framework: "d3fend"
object_type: "defensive-technique"
generated: "true"
d3fend_id: "D3-SFA"
d3fend_name: "System File Analysis"
d3fend_ontology_id: "d3f:SystemFileAnalysis"
d3fend_url: "https://d3fend.mitre.org/technique/d3f%3ASystemFileAnalysis/"
tags:
  - "d3fend"
  - "defensive-technique"
  - "defense"
  - "countermeasure"
build_date: "2026-04-26 13:08:46"
build_source: "script"
attack_technique_ids:
  - "T1003"
  - "T1003.007"
  - "T1018"
  - "T1036"
  - "T1036.003"
  - "T1055"
  - "T1055.009"
  - "T1070"
  - "T1070.002"
  - "T1543"
  - "T1543.002"
  - "T1548"
  - "T1548.003"
  - "T1556"
  - "T1556.003"
  - "T1574"
  - "T1574.006"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[workspaces/index|Notes]]

---

Monitoring system files such as authentication databases, configuration files, system logs, and system executables for modification or tampering.

## Workspace

- [[workspaces/defend/techniques/D3-SFA-system_file_analysis-note|Open workspace note]]

![[workspaces/defend/techniques/D3-SFA-system_file_analysis-note]]

## Parent Technique

- [[D3-OSM-operating_system_monitoring|D3-OSM: Operating System Monitoring]]

## Child Techniques

- [[D3-SBV-service_binary_verification|D3-SBV: Service Binary Verification]]

## Related ATT&CK Techniques

- [[T1003-os_credential_dumping|T1003: OS Credential Dumping]]
- [[T1003-os_credential_dumping#^t1003007-proc-filesystem|T1003.007: Proc Filesystem]]
- [[T1018-remote_system_discovery|T1018: Remote System Discovery]]
- [[T1036-masquerading|T1036: Masquerading]]
- [[T1036-masquerading#^t1036003-rename-legitimate-utilities|T1036.003: Rename Legitimate Utilities]]
- [[T1055-process_injection|T1055: Process Injection]]
- [[T1055-process_injection#^t1055009-proc-memory|T1055.009: Proc Memory]]
- [[T1070-indicator_removal|T1070: Indicator Removal]]
- [[T1070-indicator_removal#^t1070002-clear-linux-or-mac-system-logs|T1070.002: Clear Linux or Mac System Logs]]
- [[T1543-create_or_modify_system_process|T1543: Create or Modify System Process]]
- [[T1543-create_or_modify_system_process#^t1543002-systemd-service|T1543.002: Systemd Service]]
- [[T1548-abuse_elevation_control_mechanism|T1548: Abuse Elevation Control Mechanism]]
- [[T1548-abuse_elevation_control_mechanism#^t1548003-sudo-and-sudo-caching|T1548.003: Sudo and Sudo Caching]]
- [[T1556-modify_authentication_process|T1556: Modify Authentication Process]]
- [[T1556-modify_authentication_process#^t1556003-pluggable-authentication-modules|T1556.003: Pluggable Authentication Modules]]
- [[T1574-hijack_execution_flow|T1574: Hijack Execution Flow]]
- [[T1574-hijack_execution_flow#^t1574006-dynamic-linker-hijacking|T1574.006: Dynamic Linker Hijacking]]

## Knowledge Base Article

## How it works
This technique ensures the integrity of system owned file resources. System files can impact the behavior below the user level.


## Considerations
* Need to manage the size of log file analysis.
* False positives are a concern with this technique and filtering will need to be given additional thought.
* A baseline or snapshot of file checksums should be established for future comparison.

## Ontology Relationships

- [[D3-OSM-operating_system_monitoring|D3-OSM: Operating System Monitoring]]

