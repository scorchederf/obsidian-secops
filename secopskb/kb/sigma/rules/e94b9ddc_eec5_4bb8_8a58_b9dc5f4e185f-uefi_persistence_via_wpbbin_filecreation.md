---
sigma_id: "e94b9ddc-eec5-4bb8-8a58-b9dc5f4e185f"
title: "UEFI Persistence Via Wpbbin - FileCreation"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_wpbbin_persistence.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_wpbbin_persistence.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "windows / file_event"
aliases:
  - "e94b9ddc-eec5-4bb8-8a58-b9dc5f4e185f"
  - "UEFI Persistence Via Wpbbin - FileCreation"
attack_technique_ids:
  - "T1542.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# UEFI Persistence Via Wpbbin - FileCreation

Detects creation of a file named "wpbbin" in the "%systemroot%\system32\" directory. Which could be indicative of UEFI based persistence method

## Metadata

- Rule ID: e94b9ddc-eec5-4bb8-8a58-b9dc5f4e185f
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-07-18
- Source Path: rules/windows/file/file_event/file_event_win_wpbbin_persistence.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1542-pre-os_boot|T1542.001]]

## Detection

```yaml
selection:
  TargetFilename: C:\Windows\System32\wpbbin.exe
condition: selection
```

## False Positives

- Legitimate usage of the file by hardware manufacturer such as lenovo (Thanks @0gtweet for the tip)

## References

- https://grzegorztworek.medium.com/using-uefi-to-inject-executable-files-into-bitlocker-protected-drives-8ff4ca59c94c
- https://persistence-info.github.io/Data/wpbbin.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_wpbbin_persistence.yml)
