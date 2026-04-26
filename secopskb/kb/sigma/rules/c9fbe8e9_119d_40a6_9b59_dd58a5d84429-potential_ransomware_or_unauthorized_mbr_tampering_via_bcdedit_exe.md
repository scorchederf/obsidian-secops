---
sigma_id: "c9fbe8e9-119d-40a6-9b59-dd58a5d84429"
title: "Potential Ransomware or Unauthorized MBR Tampering Via Bcdedit.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_bcdedit_susp_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_bcdedit_susp_execution.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "c9fbe8e9-119d-40a6-9b59-dd58a5d84429"
  - "Potential Ransomware or Unauthorized MBR Tampering Via Bcdedit.EXE"
attack_technique_ids:
  - "T1070"
  - "T1542.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Ransomware or Unauthorized MBR Tampering Via Bcdedit.EXE

Detects potential malicious and unauthorized usage of bcdedit.exe

## Metadata

- Rule ID: c9fbe8e9-119d-40a6-9b59-dd58a5d84429
- Status: test
- Level: medium
- Author: @neu5ron
- Date: 2019-02-07
- Modified: 2023-02-15
- Source Path: rules/windows/process_creation/proc_creation_win_bcdedit_susp_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1070-indicator_removal|T1070]]
- [[kb/attack/techniques/T1542-pre-os_boot|T1542.003]]

## Detection

```yaml
selection_img:
- Image|endswith: \bcdedit.exe
- OriginalFileName: bcdedit.exe
selection_cli:
  CommandLine|contains:
  - delete
  - deletevalue
  - import
  - safeboot
  - network
condition: all of selection_*
```

## References

- https://learn.microsoft.com/en-us/windows-hardware/drivers/devtest/bcdedit--set
- https://twitter.com/malwrhunterteam/status/1372536434125512712/photo/2

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_bcdedit_susp_execution.yml)
