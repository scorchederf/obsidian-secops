---
sigma_id: "c048f047-7e2a-4888-b302-55f509d4a91d"
title: "SCR File Write Event"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_new_scr_file.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_new_scr_file.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "medium"
logsource: "windows / file_event"
aliases:
  - "c048f047-7e2a-4888-b302-55f509d4a91d"
  - "SCR File Write Event"
attack_technique_ids:
  - "T1218.011"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# SCR File Write Event

Detects the creation of screensaver files (.scr) outside of system folders. Attackers may execute an application as an ".SCR" file using "rundll32.exe desk.cpl,InstallScreenSaver" for example.

## Metadata

- Rule ID: c048f047-7e2a-4888-b302-55f509d4a91d
- Status: test
- Level: medium
- Author: Christopher Peacock @securepeacock, SCYTHE @scythe_io
- Date: 2022-04-27
- Modified: 2023-08-23
- Source Path: rules/windows/file/file_event/file_event_win_new_scr_file.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.011]]

## Detection

```yaml
selection:
  TargetFilename|endswith: .scr
filter:
  TargetFilename|contains:
  - :\$WINDOWS.~BT\NewOS\
  - :\Windows\System32\
  - :\Windows\SysWOW64\
  - :\Windows\WinSxS\
  - :\WUDownloadCache\
condition: selection and not filter
```

## False Positives

- The installation of new screen savers by third party software

## References

- https://lolbas-project.github.io/lolbas/Libraries/Desk/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_new_scr_file.yml)
