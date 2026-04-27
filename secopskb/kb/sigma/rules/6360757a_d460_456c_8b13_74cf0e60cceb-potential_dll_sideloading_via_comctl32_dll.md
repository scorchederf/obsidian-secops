---
sigma_id: "6360757a-d460-456c-8b13-74cf0e60cceb"
title: "Potential DLL Sideloading Via comctl32.dll"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_side_load_comctl32.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_comctl32.yml"
build_date: "2026-04-26 17:03:20"
status: "test"
level: "high"
logsource: "windows / image_load"
aliases:
  - "6360757a-d460-456c-8b13-74cf0e60cceb"
  - "Potential DLL Sideloading Via comctl32.dll"
attack_technique_ids:
  - "T1574.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Potential DLL Sideloading Via comctl32.dll

Detects potential DLL sideloading using comctl32.dll to obtain system privileges

## Metadata

- Rule ID: 6360757a-d460-456c-8b13-74cf0e60cceb
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems), Subhash Popuri (@pbssubhash)
- Date: 2022-12-16
- Modified: 2022-12-19
- Source Path: rules/windows/image_load/image_load_side_load_comctl32.yml

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.001]]

## Detection

```yaml
selection:
  ImageLoaded|startswith:
  - C:\Windows\System32\logonUI.exe.local\
  - C:\Windows\System32\werFault.exe.local\
  - C:\Windows\System32\consent.exe.local\
  - C:\Windows\System32\narrator.exe.local\
  - C:\windows\system32\wermgr.exe.local\
  ImageLoaded|endswith: \comctl32.dll
condition: selection
```

## False Positives

- Unlikely

## References

- https://github.com/binderlabs/DirCreate2System
- https://github.com/sailay1996/awesome_windows_logical_bugs/blob/60cbb23a801f4c3195deac1cc46df27c225c3d07/dir_create2system.txt

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_comctl32.yml)
