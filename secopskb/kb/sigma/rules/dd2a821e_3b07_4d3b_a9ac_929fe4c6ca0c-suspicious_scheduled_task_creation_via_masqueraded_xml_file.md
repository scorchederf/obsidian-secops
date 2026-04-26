---
sigma_id: "dd2a821e-3b07-4d3b-a9ac-929fe4c6ca0c"
title: "Suspicious Scheduled Task Creation via Masqueraded XML File"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_schtasks_schedule_via_masqueraded_xml_file.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_schtasks_schedule_via_masqueraded_xml_file.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "dd2a821e-3b07-4d3b-a9ac-929fe4c6ca0c"
  - "Suspicious Scheduled Task Creation via Masqueraded XML File"
attack_technique_ids:
  - "T1036.005"
  - "T1053.005"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Scheduled Task Creation via Masqueraded XML File

Detects the creation of a scheduled task using the "-XML" flag with a file without the '.xml' extension. This behavior could be indicative of potential defense evasion attempt during persistence

## Metadata

- Rule ID: dd2a821e-3b07-4d3b-a9ac-929fe4c6ca0c
- Status: test
- Level: medium
- Author: Swachchhanda Shrawan Poudel, Elastic (idea)
- Date: 2023-04-20
- Modified: 2024-12-01
- Source Path: rules/windows/process_creation/proc_creation_win_schtasks_schedule_via_masqueraded_xml_file.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1036-masquerading|T1036.005]]
- [[kb/attack/techniques/T1053-scheduled_task_job|T1053.005]]

## Detection

```yaml
selection_img:
- Image|endswith: \schtasks.exe
- OriginalFileName: schtasks.exe
selection_cli_create:
  CommandLine|contains:
  - /create
  - -create
selection_cli_xml:
  CommandLine|contains:
  - /xml
  - -xml
filter_main_extension_xml:
  CommandLine|contains: .xml
filter_main_system_process:
  IntegrityLevel:
  - System
  - S-1-16-16384
filter_main_rundll32:
  ParentImage|endswith: \rundll32.exe
  ParentCommandLine|contains|all:
  - :\WINDOWS\Installer\MSI
  - .tmp,zzzzInvokeManagedCustomActionOutOfProc
filter_optional_third_party:
  ParentImage|endswith:
  - :\ProgramData\OEM\UpgradeTool\CareCenter_*\BUnzip\Setup_msi.exe
  - :\Program Files\Axis Communications\AXIS Camera Station\SetupActions.exe
  - :\Program Files\Axis Communications\AXIS Device Manager\AdmSetupActions.exe
  - :\Program Files (x86)\Zemana\AntiMalware\AntiMalware.exe
  - :\Program Files\Dell\SupportAssist\pcdrcui.exe
condition: all of selection_* and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- Unknown

## References

- https://learn.microsoft.com/en-us/windows/win32/taskschd/daily-trigger-example--xml-
- https://github.com/elastic/protections-artifacts/blob/084067123d3328a823b1c3fdde305b694275c794/behavior/rules/persistence_suspicious_scheduled_task_creation_via_masqueraded_xml_file.toml

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_schtasks_schedule_via_masqueraded_xml_file.yml)
