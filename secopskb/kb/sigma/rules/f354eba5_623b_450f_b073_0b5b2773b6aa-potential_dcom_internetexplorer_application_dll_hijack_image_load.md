---
sigma_id: "f354eba5-623b-450f-b073-0b5b2773b6aa"
title: "Potential DCOM InternetExplorer.Application DLL Hijack - Image Load"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_iexplore_dcom_iertutil_dll_hijack.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_iexplore_dcom_iertutil_dll_hijack.yml"
build_date: "2026-04-27 19:13:53"
status: "test"
level: "critical"
logsource: "windows / image_load"
aliases:
  - "f354eba5-623b-450f-b073-0b5b2773b6aa"
  - "Potential DCOM InternetExplorer.Application DLL Hijack - Image Load"
attack_technique_ids:
  - "T1021.002"
  - "T1021.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects potential DLL hijack of "iertutil.dll" found in the DCOM InternetExplorer.Application Class

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1021-remote_services#^t1021002-smb-windows-admin-shares|T1021.002: SMB/Windows Admin Shares]]
- [[kb/attack/techniques/T1021-remote_services#^t1021003-distributed-component-object-model|T1021.003: Distributed Component Object Model]]

## Detection

```yaml
selection:
  Image|endswith: \Internet Explorer\iexplore.exe
  ImageLoaded|endswith: \Internet Explorer\iertutil.dll
condition: selection
```

## False Positives

- Unknown

## References

- https://threathunterplaybook.com/hunts/windows/201009-RemoteDCOMIErtUtilDLLHijack/notebook.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_iexplore_dcom_iertutil_dll_hijack.yml)
