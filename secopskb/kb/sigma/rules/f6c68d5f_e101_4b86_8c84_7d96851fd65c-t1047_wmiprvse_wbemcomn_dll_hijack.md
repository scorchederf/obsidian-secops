---
sigma_id: "f6c68d5f-e101-4b86-8c84-7d96851fd65c"
title: "T1047 Wmiprvse Wbemcomn DLL Hijack"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_wmiprvse_wbemcomn_dll_hijack.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_wmiprvse_wbemcomn_dll_hijack.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "windows / security"
aliases:
  - "f6c68d5f-e101-4b86-8c84-7d96851fd65c"
  - "T1047 Wmiprvse Wbemcomn DLL Hijack"
attack_technique_ids:
  - "T1047"
  - "T1021.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# T1047 Wmiprvse Wbemcomn DLL Hijack

Detects a threat actor creating a file named `wbemcomn.dll` in the `C:\Windows\System32\wbem\` directory over the network for a WMI DLL Hijack scenario.

## Metadata

- Rule ID: f6c68d5f-e101-4b86-8c84-7d96851fd65c
- Status: test
- Level: high
- Author: Roberto Rodriguez @Cyb3rWard0g, Open Threat Research (OTR)
- Date: 2020-10-12
- Modified: 2022-02-24
- Source Path: rules/windows/builtin/security/win_security_wmiprvse_wbemcomn_dll_hijack.yml

## Logsource

- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1047-windows_management_instrumentation|T1047]]
- [[kb/attack/techniques/T1021-remote_services|T1021.002]]

## Detection

```yaml
selection:
  EventID: 5145
  RelativeTargetName|endswith: \wbem\wbemcomn.dll
filter:
  SubjectUserName|endswith: $
condition: selection and not filter
```

## False Positives

- Unknown

## References

- https://threathunterplaybook.com/hunts/windows/201009-RemoteWMIWbemcomnDLLHijack/notebook.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_wmiprvse_wbemcomn_dll_hijack.yml)
