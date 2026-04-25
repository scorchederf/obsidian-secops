---
mitre_id: "DC0060"
mitre_name: "Service Creation"
mitre_type: "x-mitre-data-component"
mitre_stix_id: "x-mitre-data-component--5297a638-1382-4f0c-8472-0d21830bf705"
mitre_created: "2021-10-20T15:05:19.273Z"
mitre_modified: "2025-11-12T22:03:39.105Z"
mitre_version: "2.0"
mitre_domains:
  - "ics-attack"
  - "enterprise-attack"
framework: "attack"
generated: "true"
build_date: "2026-04-25 20:43:29"
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

The registration of a new service or daemon on an operating system.

*Data Collection Measures:*

- Windows Event Logs
    - Event ID 4697 - Captures the creation of a new Windows service.
    - Event ID 7045 - Captures services installed by administrators or adversaries.
    - Event ID 7034 - Could indicate malicious service modification or exploitation.
- Sysmon Logs
    - Sysmon Event ID 1 - Process Creation (captures service executables).
    - Sysmon Event ID 4 - Service state changes (detects service installation).
    - Sysmon Event ID 13 - Registry modifications (captures service persistence changes).
- PowerShell Logging
    - Monitor `New-Service` and `Set-Service` PowerShell cmdlets in Event ID 4104 (Script Block Logging).
- Linux/macOS Collection Methods
    - AuditD & Syslog Daemon Logs (`/var/log/syslog`, `/var/log/messages`, `/var/log/daemon.log`)
    - AuditD Rules:
        - `auditctl -w /etc/systemd/system -p wa -k service_creation`
        - Detects changes to `systemd` service configurations.
- Systemd Journals (`journalctl -u <service_name>`)
    - Captures newly created systemd services.
- LaunchDaemons & LaunchAgents (macOS)
    - Monitor `/Library/LaunchDaemons/` and `/Library/LaunchAgents/` for new plist files.

## Workspace

- [[workspaces/attack/data-components/DC0060-service_creation-note|Open workspace note]]

![[workspaces/attack/data-components/DC0060-service_creation-note]]

