---
sigma_id: "52d097e2-063e-4c9c-8fbb-855c8948d135"
title: "Suspicious Windows Update Agent Empty Cmdline"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_wuauclt_no_cli_flags_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wuauclt_no_cli_flags_execution.yml"
build_date: "2026-04-26 15:01:52"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "52d097e2-063e-4c9c-8fbb-855c8948d135"
  - "Suspicious Windows Update Agent Empty Cmdline"
attack_technique_ids:
  - "T1036"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Suspicious Windows Update Agent Empty Cmdline

Detects suspicious Windows Update Agent activity in which a wuauclt.exe process command line doesn't contain any command line flags

## Metadata

- Rule ID: 52d097e2-063e-4c9c-8fbb-855c8948d135
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2022-02-26
- Modified: 2023-11-11
- Source Path: rules/windows/process_creation/proc_creation_win_wuauclt_no_cli_flags_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1036-masquerading|T1036]]

## Detection

```yaml
selection_img:
- Image|endswith: \Wuauclt.exe
- OriginalFileName: Wuauclt.exe
selection_cli:
  CommandLine|endswith:
  - Wuauclt
  - Wuauclt.exe
condition: all of selection*
```

## False Positives

- Unknown

## References

- https://redcanary.com/blog/blackbyte-ransomware/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wuauclt_no_cli_flags_execution.yml)
