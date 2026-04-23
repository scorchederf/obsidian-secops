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
build_date: "2026-04-23 20:16:46"
build_source: "script"
---

# DC0064: Command Execution

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

