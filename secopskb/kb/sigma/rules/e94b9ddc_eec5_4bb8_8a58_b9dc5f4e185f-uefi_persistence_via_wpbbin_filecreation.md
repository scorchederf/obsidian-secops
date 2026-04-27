---
sigma_id: "e94b9ddc-eec5-4bb8-8a58-b9dc5f4e185f"
title: "UEFI Persistence Via Wpbbin - FileCreation"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_wpbbin_persistence.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_wpbbin_persistence.yml"
build_date: "2026-04-27 19:13:58"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects creation of a file named "wpbbin" in the "%systemroot%\system32\" directory. Which could be indicative of UEFI based persistence method

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1542-pre-os_boot#^t1542001-system-firmware|T1542.001: System Firmware]]

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
