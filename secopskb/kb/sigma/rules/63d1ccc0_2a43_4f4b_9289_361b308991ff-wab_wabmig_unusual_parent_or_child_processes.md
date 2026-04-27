---
sigma_id: "63d1ccc0-2a43-4f4b-9289-361b308991ff"
title: "Wab/Wabmig Unusual Parent Or Child Processes"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_wab_unusual_parents.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wab_unusual_parents.yml"
build_date: "2026-04-26 17:03:24"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "63d1ccc0-2a43-4f4b-9289-361b308991ff"
  - "Wab/Wabmig Unusual Parent Or Child Processes"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Wab/Wabmig Unusual Parent Or Child Processes

Detects unusual parent or children of the wab.exe (Windows Contacts) and Wabmig.exe (Microsoft Address Book Import Tool) processes as seen being used with bumblebee activity

## Metadata

- Rule ID: 63d1ccc0-2a43-4f4b-9289-361b308991ff
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-08-12
- Modified: 2022-09-27
- Source Path: rules/windows/process_creation/proc_creation_win_wab_unusual_parents.yml

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
  Image|endswith:
  - \wab.exe
  - \wabmig.exe
selection_child:
  ParentImage|endswith:
  - \wab.exe
  - \wabmig.exe
condition: 1 of selection_*
```

## False Positives

- Unknown

## References

- https://thedfirreport.com/2022/08/08/bumblebee-roasts-its-way-to-domain-admin/
- https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/bumblebee-loader-cybercrime
- https://thedfirreport.com/2022/09/26/bumblebee-round-two/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wab_unusual_parents.yml)
