---
sigma_id: "2f869d59-7f6a-4931-992c-cce556ff2d53"
title: "Potential Adplus.EXE Abuse"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_adplus_memory_dump.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_adplus_memory_dump.yml"
build_date: "2026-04-26 14:14:31"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "2f869d59-7f6a-4931-992c-cce556ff2d53"
  - "Potential Adplus.EXE Abuse"
attack_technique_ids:
  - "T1003.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Adplus.EXE Abuse

Detects execution of "AdPlus.exe", a binary that is part of the Windows SDK that can be used as a LOLBIN in order to dump process memory and execute arbitrary commands.

## Metadata

- Rule ID: 2f869d59-7f6a-4931-992c-cce556ff2d53
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-06-09
- Modified: 2023-06-23
- Source Path: rules/windows/process_creation/proc_creation_win_adplus_memory_dump.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.001]]

## Detection

```yaml
selection_img:
- Image|endswith: \adplus.exe
- OriginalFileName: Adplus.exe
selection_cli:
  CommandLine|contains:
  - ' -hang '
  - ' -pn '
  - ' -pmn '
  - ' -p '
  - ' -po '
  - ' -c '
  - ' -sc '
condition: all of selection_*
```

## False Positives

- Legitimate usage of Adplus for debugging purposes

## References

- https://lolbas-project.github.io/lolbas/OtherMSBinaries/Adplus/
- https://twitter.com/nas_bench/status/1534916659676422152
- https://twitter.com/nas_bench/status/1534915321856917506

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_adplus_memory_dump.yml)
