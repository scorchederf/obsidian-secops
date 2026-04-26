---
sigma_id: "ec0722a3-eb5c-4a56-8ab2-bf6f20708592"
title: "Renamed Gpg.EXE Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_renamed_gpg4win.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_renamed_gpg4win.yml"
build_date: "2026-04-26 17:03:22"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "ec0722a3-eb5c-4a56-8ab2-bf6f20708592"
  - "Renamed Gpg.EXE Execution"
attack_technique_ids:
  - "T1486"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Renamed Gpg.EXE Execution

Detects the execution of a renamed "gpg.exe". Often used by ransomware and loaders to decrypt/encrypt data.

## Metadata

- Rule ID: ec0722a3-eb5c-4a56-8ab2-bf6f20708592
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems), frack113
- Date: 2023-08-09
- Source Path: rules/windows/process_creation/proc_creation_win_renamed_gpg4win.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1486-data_encrypted_for_impact|T1486]]

## Detection

```yaml
selection:
  OriginalFileName: gpg.exe
filter_main_img:
  Image|endswith:
  - \gpg.exe
  - \gpg2.exe
condition: selection and not 1 of filter_main_*
```

## References

- https://securelist.com/locked-out/68960/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_renamed_gpg4win.yml)
