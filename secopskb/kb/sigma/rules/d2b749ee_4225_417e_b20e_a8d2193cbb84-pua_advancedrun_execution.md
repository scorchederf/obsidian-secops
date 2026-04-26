---
sigma_id: "d2b749ee-4225-417e-b20e-a8d2193cbb84"
title: "PUA - AdvancedRun Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_pua_advancedrun.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pua_advancedrun.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "d2b749ee-4225-417e-b20e-a8d2193cbb84"
  - "PUA - AdvancedRun Execution"
attack_technique_ids:
  - "T1564.003"
  - "T1134.002"
  - "T1059.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# PUA - AdvancedRun Execution

Detects the execution of AdvancedRun utility

## Metadata

- Rule ID: d2b749ee-4225-417e-b20e-a8d2193cbb84
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems)
- Date: 2022-01-20
- Modified: 2023-02-21
- Source Path: rules/windows/process_creation/proc_creation_win_pua_advancedrun.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1564-hide_artifacts|T1564.003]]
- [[kb/attack/techniques/T1134-access_token_manipulation|T1134.002]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.003]]

## Detection

```yaml
selection:
- OriginalFileName: AdvancedRun.exe
- CommandLine|contains|all:
  - ' /EXEFilename '
  - ' /Run'
- CommandLine|contains|all:
  - ' /WindowState 0'
  - ' /RunAs '
  - ' /CommandLine '
condition: selection
```

## False Positives

- Unknown

## References

- https://twitter.com/splinter_code/status/1483815103279603714
- https://medium.com/s2wblog/analysis-of-destructive-malware-whispergate-targeting-ukraine-9d5d158f19f3
- https://www.elastic.co/security-labs/operation-bleeding-bear
- https://www.winhelponline.com/blog/run-program-as-system-localsystem-account-windows/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pua_advancedrun.yml)
