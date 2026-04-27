---
sigma_id: "90ae0469-0cee-4509-b67f-e5efcef040f7"
title: "Aruba Network Service Potential DLL Sideloading"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_side_load_aruba_networks_virtual_intranet_access.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_aruba_networks_virtual_intranet_access.yml"
build_date: "2026-04-27 19:13:50"
status: "test"
level: "high"
logsource: "windows / image_load"
aliases:
  - "90ae0469-0cee-4509-b67f-e5efcef040f7"
  - "Aruba Network Service Potential DLL Sideloading"
attack_technique_ids:
  - "T1574.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects potential DLL sideloading activity via the Aruba Networks Virtual Intranet Access "arubanetsvc.exe" process using DLL Search Order Hijacking

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow#^t1574001-dll|T1574.001: DLL]]

## Detection

```yaml
selection:
  Image|endswith: \arubanetsvc.exe
  ImageLoaded|endswith:
  - \wtsapi32.dll
  - \msvcr100.dll
  - \msvcp100.dll
  - \dbghelp.dll
  - \dbgcore.dll
  - \wininet.dll
  - \iphlpapi.dll
  - \version.dll
  - \cryptsp.dll
  - \cryptbase.dll
  - \wldp.dll
  - \profapi.dll
  - \sspicli.dll
  - \winsta.dll
  - \dpapi.dll
filter:
  ImageLoaded|startswith:
  - C:\Windows\System32\
  - C:\Windows\SysWOW64\
  - C:\Windows\WinSxS\
condition: selection and not filter
```

## False Positives

- Unknown

## References

- https://twitter.com/wdormann/status/1616581559892545537?t=XLCBO9BziGzD7Bmbt8oMEQ&s=09

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_aruba_networks_virtual_intranet_access.yml)
