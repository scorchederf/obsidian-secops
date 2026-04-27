---
sigma_id: "f11f2808-adb4-46c0-802a-8660db50fa99"
title: "ImagingDevices Unusual Parent/Child Processes"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_imagingdevices_unusual_parents.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_imagingdevices_unusual_parents.yml"
build_date: "2026-04-27 19:13:52"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "f11f2808-adb4-46c0-802a-8660db50fa99"
  - "ImagingDevices Unusual Parent/Child Processes"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects unusual parent or children of the ImagingDevices.exe (Windows Contacts) process as seen being used with Bumblebee activity

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection_parent:
  ParentImage|endswith:
  - \WmiPrvSE.exe
  - \svchost.exe
  - \dllhost.exe
  Image|endswith: \ImagingDevices.exe
selection_child:
  ParentImage|endswith: \ImagingDevices.exe
condition: 1 of selection_*
```

## False Positives

- Unknown

## References

- https://thedfirreport.com/2022/09/26/bumblebee-round-two/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_imagingdevices_unusual_parents.yml)
