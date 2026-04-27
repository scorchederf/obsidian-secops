---
sigma_id: "614a7e17-5643-4d89-b6fe-f9df1a79641c"
title: "Wmiprvse Wbemcomn DLL Hijack - File"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_wmiprvse_wbemcomn_dll_hijack.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_wmiprvse_wbemcomn_dll_hijack.yml"
build_date: "2026-04-27 19:13:59"
status: "test"
level: "critical"
logsource: "windows / file_event"
aliases:
  - "614a7e17-5643-4d89-b6fe-f9df1a79641c"
  - "Wmiprvse Wbemcomn DLL Hijack - File"
attack_technique_ids:
  - "T1047"
  - "T1021.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects a threat actor creating a file named `wbemcomn.dll` in the `C:\Windows\System32\wbem\` directory over the network and loading it for a WMI DLL Hijack scenario.

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1047-windows_management_instrumentation|T1047: Windows Management Instrumentation]]
- [[kb/attack/techniques/T1021-remote_services#^t1021002-smb-windows-admin-shares|T1021.002: SMB/Windows Admin Shares]]

## Detection

```yaml
selection:
  Image: System
  TargetFilename|endswith: \wbem\wbemcomn.dll
condition: selection
```

## False Positives

- Unknown

## References

- https://threathunterplaybook.com/hunts/windows/201009-RemoteWMIWbemcomnDLLHijack/notebook.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_wmiprvse_wbemcomn_dll_hijack.yml)
