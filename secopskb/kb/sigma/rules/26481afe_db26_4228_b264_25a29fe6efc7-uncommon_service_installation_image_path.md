---
sigma_id: "26481afe-db26-4228-b264-25a29fe6efc7"
title: "Uncommon Service Installation Image Path"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/system/service_control_manager/win_system_service_install_uncommon.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/service_control_manager/win_system_service_install_uncommon.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "windows / system"
aliases:
  - "26481afe-db26-4228-b264-25a29fe6efc7"
  - "Uncommon Service Installation Image Path"
attack_technique_ids:
  - "T1543.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Uncommon Service Installation Image Path

Detects uncommon service installation commands by looking at suspicious or uncommon image path values containing references to encoded powershell commands, temporary paths, etc.

## Metadata

- Rule ID: 26481afe-db26-4228-b264-25a29fe6efc7
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems)
- Date: 2022-03-18
- Modified: 2024-02-09
- Source Path: rules/windows/builtin/system/service_control_manager/win_system_service_install_uncommon.yml

## Logsource

- product: windows
- service: system

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1543-create_or_modify_system_process|T1543.003]]

## Detection

```yaml
selection:
  Provider_Name: Service Control Manager
  EventID: 7045
suspicious_paths:
  ImagePath|contains:
  - \\\\.\\pipe
  - \Users\Public\
  - \Windows\Temp\
suspicious_encoded_flag:
  ImagePath|contains: ' -e'
suspicious_encoded_keywords:
  ImagePath|contains:
  - ' aQBlAHgA'
  - ' aWV4I'
  - ' IAB'
  - ' JAB'
  - ' PAA'
  - ' SQBFAFgA'
  - ' SUVYI'
filter_optional_thor_remote:
  ImagePath|startswith: C:\WINDOWS\TEMP\thor10-remote\thor64.exe
filter_main_defender_def_updates:
  ImagePath|startswith: C:\ProgramData\Microsoft\Windows Defender\Definition Updates\
condition: selection and ( suspicious_paths or all of suspicious_encoded_* ) and not
  1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- Unknown

## References

- Internal Research

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/service_control_manager/win_system_service_install_uncommon.yml)
