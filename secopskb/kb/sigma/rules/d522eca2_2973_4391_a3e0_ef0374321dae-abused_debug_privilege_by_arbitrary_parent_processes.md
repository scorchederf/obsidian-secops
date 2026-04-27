---
sigma_id: "d522eca2-2973-4391-a3e0-ef0374321dae"
title: "Abused Debug Privilege by Arbitrary Parent Processes"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_abusing_debug_privilege.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_abusing_debug_privilege.yml"
build_date: "2026-04-27 19:13:50"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "d522eca2-2973-4391-a3e0-ef0374321dae"
  - "Abused Debug Privilege by Arbitrary Parent Processes"
attack_technique_ids:
  - "T1548"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detection of unusual child processes by different system processes

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548: Abuse Elevation Control Mechanism]]

## Detection

```yaml
selection_parent:
  ParentImage|endswith:
  - \winlogon.exe
  - \services.exe
  - \lsass.exe
  - \csrss.exe
  - \smss.exe
  - \wininit.exe
  - \spoolsv.exe
  - \searchindexer.exe
  User|contains:
  - AUTHORI
  - AUTORI
selection_img:
- Image|endswith:
  - \powershell.exe
  - \pwsh.exe
  - \cmd.exe
- OriginalFileName:
  - PowerShell.EXE
  - pwsh.dll
  - Cmd.Exe
filter:
  CommandLine|contains|all:
  - ' route '
  - ' ADD '
condition: all of selection_* and not filter
```

## False Positives

- Unknown

## References

- https://image.slidesharecdn.com/kheirkhabarovoffzonefinal-181117201458/95/hunting-for-privilege-escalation-in-windows-environment-74-638.jpg

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_abusing_debug_privilege.yml)
