---
sigma_id: "6902955a-01b7-432c-b32a-6f5f81d8f625"
title: "LSASS Process Dump Artefact In CrashDumps Folder"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_lsass_shtinkering.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_lsass_shtinkering.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "high"
logsource: "windows / file_event"
aliases:
  - "6902955a-01b7-432c-b32a-6f5f81d8f625"
  - "LSASS Process Dump Artefact In CrashDumps Folder"
attack_technique_ids:
  - "T1003.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# LSASS Process Dump Artefact In CrashDumps Folder

Detects the presence of an LSASS dump file in the "CrashDumps" folder. This could be a sign of LSASS credential dumping. Techniques such as the LSASS Shtinkering have been seen abusing the Windows Error Reporting to dump said process.

## Metadata

- Rule ID: 6902955a-01b7-432c-b32a-6f5f81d8f625
- Status: test
- Level: high
- Author: @pbssubhash
- Date: 2022-12-08
- Source Path: rules/windows/file/file_event/file_event_win_lsass_shtinkering.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.001]]

## Detection

```yaml
selection:
  TargetFilename|startswith: C:\Windows\System32\config\systemprofile\AppData\Local\CrashDumps\
  TargetFilename|contains: lsass.exe.
  TargetFilename|endswith: .dmp
condition: selection
```

## False Positives

- Rare legitimate dump of the process by the operating system due to a crash of lsass

## References

- https://github.com/deepinstinct/Lsass-Shtinkering
- https://media.defcon.org/DEF%20CON%2030/DEF%20CON%2030%20presentations/Asaf%20Gilboa%20-%20LSASS%20Shtinkering%20Abusing%20Windows%20Error%20Reporting%20to%20Dump%20LSASS.pdf

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_lsass_shtinkering.yml)
