---
sigma_id: "17a1be64-8d88-40bf-b5ff-a4f7a50ebcc8"
title: "Suspicious New Service Creation"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_service_creation.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_service_creation.yml"
build_date: "2026-04-26 15:01:52"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "17a1be64-8d88-40bf-b5ff-a4f7a50ebcc8"
  - "Suspicious New Service Creation"
attack_technique_ids:
  - "T1543.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Suspicious New Service Creation

Detects creation of a new service via "sc" command or the powershell "new-service" cmdlet with suspicious binary paths

## Metadata

- Rule ID: 17a1be64-8d88-40bf-b5ff-a4f7a50ebcc8
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-07-14
- Modified: 2022-11-18
- Source Path: rules/windows/process_creation/proc_creation_win_susp_service_creation.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1543-create_or_modify_system_process|T1543.003]]

## Detection

```yaml
selection_sc:
  Image|endswith: \sc.exe
  CommandLine|contains|all:
  - create
  - binPath=
selection_posh:
  CommandLine|contains|all:
  - New-Service
  - -BinaryPathName
susp_binpath:
  CommandLine|contains:
  - powershell
  - mshta
  - wscript
  - cscript
  - svchost
  - dllhost
  - 'cmd '
  - cmd.exe /c
  - cmd.exe /k
  - cmd.exe /r
  - rundll32
  - C:\Users\Public
  - \Downloads\
  - \Desktop\
  - \Microsoft\Windows\Start Menu\Programs\Startup\
  - C:\Windows\TEMP\
  - \AppData\Local\Temp
condition: 1 of selection* and susp_binpath
```

## False Positives

- Unlikely

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1543.003/T1543.003.md
- https://web.archive.org/web/20180331144337/https://www.fireeye.com/blog/threat-research/2018/03/sanny-malware-delivery-method-updated-in-recently-observed-attacks.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_service_creation.yml)
