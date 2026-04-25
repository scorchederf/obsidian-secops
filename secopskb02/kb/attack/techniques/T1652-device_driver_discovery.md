---
mitre_id: "T1652"
mitre_name: "Device Driver Discovery"
mitre_type: "attack-pattern"
mitre_stix_id: "attack-pattern--215d9700-5881-48b8-8265-6449dbb7195d"
mitre_created: "2023-03-28T20:14:49.087Z"
mitre_modified: "2025-04-15T22:17:22.391Z"
mitre_version: "1.0"
mitre_domains:
  - "enterprise-attack"
mitre_url: "https://attack.mitre.org/techniques/T1652/"
framework: "attack"
generated: "true"
build_date: "2026-04-25 20:43:29"
build_source: "script"
object_type: "technique"
mitre_is_subtechnique: "False"
mitre_platforms:
  - "Linux"
  - "macOS"
  - "Windows"
mitre_tactic_ids:
  - "TA0007"
tags:
  - "attack"
  - "technique"
  - "offense"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[workspaces/index|Notes]]

---

Adversaries may attempt to enumerate local device drivers on a victim host. Information about device drivers may highlight various insights that shape follow-on behaviors, such as the function/purpose of the host, present security tools (i.e. [[T1518-software_discovery#^t1518001-security-software-discovery|T1518.001: Security Software Discovery]]) or other defenses (e.g., [[T1497-virtualization_sandbox_evasion|T1497: Virtualization/Sandbox Evasion]]), as well as potential exploitable vulnerabilities (e.g., [[T1068-exploitation_for_privilege_escalation|T1068: Exploitation for Privilege Escalation]]).

Many OS utilities may provide information about local device drivers, such as `driverquery.exe` and the `EnumDeviceDrivers()` API function on Windows.(Citation: Microsoft Driverquery)(Citation: Microsoft EnumDeviceDrivers) Information about device drivers (as well as associated services, i.e., [[T1007-system_service_discovery|T1007: System Service Discovery]]) may also be available in the Registry.(Citation: Microsoft Registry Drivers)

On Linux/macOS, device drivers (in the form of kernel modules) may be visible within `/dev` or using utilities such as `lsmod` and `modinfo`.(Citation: Linux Kernel Programming)(Citation: lsmod man)(Citation: modinfo man)

## Workspace

- [[workspaces/attack/techniques/T1652-device_driver_discovery-note|Open workspace note]]

![[workspaces/attack/techniques/T1652-device_driver_discovery-note]]

## Tactics

- [[TA0007-discovery|TA0007: Discovery]]

## Platforms

- Linux
- macOS
- Windows

