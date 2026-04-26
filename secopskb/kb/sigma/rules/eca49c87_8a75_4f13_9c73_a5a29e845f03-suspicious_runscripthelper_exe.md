---
sigma_id: "eca49c87-8a75-4f13-9c73-a5a29e845f03"
title: "Suspicious Runscripthelper.exe"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_lolbin_runscripthelper.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_runscripthelper.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "eca49c87-8a75-4f13-9c73-a5a29e845f03"
  - "Suspicious Runscripthelper.exe"
attack_technique_ids:
  - "T1059"
  - "T1202"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Runscripthelper.exe

Detects execution of powershell scripts via Runscripthelper.exe

## Metadata

- Rule ID: eca49c87-8a75-4f13-9c73-a5a29e845f03
- Status: test
- Level: medium
- Author: Victor Sergeev, oscd.community
- Date: 2020-10-09
- Modified: 2022-07-11
- Source Path: rules/windows/process_creation/proc_creation_win_lolbin_runscripthelper.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059]]
- [[kb/attack/techniques/T1202-indirect_command_execution|T1202]]

## Detection

```yaml
selection:
  Image|endswith: \Runscripthelper.exe
  CommandLine|contains: surfacecheck
condition: selection
```

## False Positives

- Unknown

## References

- https://lolbas-project.github.io/lolbas/Binaries/Runscripthelper/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_runscripthelper.yml)
