---
sigma_id: "863218bd-c7d0-4c52-80cd-0a96c09f54af"
title: "Arbitrary File Download Via IMEWDBLD.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_imewbdld_download.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_imewbdld_download.yml"
build_date: "2026-04-26 15:01:43"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "863218bd-c7d0-4c52-80cd-0a96c09f54af"
  - "Arbitrary File Download Via IMEWDBLD.EXE"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Arbitrary File Download Via IMEWDBLD.EXE

Detects usage of "IMEWDBLD.exe" to download arbitrary files

## Metadata

- Rule ID: 863218bd-c7d0-4c52-80cd-0a96c09f54af
- Status: test
- Level: high
- Author: Swachchhanda Shrawan Poudel
- Date: 2023-11-09
- Source Path: rules/windows/process_creation/proc_creation_win_imewbdld_download.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection_img:
- Image|endswith: \IMEWDBLD.exe
- OriginalFileName: imewdbld.exe
selection_cli:
  CommandLine|contains:
  - http://
  - https://
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1105/T1105.md#atomic-test-10---windows---powershell-download
- https://lolbas-project.github.io/lolbas/Binaries/IMEWDBLD/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_imewbdld_download.yml)
