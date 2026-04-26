---
atomic_guid: "634bd9b9-dc83-4229-b19f-7f83ba9ad313"
title: "Automated Collection PowerShell"
framework: "atomic"
generated: "true"
attack_technique_id: "T1119"
attack_technique_name: "Automated Collection"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1119/T1119.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "634bd9b9-dc83-4229-b19f-7f83ba9ad313"
  - "Automated Collection PowerShell"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Automated Collection PowerShell

Automated Collection. Upon execution, check the users temp directory (%temp%) for the folder T1119_powershell_collection
to see what was collected.

## Metadata

- Atomic GUID: 634bd9b9-dc83-4229-b19f-7f83ba9ad313
- Technique: T1119: Automated Collection
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1119/T1119.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1119-automated_collection|T1119]]

## Executor

- name: powershell

### Command

```powershell
New-Item -Path $env:TEMP\T1119_powershell_collection -ItemType Directory -Force | Out-Null
Get-ChildItem -Recurse -Include *.doc | % {Copy-Item $_.FullName -destination $env:TEMP\T1119_powershell_collection}
```

### Cleanup

```powershell
Remove-Item $env:TEMP\T1119_powershell_collection -Force -ErrorAction Ignore | Out-Null
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1119/T1119.yaml)
