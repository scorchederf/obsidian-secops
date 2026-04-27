---
sigma_id: "0b80ade5-6997-4b1d-99a1-71701778ea61"
title: "Imports Registry Key From an ADS"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_regedit_import_keys_ads.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_regedit_import_keys_ads.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "0b80ade5-6997-4b1d-99a1-71701778ea61"
  - "Imports Registry Key From an ADS"
attack_technique_ids:
  - "T1112"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Imports Registry Key From an ADS

Detects the import of a alternate datastream to the registry with regedit.exe.

## Metadata

- Rule ID: 0b80ade5-6997-4b1d-99a1-71701778ea61
- Status: test
- Level: high
- Author: Oddvar Moe, Sander Wiebing, oscd.community
- Date: 2020-10-12
- Modified: 2024-03-13
- Source Path: rules/windows/process_creation/proc_creation_win_regedit_import_keys_ads.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1112-modify_registry|T1112]]

## Detection

```yaml
selection_img:
- Image|endswith: \regedit.exe
- OriginalFileName: REGEDIT.EXE
selection_cli:
  CommandLine|contains:
  - ' /i '
  - .reg
  CommandLine|re: :[^ \\]
filter:
  CommandLine|contains|windash:
  - ' -e '
  - ' -a '
  - ' -c '
condition: all of selection_* and not filter
```

## False Positives

- Unknown

## References

- https://lolbas-project.github.io/lolbas/Binaries/Regedit/
- https://gist.github.com/api0cradle/cdd2d0d0ec9abb686f0e89306e277b8f

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_regedit_import_keys_ads.yml)
