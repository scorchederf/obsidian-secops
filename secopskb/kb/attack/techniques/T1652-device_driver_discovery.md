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
build_date: "2026-04-26 13:08:46"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

---

Adversaries may attempt to enumerate local device drivers on a victim host. Information about device drivers may highlight various insights that shape follow-on behaviors, such as the function/purpose of the host, present security tools (i.e. [[T1518-software_discovery#^t1518001-security-software-discovery|T1518.001: Security Software Discovery]]) or other defenses (e.g., [[T1497-virtualization_sandbox_evasion|T1497: Virtualization/Sandbox Evasion]]), as well as potential exploitable vulnerabilities (e.g., [[T1068-exploitation_for_privilege_escalation|T1068: Exploitation for Privilege Escalation]]).

Many OS utilities may provide information about local device drivers, such as `driverquery.exe` and the `EnumDeviceDrivers()` API function on Windows.(Citation: Microsoft Driverquery)(Citation: Microsoft EnumDeviceDrivers) Information about device drivers (as well as associated services, i.e., [[T1007-system_service_discovery|T1007: System Service Discovery]]) may also be available in the Registry.(Citation: Microsoft Registry Drivers)

On Linux/macOS, device drivers (in the form of kernel modules) may be visible within `/dev` or using utilities such as `lsmod` and `modinfo`.(Citation: Linux Kernel Programming)(Citation: lsmod man)(Citation: modinfo man)

## Workspace

- [[workspaces/attack/techniques/T1652-device_driver_discovery-note|Open workspace note]]

![[workspaces/attack/techniques/T1652-device_driver_discovery-note]]

<!-- generated-detection-validation-start -->
## Detection & Validation

### Atomic Tests

- [[kb/atomic/tests/13c0fef5_9be9_4d7f_9c6b_901624e53770-enumerate_kernel_driver_files_linux|Enumerate Kernel Driver Files (Linux) (bash; linux)]]
- [[kb/atomic/tests/235b30a2_e5b1_441f_9705_be6231c88ddd-device_driver_discovery|Device Driver Discovery (powershell; windows)]]
- [[kb/atomic/tests/71eab73d_5d7d_4681_9a72_7873489a5b85-list_loaded_kernel_extensions_macos|List loaded kernel extensions (macOS) (bash; macos)]]
- [[kb/atomic/tests/c63bbe52_6f17_4832_b221_f07ba8b1736f-find_kernel_extensions_macos|Find Kernel Extensions (macOS) (bash; macos)]]
- [[kb/atomic/tests/d57dfc9e_ed9a_418e_88f8_b59c85f8cfd1-device_driver_discovery_linux|Device Driver Discovery (Linux) (bash; linux)]]

<!-- generated-detection-validation-end -->

## Tactics

- [[TA0007-discovery|TA0007: Discovery]]

## Platforms

- Linux
- macOS
- Windows

