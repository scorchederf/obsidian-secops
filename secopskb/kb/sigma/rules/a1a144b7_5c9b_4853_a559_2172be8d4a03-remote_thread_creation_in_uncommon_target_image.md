---
sigma_id: "a1a144b7-5c9b-4853-a559-2172be8d4a03"
title: "Remote Thread Creation In Uncommon Target Image"
framework: "sigma"
generated: "true"
source_path: "rules/windows/create_remote_thread/create_remote_thread_win_susp_uncommon_target_image.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/create_remote_thread/create_remote_thread_win_susp_uncommon_target_image.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "medium"
logsource: "windows / create_remote_thread"
aliases:
  - "a1a144b7-5c9b-4853-a559-2172be8d4a03"
  - "Remote Thread Creation In Uncommon Target Image"
attack_technique_ids:
  - "T1055.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Remote Thread Creation In Uncommon Target Image

Detects uncommon target processes for remote thread creation

## Metadata

- Rule ID: a1a144b7-5c9b-4853-a559-2172be8d4a03
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems)
- Date: 2022-03-16
- Modified: 2025-07-04
- Source Path: rules/windows/create_remote_thread/create_remote_thread_win_susp_uncommon_target_image.yml

## Logsource

- category: create_remote_thread
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1055-process_injection|T1055.003]]

## Detection

```yaml
selection:
  TargetImage|endswith:
  - \calc.exe
  - \calculator.exe
  - \mspaint.exe
  - \notepad.exe
  - \ping.exe
  - \sethc.exe
  - \spoolsv.exe
  - \wordpad.exe
  - \write.exe
filter_main_csrss:
  SourceImage: C:\Windows\System32\csrss.exe
filter_main_notepad:
  SourceImage:
  - C:\Windows\System32\explorer.exe
  - C:\Windows\System32\OpenWith.exe
  TargetImage: C:\Windows\System32\notepad.exe
filter_main_sethc:
  SourceImage: C:\Windows\System32\AtBroker.exe
  TargetImage: C:\Windows\System32\Sethc.exe
filter_optional_aurora_1:
  StartFunction: EtwpNotificationThread
filter_optional_aurora_2:
  SourceImage|contains: unknown process
filter_optional_vmtoolsd:
  SourceImage: C:\Program Files\VMware\VMware Tools\vmtoolsd.exe
  StartFunction: GetCommandLineW
  TargetImage:
  - C:\Windows\System32\notepad.exe
  - C:\Windows\System32\spoolsv.exe
filter_optional_xerox_pjems:
  SourceImage: C:\Program Files\Xerox\XeroxPrintExperience\CommonFiles\XeroxPrintJobEventManagerService.exe
  StartFunction: LoadLibraryW
  TargetImage: C:\Windows\System32\spoolsv.exe
condition: selection and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- Unknown

## References

- https://web.archive.org/web/20220319032520/https://blog.redbluepurple.io/offensive-research/bypassing-injection-detection

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/create_remote_thread/create_remote_thread_win_susp_uncommon_target_image.yml)
