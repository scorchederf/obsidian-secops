---
sigma_id: "9c7e131a-0f2c-4ae0-9d43-b04f4e266d43"
title: "Uncommon Child Process Of Appvlp.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_appvlp_uncommon_child_process.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_appvlp_uncommon_child_process.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "9c7e131a-0f2c-4ae0-9d43-b04f4e266d43"
  - "Uncommon Child Process Of Appvlp.EXE"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Uncommon Child Process Of Appvlp.EXE

Detects uncommon child processes of Appvlp.EXE
Appvlp or the Application Virtualization Utility is included with Microsoft Office. Attackers are able to abuse "AppVLP" to execute shell commands.
Normally, this binary is used for Application Virtualization, but it can also be abused to circumvent the ASR file path rule folder
or to mark a file as a system file.

## Metadata

- Rule ID: 9c7e131a-0f2c-4ae0-9d43-b04f4e266d43
- Status: test
- Level: medium
- Author: Sreeman
- Date: 2020-03-13
- Modified: 2023-11-09
- Source Path: rules/windows/process_creation/proc_creation_win_appvlp_uncommon_child_process.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection:
  ParentImage|endswith: \appvlp.exe
filter_main_generic:
  Image|endswith:
  - :\Windows\SysWOW64\rundll32.exe
  - :\Windows\System32\rundll32.exe
filter_optional_office_msoasb:
  Image|contains: :\Program Files\Microsoft Office
  Image|endswith: \msoasb.exe
filter_optional_office_skype:
  Image|contains|all:
  - :\Program Files\Microsoft Office
  - \SkypeSrv\
  Image|endswith: \SKYPESERVER.EXE
filter_optional_office_msouc:
  Image|contains: :\Program Files\Microsoft Office
  Image|endswith: \MSOUC.EXE
condition: selection and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- Unknown

## References

- https://lolbas-project.github.io/lolbas/OtherMSBinaries/Appvlp/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_appvlp_uncommon_child_process.yml)
