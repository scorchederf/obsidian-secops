---
sigma_id: "2aa0a6b4-a865-495b-ab51-c28249537b75"
title: "Startup Folder File Write"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_startup_folder_file_write.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_startup_folder_file_write.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "medium"
logsource: "windows / file_event"
aliases:
  - "2aa0a6b4-a865-495b-ab51-c28249537b75"
  - "Startup Folder File Write"
attack_technique_ids:
  - "T1547.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Startup Folder File Write

A General detection for files being created in the Windows startup directory. This could be an indicator of persistence.

## Metadata

- Rule ID: 2aa0a6b4-a865-495b-ab51-c28249537b75
- Status: test
- Level: medium
- Author: Roberto Rodriguez (Cyb3rWard0g), OTR (Open Threat Research)
- Date: 2020-05-02
- Modified: 2025-12-03
- Source Path: rules/windows/file/file_event/file_event_win_startup_folder_file_write.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547.001]]

## Detection

```yaml
selection:
  TargetFilename|contains: \Microsoft\Windows\Start Menu\Programs\StartUp
filter_main_update:
- Image:
  - C:\Windows\System32\wuauclt.exe
  - C:\Windows\uus\ARM64\wuaucltcore.exe
- TargetFilename|startswith:
  - C:\$WINDOWS.~BT\NewOS\
  - C:\$WinREAgent\Scratch\Mount\
filter_optional_onenote:
  Image|endswith: \ONENOTE.EXE
  TargetFilename|endswith: \Send to OneNote.lnk
condition: selection and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- FP could be caused by legitimate application writing shortcuts for example. This folder should always be inspected to make sure that all the files in there are legitimate

## References

- https://github.com/OTRF/detection-hackathon-apt29/issues/12
- https://github.com/OTRF/ThreatHunter-Playbook/blob/2d4257f630f4c9770f78d0c1df059f891ffc3fec/docs/evals/apt29/detections/5.B.1_611FCA99-97D0-4873-9E51-1C1BA2DBB40D.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_startup_folder_file_write.yml)
