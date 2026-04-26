---
sigma_id: "f354eba5-623b-450f-b073-0b5b2773b6aa"
title: "Potential DCOM InternetExplorer.Application DLL Hijack - Image Load"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_iexplore_dcom_iertutil_dll_hijack.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_iexplore_dcom_iertutil_dll_hijack.yml"
build_date: "2026-04-26 15:01:48"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Potential DCOM InternetExplorer.Application DLL Hijack - Image Load

Detects potential DLL hijack of "iertutil.dll" found in the DCOM InternetExplorer.Application Class

## Metadata

- Rule ID: f354eba5-623b-450f-b073-0b5b2773b6aa
- Status: test
- Level: critical
- Author: Roberto Rodriguez @Cyb3rWard0g, Open Threat Research (OTR), wagga
- Date: 2020-10-12
- Modified: 2022-12-18
- Source Path: rules/windows/image_load/image_load_iexplore_dcom_iertutil_dll_hijack.yml

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1021-remote_services|T1021.002]]
- [[kb/attack/techniques/T1021-remote_services|T1021.003]]

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
