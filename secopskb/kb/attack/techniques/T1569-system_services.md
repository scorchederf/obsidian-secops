---
mitre_id: "T1569"
mitre_name: "System Services"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--d157f9d2-d09a-4efa-bb2a-64963f94e253"
mitre_created: "2020-03-10T18:23:06.482Z"
mitre_modified: "2025-10-24T17:49:25.548Z"
mitre_version: "1.4"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1569/"
framework: "attack"
generated: "true"
build_date: "2026-04-26 13:08:46"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Windows"
  - "macOS"
  - "Linux"
mitre_tactic_ids:
  - "TA0002"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[workspaces/index|Notes]]

---

Adversaries may abuse system services or daemons to execute commands or programs. Adversaries can execute malicious content by interacting with or creating services either locally or remotely. Many services are set to run at boot, which can aid in achieving persistence ([[T1543-create_or_modify_system_process|T1543: Create or Modify System Process]]), but adversaries can also abuse services for one-time or temporary execution.

## Workspace

- [[workspaces/attack/techniques/T1569-system_services-note|Open workspace note]]

![[workspaces/attack/techniques/T1569-system_services-note]]

## Tactics

- [[TA0002-execution|TA0002: Execution]]

## Subtechniques

### T1569.001: Launchctl

^t1569001-launchctl

Adversaries may abuse launchctl to execute commands or programs. Launchctl interfaces with launchd, the service management framework for macOS. Launchctl supports taking subcommands on the command-line, interactively, or even redirected from standard input.(Citation: Launchctl Man)

Adversaries use launchctl to execute commands and programs as [[T1543-create_or_modify_system_process#^t1543001-launch-agent|T1543.001: Launch Agent]]s or [[T1543-create_or_modify_system_process#^t1543004-launch-daemon|T1543.004: Launch Daemon]]s. Common subcommands include: `launchctl load`,`launchctl unload`, and `launchctl start`. Adversaries can use scripts or manually run the commands `launchctl load -w "%s/Library/LaunchAgents/%s"` or `/bin/launchctl load` to execute [[T1543-create_or_modify_system_process#^t1543001-launch-agent|T1543.001: Launch Agent]]s or [[T1543-create_or_modify_system_process#^t1543004-launch-daemon|T1543.004: Launch Daemon]]s.(Citation: Sofacy Komplex Trojan)(Citation: 20 macOS Common Tools and Techniques)


### T1569.002: Service Execution

^t1569002-service-execution

Adversaries may abuse the Windows service control manager to execute malicious commands or payloads. The Windows service control manager (`services.exe`) is an interface to manage and manipulate services.(Citation: Microsoft Service Control Manager) The service control manager is accessible to users via GUI components as well as system utilities such as `sc.exe` and [[net|Net (S0039)]].

[[psexec|PsExec (S0029)]] can also be used to execute commands or payloads via a temporary Windows service created through the service control manager API.(Citation: Russinovich Sysinternals) Tools such as [[psexec|PsExec (S0029)]] and `sc.exe` can accept remote servers as arguments and may be used to conduct remote execution.

Adversaries may leverage these mechanisms to execute malicious content. This can be done by either executing a new or modified service. This technique is the execution used in conjunction with [[T1543-create_or_modify_system_process#^t1543003-windows-service|T1543.003: Windows Service]] during service persistence or privilege escalation.

### T1569.003: Systemctl

^t1569003-systemctl

Adversaries may abuse systemctl to execute commands or programs. Systemctl is the primary interface for systemd, the Linux init system and service manager. Typically invoked from a shell, Systemctl can also be integrated into scripts or applications.   

Adversaries may use systemctl to execute commands or programs as [[T1543-create_or_modify_system_process#^t1543002-systemd-service|T1543.002: Systemd Service]]s. Common subcommands include: `systemctl start`, `systemctl stop`, `systemctl enable`, `systemctl disable`, and `systemctl status`.(Citation: Red Hat Systemctl 2022)

## Mitigations

- [[M1018-user_account_management|M1018: User Account Management]]
- [[M1022-restrict_file_and_directory_permissions|M1022: Restrict File and Directory Permissions]]
- [[M1026-privileged_account_management|M1026: Privileged Account Management]]
- [[M1040-behavior_prevention_on_endpoint|M1040: Behavior Prevention on Endpoint]]

## Platforms

- Windows
- macOS
- Linux

