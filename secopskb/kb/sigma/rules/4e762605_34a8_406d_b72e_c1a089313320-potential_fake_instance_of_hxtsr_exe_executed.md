---
sigma_id: "4e762605-34a8-406d-b72e-c1a089313320"
title: "Potential Fake Instance Of Hxtsr.EXE Executed"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hxtsr_masquerading.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hxtsr_masquerading.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "4e762605-34a8-406d-b72e-c1a089313320"
  - "Potential Fake Instance Of Hxtsr.EXE Executed"
attack_technique_ids:
  - "T1036"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Fake Instance Of Hxtsr.EXE Executed

HxTsr.exe is a Microsoft compressed executable file called Microsoft Outlook Communications.
HxTsr.exe is part of Outlook apps, because it resides in a hidden "WindowsApps" subfolder of "C:\Program Files".
Any instances of hxtsr.exe not in this folder may be malware camouflaging itself as HxTsr.exe

## Metadata

- Rule ID: 4e762605-34a8-406d-b72e-c1a089313320
- Status: test
- Level: medium
- Author: Sreeman
- Date: 2020-04-17
- Modified: 2024-02-08
- Source Path: rules/windows/process_creation/proc_creation_win_hxtsr_masquerading.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1036-masquerading|T1036]]

## Detection

```yaml
selection:
  Image|endswith: \hxtsr.exe
filter_main_hxtsr:
  Image|contains: :\program files\windowsapps\microsoft.windowscommunicationsapps_
  Image|endswith: \hxtsr.exe
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- Internal Research

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hxtsr_masquerading.yml)
