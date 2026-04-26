---
sigma_id: "77df53a5-1d78-4f32-bc5a-0e7465bd8f41"
title: "Portable Gpg.EXE Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_gpg4win_portable_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_gpg4win_portable_execution.yml"
build_date: "2026-04-26 14:14:31"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "77df53a5-1d78-4f32-bc5a-0e7465bd8f41"
  - "Portable Gpg.EXE Execution"
attack_technique_ids:
  - "T1486"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Portable Gpg.EXE Execution

Detects the execution of "gpg.exe" from uncommon location. Often used by ransomware and loaders to decrypt/encrypt data.

## Metadata

- Rule ID: 77df53a5-1d78-4f32-bc5a-0e7465bd8f41
- Status: test
- Level: medium
- Author: frack113, Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-08-06
- Modified: 2023-11-10
- Source Path: rules/windows/process_creation/proc_creation_win_gpg4win_portable_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1486-data_encrypted_for_impact|T1486]]

## Detection

```yaml
selection:
- Image|endswith:
  - \gpg.exe
  - \gpg2.exe
- OriginalFileName: gpg.exe
- Description: GnuPG’s OpenPGP tool
filter_main_legit_location:
  Image|contains:
  - :\Program Files (x86)\GNU\GnuPG\bin\
  - :\Program Files (x86)\GnuPG VS-Desktop\
  - :\Program Files (x86)\GnuPG\bin\
  - :\Program Files (x86)\Gpg4win\bin\
condition: selection and not 1 of filter_main_*
```

## References

- https://www.trendmicro.com/vinfo/vn/threat-encyclopedia/malware/ransom.bat.zarlock.a
- https://securelist.com/locked-out/68960/
- https://github.com/redcanaryco/atomic-red-team/blob/c4097dc7ed14d7f7d08c89d148c4307097e8c294/atomics/T1486/T1486.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_gpg4win_portable_execution.yml)
