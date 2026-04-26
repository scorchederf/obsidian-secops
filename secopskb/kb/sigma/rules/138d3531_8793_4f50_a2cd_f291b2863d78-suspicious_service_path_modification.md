---
sigma_id: "138d3531-8793-4f50-a2cd-f291b2863d78"
title: "Suspicious Service Path Modification"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_sc_service_path_modification.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sc_service_path_modification.yml"
build_date: "2026-04-26 15:01:52"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "138d3531-8793-4f50-a2cd-f291b2863d78"
  - "Suspicious Service Path Modification"
attack_technique_ids:
  - "T1543.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Suspicious Service Path Modification

Detects service path modification via the "sc" binary to a suspicious command or path

## Metadata

- Rule ID: 138d3531-8793-4f50-a2cd-f291b2863d78
- Status: test
- Level: high
- Author: Victor Sergeev, oscd.community, Nasreddine Bencherchali (Nextron Systems)
- Date: 2019-10-21
- Modified: 2022-11-18
- Source Path: rules/windows/process_creation/proc_creation_win_sc_service_path_modification.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1543-create_or_modify_system_process|T1543.003]]

## Detection

```yaml
selection:
  Image|endswith: \sc.exe
  CommandLine|contains|all:
  - config
  - binPath
  CommandLine|contains:
  - powershell
  - 'cmd '
  - mshta
  - wscript
  - cscript
  - rundll32
  - svchost
  - dllhost
  - cmd.exe /c
  - cmd.exe /k
  - cmd.exe /r
  - cmd /c
  - cmd /k
  - cmd /r
  - C:\Users\Public
  - \Downloads\
  - \Desktop\
  - \Microsoft\Windows\Start Menu\Programs\Startup\
  - C:\Windows\TEMP\
  - \AppData\Local\Temp
condition: selection
```

## False Positives

- Unlikely

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1543.003/T1543.003.md
- https://web.archive.org/web/20180331144337/https://www.fireeye.com/blog/threat-research/2018/03/sanny-malware-delivery-method-updated-in-recently-observed-attacks.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sc_service_path_modification.yml)
