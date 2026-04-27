---
sigma_id: "1908fcc1-1b92-4272-8214-0fbaf2fa5163"
title: "Malicious DLL File Dropped in the Teams or OneDrive Folder"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_iphlpapi_dll_sideloading.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_iphlpapi_dll_sideloading.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "high"
logsource: "windows / file_event"
aliases:
  - "1908fcc1-1b92-4272-8214-0fbaf2fa5163"
  - "Malicious DLL File Dropped in the Teams or OneDrive Folder"
attack_technique_ids:
  - "T1574.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Malicious DLL File Dropped in the Teams or OneDrive Folder

Detects creation of a malicious DLL file in the location where the OneDrive or Team applications
Upon execution of the Teams or OneDrive application, the dropped malicious DLL file ("iphlpapi.dll") is sideloaded

## Metadata

- Rule ID: 1908fcc1-1b92-4272-8214-0fbaf2fa5163
- Status: test
- Level: high
- Author: frack113
- Date: 2022-08-12
- Source Path: rules/windows/file/file_event/file_event_win_iphlpapi_dll_sideloading.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.001]]

## Detection

```yaml
selection:
  TargetFilename|contains|all:
  - iphlpapi.dll
  - \AppData\Local\Microsoft
condition: selection
```

## False Positives

- Unknown

## References

- https://blog.cyble.com/2022/07/27/targeted-attacks-being-carried-out-via-dll-sideloading/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_iphlpapi_dll_sideloading.yml)
