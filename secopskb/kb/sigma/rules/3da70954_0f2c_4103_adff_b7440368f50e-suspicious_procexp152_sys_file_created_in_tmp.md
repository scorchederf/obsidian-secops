---
sigma_id: "3da70954-0f2c-4103-adff-b7440368f50e"
title: "Suspicious PROCEXP152.sys File Created In TMP"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_susp_procexplorer_driver_created_in_tmp_folder.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_susp_procexplorer_driver_created_in_tmp_folder.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "medium"
logsource: "windows / file_event"
aliases:
  - "3da70954-0f2c-4103-adff-b7440368f50e"
  - "Suspicious PROCEXP152.sys File Created In TMP"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious PROCEXP152.sys File Created In TMP

Detects the creation of the PROCEXP152.sys file in the application-data local temporary folder.
This driver is used by Sysinternals Process Explorer but also by KDU (https://github.com/hfiref0x/KDU) or Ghost-In-The-Logs (https://github.com/bats3c/Ghost-In-The-Logs), which uses KDU.

## Metadata

- Rule ID: 3da70954-0f2c-4103-adff-b7440368f50e
- Status: test
- Level: medium
- Author: xknow (@xknow_infosec), xorxes (@xor_xes)
- Date: 2019-04-08
- Modified: 2022-11-22
- Source Path: rules/windows/file/file_event/file_event_win_susp_procexplorer_driver_created_in_tmp_folder.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Detection

```yaml
selection:
  TargetFilename|contains: \AppData\Local\Temp\
  TargetFilename|endswith: PROCEXP152.sys
filter:
  Image|contains:
  - \procexp64.exe
  - \procexp.exe
  - \procmon64.exe
  - \procmon.exe
condition: selection and not filter
```

## False Positives

- Other legimate tools using this driver and filename (like Sysinternals). Note - Clever attackers may easily bypass this detection by just renaming the driver filename. Therefore just Medium-level and don't rely on it.

## References

- https://web.archive.org/web/20230331181619/https://blog.dylan.codes/evading-sysmon-and-windows-event-logging/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_susp_procexplorer_driver_created_in_tmp_folder.yml)
