---
sigma_id: "883faa95-175a-4e22-8181-e5761aeb373c"
title: "Suspicious Service Binary Directory"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_service_dir.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_service_dir.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "883faa95-175a-4e22-8181-e5761aeb373c"
  - "Suspicious Service Binary Directory"
attack_technique_ids:
  - "T1202"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Suspicious Service Binary Directory

Detects a service binary running in a suspicious directory

## Metadata

- Rule ID: 883faa95-175a-4e22-8181-e5761aeb373c
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2021-03-09
- Modified: 2022-10-09
- Source Path: rules/windows/process_creation/proc_creation_win_susp_service_dir.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1202-indirect_command_execution|T1202]]

## Detection

```yaml
selection:
  Image|contains:
  - \Users\Public\
  - \$Recycle.bin
  - \Users\All Users\
  - \Users\Default\
  - \Users\Contacts\
  - \Users\Searches\
  - C:\Perflogs\
  - \config\systemprofile\
  - \Windows\Fonts\
  - \Windows\IME\
  - \Windows\addins\
  ParentImage|endswith:
  - \services.exe
  - \svchost.exe
condition: selection
```

## False Positives

- Unknown

## References

- https://blog.truesec.com/2021/03/07/exchange-zero-day-proxylogon-and-hafnium/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_service_dir.yml)
