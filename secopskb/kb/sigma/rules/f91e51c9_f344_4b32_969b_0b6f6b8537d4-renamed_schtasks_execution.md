---
sigma_id: "f91e51c9-f344-4b32-969b-0b6f6b8537d4"
title: "Renamed Schtasks Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_renamed_schtasks_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_renamed_schtasks_execution.yml"
build_date: "2026-04-27 19:13:55"
status: "experimental"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "f91e51c9-f344-4b32-969b-0b6f6b8537d4"
  - "Renamed Schtasks Execution"
attack_technique_ids:
  - "T1036.003"
  - "T1053.005"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the execution of renamed schtasks.exe binary, which is a legitimate Windows utility used for scheduling tasks.
One of the very common persistence techniques is schedule malicious tasks using schtasks.exe.
Since, it is heavily abused, it is also heavily monitored by security products. To evade detection, threat actors may rename the schtasks.exe binary to schedule their malicious tasks.

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1036-masquerading#^t1036003-rename-legitimate-utilities|T1036.003: Rename Legitimate Utilities]]
- [[kb/attack/techniques/T1053-scheduled_task_job#^t1053005-scheduled-task|T1053.005: Scheduled Task]]

## Detection

```yaml
selection_cmd_operation:
  CommandLine|contains|windash:
  - ' /create '
  - ' /delete '
  - ' /query '
  - ' /change '
  - ' /run '
  - ' /end '
selection_cmd_flags:
  CommandLine|contains|windash:
  - ' /tn '
  - ' /tr '
  - ' /sc '
  - ' /st '
  - ' /ru '
  - ' /fo '
selection_pe:
  OriginalFileName: schtasks.exe
filter_main_cmd:
  CommandLine|contains: schtasks
filter_main_img:
  Image|endswith: \schtasks.exe
condition: (all of selection_cmd_* and not filter_main_cmd) or (selection_pe and not
  filter_main_img)
```

## False Positives

- Unlikely

## References

- https://x.com/JangPr0/status/1932034543026065833
- https://ss64.com/nt/schtasks.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_renamed_schtasks_execution.yml)
