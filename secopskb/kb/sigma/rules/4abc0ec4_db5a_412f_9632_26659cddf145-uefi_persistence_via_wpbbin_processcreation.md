---
sigma_id: "4abc0ec4-db5a-412f-9632-26659cddf145"
title: "UEFI Persistence Via Wpbbin - ProcessCreation"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_wpbbin_potential_persistence.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wpbbin_potential_persistence.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "4abc0ec4-db5a-412f-9632-26659cddf145"
  - "UEFI Persistence Via Wpbbin - ProcessCreation"
attack_technique_ids:
  - "T1542.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# UEFI Persistence Via Wpbbin - ProcessCreation

Detects execution of the binary "wpbbin" which is used as part of the UEFI based persistence method described in the reference section

## Metadata

- Rule ID: 4abc0ec4-db5a-412f-9632-26659cddf145
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-07-18
- Source Path: rules/windows/process_creation/proc_creation_win_wpbbin_potential_persistence.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1542-pre-os_boot|T1542.001]]

## Detection

```yaml
selection:
  Image: C:\Windows\System32\wpbbin.exe
condition: selection
```

## False Positives

- Legitimate usage of the file by hardware manufacturer such as lenovo (Thanks @0gtweet for the tip)

## References

- https://grzegorztworek.medium.com/using-uefi-to-inject-executable-files-into-bitlocker-protected-drives-8ff4ca59c94c
- https://persistence-info.github.io/Data/wpbbin.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wpbbin_potential_persistence.yml)
