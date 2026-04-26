---
sigma_id: "b2309017-4235-44fe-b5af-b15363011957"
title: "Uncommon Child Process Of Defaultpack.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_defaultpack_uncommon_child_process.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_defaultpack_uncommon_child_process.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "b2309017-4235-44fe-b5af-b15363011957"
  - "Uncommon Child Process Of Defaultpack.EXE"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Uncommon Child Process Of Defaultpack.EXE

Detects uncommon child processes of "DefaultPack.EXE" binary as a proxy to launch other programs

## Metadata

- Rule ID: b2309017-4235-44fe-b5af-b15363011957
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-12-31
- Modified: 2024-04-22
- Source Path: rules/windows/process_creation/proc_creation_win_defaultpack_uncommon_child_process.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection:
  ParentImage|endswith: \DefaultPack.exe
condition: selection
```

## False Positives

- Unknown

## References

- https://lolbas-project.github.io/lolbas/OtherMSBinaries/DefaultPack/
- https://www.echotrail.io/insights/search/defaultpack.exe

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_defaultpack_uncommon_child_process.yml)
