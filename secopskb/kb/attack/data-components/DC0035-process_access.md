---
mitre_id: "DC0035"
mitre_name: "Process Access"
mitre_type: "x-mitre-data-component"
mitre_stix_id: "x-mitre-data-component--1887a270-576a-4049-84de-ef746b2572d6"
mitre_created: "2021-10-20T15:05:19.272Z"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

---

Refers to an event where one process attempts to open another process, typically to inspect or manipulate its memory, access handles, or modify execution flow. Monitoring these access attempts can provide valuable insight into both benign and malicious behaviors, such as debugging, inter-process communication (IPC), or process injection.

*Data Collection Measures:*

- Endpoint Detection and Response (EDR) Tools:
    -  EDR solutions that provide telemetry on inter-process access and memory manipulation.
- Sysmon (Windows):
    - Event ID 10: Captures process access attempts, including:
        - Source process (initiator)
        - Target process (victim)
        - Access rights requested
        - Process ID correlation
- Windows Event Logs:
    - Event ID 4656 (Audit Handle to an Object): Logs access attempts to system objects.
    - Event ID 4690 (Attempted Process Modification): Can help identify unauthorized process changes.
- Linux/macOS Monitoring:
    - AuditD: Monitors process access through syscall tracing (e.g., `ptrace`, `open`, `read`, `write`).
    - eBPF/XDP: Used for low-level monitoring of kernel process access.
    - OSQuery: Query process access behavior via structured SQL-like logging.
- Procmon (Process Monitor) and Debugging Tools:
    - Windows Procmon: Captures real-time process interactions.
    - Linux strace / ptrace: Useful for tracking process behavior at the system call level.

## Workspace

- [[workspaces/attack/data-components/DC0035-process_access-note|Open workspace note]]

![[workspaces/attack/data-components/DC0035-process_access-note]]

