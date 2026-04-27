---
atomic_guid: "36f96049-0ad7-4a5f-8418-460acaeb92fb"
title: "Delete Prefetch File"
framework: "atomic"
generated: "true"
attack_technique_id: "T1070.004"
attack_technique_name: "Indicator Removal on Host: File Deletion"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.004/T1070.004.yaml"
build_date: "2026-04-27 19:12:26"
executor: "powershell"
aliases:
  - "36f96049-0ad7-4a5f-8418-460acaeb92fb"
  - "Delete Prefetch File"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Delete a single prefetch file.  Deletion of prefetch files is a known anti-forensic technique. To verify execution, Run `(Get-ChildItem -Path "$Env:SystemRoot\prefetch\*.pf" | Measure-Object).Count`
before and after the test to verify that the number of prefetch files decreases by 1.

## ATT&CK Mapping

- [[kb/attack/techniques/T1070-indicator_removal#^t1070004-file-deletion|T1070.004: File Deletion]]

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
Remove-Item -Path (Join-Path "$Env:SystemRoot\prefetch\" (Get-ChildItem -Path "$Env:SystemRoot\prefetch\*.pf" -Name)[0])
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.004/T1070.004.yaml)
