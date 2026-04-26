---
sigma_id: "11b1ed55-154d-4e82-8ad7-83739298f720"
title: "NTDS.DIT Creation By Uncommon Process"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_ntds_dit_uncommon_process.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_ntds_dit_uncommon_process.yml"
build_date: "2026-04-26 17:03:20"
status: "test"
level: "high"
logsource: "windows / file_event"
aliases:
  - "11b1ed55-154d-4e82-8ad7-83739298f720"
  - "NTDS.DIT Creation By Uncommon Process"
attack_technique_ids:
  - "T1003.002"
  - "T1003.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# NTDS.DIT Creation By Uncommon Process

Detects creation of a file named "ntds.dit" (Active Directory Database) by an uncommon process or a process located in a suspicious directory

## Metadata

- Rule ID: 11b1ed55-154d-4e82-8ad7-83739298f720
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems), Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-01-11
- Modified: 2022-07-14
- Source Path: rules/windows/file/file_event/file_event_win_ntds_dit_uncommon_process.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.002]]
- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.003]]

## Detection

```yaml
selection_ntds:
  TargetFilename|endswith: \ntds.dit
selection_process_img:
  Image|endswith:
  - \cmd.exe
  - \cscript.exe
  - \mshta.exe
  - \powershell.exe
  - \pwsh.exe
  - \regsvr32.exe
  - \rundll32.exe
  - \wscript.exe
  - \wsl.exe
  - \wt.exe
selection_process_paths:
  Image|contains:
  - \AppData\
  - \Temp\
  - \Public\
  - \PerfLogs\
condition: selection_ntds and 1 of selection_process_*
```

## False Positives

- Unknown

## References

- https://stealthbits.com/blog/extracting-password-hashes-from-the-ntds-dit-file/
- https://adsecurity.org/?p=2398

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_ntds_dit_uncommon_process.yml)
