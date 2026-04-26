---
mitre_id: "DC0064"
mitre_name: "Command Execution"
mitre_type: "x-mitre-data-component"
mitre_stix_id: "x-mitre-data-component--685f917a-e95e-4ba0-ade1-c7d354dae6e0"
mitre_created: "2021-10-20T15:05:19.273Z"
mitre_modified: "2025-11-12T22:03:39.105Z"
mitre_version: "2.0"
mitre_domains:
  - "ics-attack"
  - "mobile-attack"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[workspaces/index|Notes]]

---

Command Execution involves monitoring and capturing the execution of textual commands (including shell commands, cmdlets, and scripts) within an operating system or application. These commands may include arguments or parameters and are typically executed through interpreters such as `cmd.exe`, `bash`, `zsh`, `PowerShell`, or programmatic execution. Examples: 

- Windows Command Prompt
    - dir – Lists directory contents.
    - net user – Queries or manipulates user accounts.
    - tasklist – Lists running processes.
- PowerShell
    - Get-Process – Retrieves processes running on a system.
    - Set-ExecutionPolicy – Changes PowerShell script execution policies.
    - Invoke-WebRequest – Downloads remote resources.
- Linux Shell
    - ls – Lists files in a directory.
    - cat /etc/passwd – Reads the user accounts file.
    - curl http://malicious-site.com – Retrieves content from a malicious URL.
- Container Environments
    - docker exec – Executes a command inside a running container.
    - kubectl exec – Runs commands in Kubernetes pods.
- macOS Terminal
    - open – Opens files or URLs.
    - dscl . -list /Users – Lists all users on the system.
    - osascript -e – Executes AppleScript commands.

## Workspace

- [[workspaces/attack/data-components/DC0064-command_execution-note|Open workspace note]]

![[workspaces/attack/data-components/DC0064-command_execution-note]]

