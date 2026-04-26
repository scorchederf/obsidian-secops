---
sigma_id: "b27077d6-23e6-45d2-81a0-e2b356eea5fd"
title: "Use of TTDInject.exe"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_lolbin_ttdinject.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_ttdinject.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "b27077d6-23e6-45d2-81a0-e2b356eea5fd"
  - "Use of TTDInject.exe"
attack_technique_ids:
  - "T1127"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Use of TTDInject.exe

Detects the executiob of TTDInject.exe, which is used by Windows 10 v1809 and newer to debug time travel (underlying call of tttracer.exe)

## Metadata

- Rule ID: b27077d6-23e6-45d2-81a0-e2b356eea5fd
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-05-16
- Source Path: rules/windows/process_creation/proc_creation_win_lolbin_ttdinject.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1127-trusted_developer_utilities_proxy_execution|T1127]]

## Detection

```yaml
selection:
- Image|endswith: ttdinject.exe
- OriginalFileName: TTDInject.EXE
condition: selection
```

## False Positives

- Legitimate use

## References

- https://lolbas-project.github.io/lolbas/Binaries/Ttdinject/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_ttdinject.yml)
