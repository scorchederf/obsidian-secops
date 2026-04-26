---
sigma_id: "90d50722-0483-4065-8e35-57efaadd354d"
title: "Arbitrary MSI Download Via Devinit.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_devinit_lolbin_usage.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_devinit_lolbin_usage.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "90d50722-0483-4065-8e35-57efaadd354d"
  - "Arbitrary MSI Download Via Devinit.EXE"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Arbitrary MSI Download Via Devinit.EXE

Detects a certain command line flag combination used by "devinit.exe", which can be abused as a LOLBIN to download arbitrary MSI packages on a Windows system

## Metadata

- Rule ID: 90d50722-0483-4065-8e35-57efaadd354d
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems)
- Date: 2022-01-11
- Modified: 2023-04-06
- Source Path: rules/windows/process_creation/proc_creation_win_devinit_lolbin_usage.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection:
  CommandLine|contains|all:
  - ' -t msi-install '
  - ' -i http'
condition: selection
```

## False Positives

- Unknown

## References

- https://twitter.com/mrd0x/status/1460815932402679809
- https://lolbas-project.github.io/lolbas/OtherMSBinaries/Devinit/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_devinit_lolbin_usage.yml)
