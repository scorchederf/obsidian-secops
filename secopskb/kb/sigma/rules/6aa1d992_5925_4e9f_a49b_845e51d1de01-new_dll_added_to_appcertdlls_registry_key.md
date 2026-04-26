---
sigma_id: "6aa1d992-5925-4e9f-a49b-845e51d1de01"
title: "New DLL Added to AppCertDlls Registry Key"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_event/registry_event_new_dll_added_to_appcertdlls_registry_key.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_event/registry_event_new_dll_added_to_appcertdlls_registry_key.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "medium"
logsource: "windows / registry_event"
aliases:
  - "6aa1d992-5925-4e9f-a49b-845e51d1de01"
  - "New DLL Added to AppCertDlls Registry Key"
attack_technique_ids:
  - "T1546.009"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# New DLL Added to AppCertDlls Registry Key

Dynamic-link libraries (DLLs) that are specified in the AppCertDLLs value in the Registry key can be abused to obtain persistence and privilege escalation
by causing a malicious DLL to be loaded and run in the context of separate processes on the computer.

## Metadata

- Rule ID: 6aa1d992-5925-4e9f-a49b-845e51d1de01
- Status: test
- Level: medium
- Author: Ilyas Ochkov, oscd.community
- Date: 2019-10-25
- Modified: 2021-11-27
- Source Path: rules/windows/registry/registry_event/registry_event_new_dll_added_to_appcertdlls_registry_key.yml

## Logsource

- category: registry_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1546-event_triggered_execution|T1546.009]]

## Detection

```yaml
selection:
- TargetObject: HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\AppCertDlls
- NewName: HKLM\SYSTEM\CurentControlSet\Control\Session Manager\AppCertDlls
condition: selection
```

## False Positives

- Unknown

## References

- http://www.hexacorn.com/blog/2013/01/19/beyond-good-ol-run-key-part-3/
- https://eqllib.readthedocs.io/en/latest/analytics/14f90406-10a0-4d36-a672-31cabe149f2f.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_event/registry_event_new_dll_added_to_appcertdlls_registry_key.yml)
