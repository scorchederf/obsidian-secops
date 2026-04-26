---
sigma_id: "7864a175-3654-4824-9f0d-f0da18ab27c0"
title: "Password Set to Never Expire via WMI"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_wmi_password_never_expire.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wmi_password_never_expire.yml"
build_date: "2026-04-26 14:14:30"
status: "experimental"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "7864a175-3654-4824-9f0d-f0da18ab27c0"
  - "Password Set to Never Expire via WMI"
attack_technique_ids:
  - "T1047"
  - "T1098"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Password Set to Never Expire via WMI

Detects the use of wmic.exe to modify user account settings and explicitly disable password expiration.

## Metadata

- Rule ID: 7864a175-3654-4824-9f0d-f0da18ab27c0
- Status: experimental
- Level: medium
- Author: Daniel Koifman (KoifSec)
- Date: 2025-07-30
- Source Path: rules/windows/process_creation/proc_creation_win_wmi_password_never_expire.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1047-windows_management_instrumentation|T1047]]
- [[kb/attack/techniques/T1098-account_manipulation|T1098]]

## Detection

```yaml
selection_img:
- Image|endswith: \wmic.exe
- OriginalFileName: wmic.exe
selection_cli:
  CommandLine|contains|all:
  - useraccount
  - ' set '
  - passwordexpires
  - 'false'
condition: all of selection_*
```

## False Positives

- Legitimate administrative activity

## References

- https://www.huntress.com/blog/the-unwanted-guest

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wmi_password_never_expire.yml)
