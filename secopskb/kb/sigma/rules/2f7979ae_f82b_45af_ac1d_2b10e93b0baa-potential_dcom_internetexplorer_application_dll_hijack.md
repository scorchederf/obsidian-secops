---
sigma_id: "2f7979ae-f82b-45af-ac1d-2b10e93b0baa"
title: "Potential DCOM InternetExplorer.Application DLL Hijack"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_dcom_iertutil_dll_hijack.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_dcom_iertutil_dll_hijack.yml"
build_date: "2026-04-27 19:13:53"
status: "test"
level: "critical"
logsource: "windows / file_event"
aliases:
  - "2f7979ae-f82b-45af-ac1d-2b10e93b0baa"
  - "Potential DCOM InternetExplorer.Application DLL Hijack"
attack_technique_ids:
  - "T1021.002"
  - "T1021.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects potential DLL hijack of "iertutil.dll" found in the DCOM InternetExplorer.Application Class over the network

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1021-remote_services#^t1021002-smb-windows-admin-shares|T1021.002: SMB/Windows Admin Shares]]
- [[kb/attack/techniques/T1021-remote_services#^t1021003-distributed-component-object-model|T1021.003: Distributed Component Object Model]]

## Detection

```yaml
selection:
  Image: System
  TargetFilename|endswith: \Internet Explorer\iertutil.dll
condition: selection
```

## False Positives

- Unknown

## References

- https://threathunterplaybook.com/hunts/windows/201009-RemoteDCOMIErtUtilDLLHijack/notebook.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_dcom_iertutil_dll_hijack.yml)
