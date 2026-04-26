---
sigma_id: "4f84b697-c9ed-4420-8ab5-e09af5b2345d"
title: "New DLL Added to AppInit_DLLs Registry Key"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_event/registry_event_new_dll_added_to_appinit_dlls_registry_key.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_event/registry_event_new_dll_added_to_appinit_dlls_registry_key.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "medium"
logsource: "windows / registry_event"
aliases:
  - "4f84b697-c9ed-4420-8ab5-e09af5b2345d"
  - "New DLL Added to AppInit_DLLs Registry Key"
attack_technique_ids:
  - "T1546.010"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# New DLL Added to AppInit_DLLs Registry Key

DLLs that are specified in the AppInit_DLLs value in the Registry key HKLM\Software\Microsoft\Windows NT\CurrentVersion\Windows are loaded by user32.dll into every process that loads user32.dll

## Metadata

- Rule ID: 4f84b697-c9ed-4420-8ab5-e09af5b2345d
- Status: test
- Level: medium
- Author: Ilyas Ochkov, oscd.community, Tim Shelton
- Date: 2019-10-25
- Modified: 2022-12-25
- Source Path: rules/windows/registry/registry_event/registry_event_new_dll_added_to_appinit_dlls_registry_key.yml

## Logsource

- category: registry_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1546-event_triggered_execution|T1546.010]]

## Detection

```yaml
selection:
- TargetObject|endswith:
  - \SOFTWARE\Microsoft\Windows NT\CurrentVersion\Windows\AppInit_Dlls
  - \SOFTWARE\Wow6432Node\Microsoft\Windows NT\CurrentVersion\Windows\AppInit_Dlls
- NewName|endswith:
  - \SOFTWARE\Microsoft\Windows NT\CurrentVersion\Windows\AppInit_Dlls
  - \SOFTWARE\Wow6432Node\Microsoft\Windows NT\CurrentVersion\Windows\AppInit_Dlls
filter:
  Details: (Empty)
condition: selection and not filter
```

## False Positives

- Unknown

## References

- https://eqllib.readthedocs.io/en/latest/analytics/822dc4c5-b355-4df8-bd37-29c458997b8f.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_event/registry_event_new_dll_added_to_appinit_dlls_registry_key.yml)
