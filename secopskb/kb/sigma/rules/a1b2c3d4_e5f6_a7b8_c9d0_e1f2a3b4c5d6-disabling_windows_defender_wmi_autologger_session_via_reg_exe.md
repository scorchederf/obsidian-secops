---
sigma_id: "a1b2c3d4-e5f6-a7b8-c9d0-e1f2a3b4c5d6"
title: "Disabling Windows Defender WMI Autologger Session via Reg.exe"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_reg_disable_defender_wmi_autologger.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_reg_disable_defender_wmi_autologger.yml"
build_date: "2026-04-26 15:01:44"
status: "experimental"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "a1b2c3d4-e5f6-a7b8-c9d0-e1f2a3b4c5d6"
  - "Disabling Windows Defender WMI Autologger Session via Reg.exe"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Disabling Windows Defender WMI Autologger Session via Reg.exe

Detects the use of reg.exe to disable the Event Tracing for Windows (ETW) Autologger session for Windows Defender API and Audit events.
By setting the 'Start' value to '0' for the 'DefenderApiLogger' or 'DefenderAuditLogger' session, an attacker can prevent these critical security events
from being logged, effectively blinding monitoring tools that rely on this data. This is a powerful defense evasion technique.

## Metadata

- Rule ID: a1b2c3d4-e5f6-a7b8-c9d0-e1f2a3b4c5d6
- Status: experimental
- Level: high
- Author: Matt Anderson (Huntress)
- Date: 2025-07-09
- Source Path: rules/windows/process_creation/proc_creation_win_reg_disable_defender_wmi_autologger.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Detection

```yaml
selection_img:
- Image|endswith: \reg.exe
- OriginalFileName: reg.exe
selection_reg_path:
  CommandLine|contains:
  - \Control\WMI\Autologger\DefenderApiLogger\Start
  - \Control\WMI\Autologger\DefenderAuditLogger\Start
selection_reg_add:
  CommandLine|contains|all:
  - add
  - '0'
filter_main_enable:
  CommandLine|contains: '0x00000001'
condition: all of selection_* and not 1 of filter_main_*
```

## False Positives

- Highly unlikely

## References

- https://research.splunk.com/endpoint/76406a0f-f5e0-4167-8e1f-337fdc0f1b0c/
- https://docs.microsoft.com/en-us/windows/win32/etw/configuring-and-starting-an-autologger-session
- https://thedfirreport.com/2021/10/18/icedid-to-xinglocker-ransomware-in-24-hours/
- https://blog.malwarebytes.com/malwarebytes-news/2021/02/lazyscripter-from-empire-to-double-rat/
- https://www.binarly.io/blog/design-issues-of-modern-edrs-bypassing-etw-based-solutions

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_reg_disable_defender_wmi_autologger.yml)
