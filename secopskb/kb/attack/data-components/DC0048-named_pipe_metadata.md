---
mitre_id: "DC0048"
mitre_name: "Named Pipe Metadata"
mitre_type: "x-mitre-data-component"
mitre_stix_id: "x-mitre-data-component--b9a1578e-8653-4103-be23-cb52e0b1816e"
mitre_created: "2021-10-20T15:05:19.273Z"
mitre_modified: "2025-10-21T15:14:39.039Z"
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

Contextual data about a named pipe on a system, including pipe name and creating process (ex: Sysmon EIDs 17-18)

*Data Collection Measures:*

- Windows:
    - Sysmon Event ID 17: Logs the creation of a named pipe.
    - Sysmon Event ID 18: Logs connection attempts to a named pipe.
    - Windows Security Event ID 5145: Logs access attempts to named pipes via SMB shares.
    - ETW (Event Tracing for Windows): Provides deep telemetry into named pipe interactions.
- Linux/macOS:
    - AuditD (`mkfifo`, `open`, `read`, `write` syscalls): Tracks FIFO (named pipe) creation and usage.
    - Lsof (`lsof -p <PID>` or `lsof | grep PIPE`): Lists active named pipes and associated processes.
    - Strace (`strace -e open <process>`): Monitors named pipe interactions.
- Endpoint Detection & Response (EDR):
    - Capture named pipe events as part of process tracking.
- Memory Forensics:
    - Volatility Plugin (`pipescan`): Enumerates named pipes in system memory.
    - Rekall Framework: Identifies active named pipes and associated processes.

## Workspace

- [[workspaces/attack/data-components/DC0048-named_pipe_metadata-note|Open workspace note]]

![[workspaces/attack/data-components/DC0048-named_pipe_metadata-note]]

