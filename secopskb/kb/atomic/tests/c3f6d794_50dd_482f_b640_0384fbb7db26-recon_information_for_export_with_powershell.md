---
atomic_guid: "c3f6d794-50dd-482f-b640-0384fbb7db26"
title: "Recon information for export with PowerShell"
framework: "atomic"
generated: "true"
attack_technique_id: "T1119"
attack_technique_name: "Automated Collection"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1119/T1119.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "c3f6d794-50dd-482f-b640-0384fbb7db26"
  - "Recon information for export with PowerShell"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Recon information for export with PowerShell

collect information for exfiltration. Upon execution, check the users temp directory (%temp%) for files T1119_*.txt
to see what was collected.

## Metadata

- Atomic GUID: c3f6d794-50dd-482f-b640-0384fbb7db26
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
Get-Service > $env:TEMP\T1119_1.txt
Get-ChildItem Env: > $env:TEMP\T1119_2.txt
Get-Process > $env:TEMP\T1119_3.txt
```

### Cleanup

```powershell
Remove-Item $env:TEMP\T1119_1.txt -ErrorAction Ignore
Remove-Item $env:TEMP\T1119_2.txt -ErrorAction Ignore
Remove-Item $env:TEMP\T1119_3.txt -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1119/T1119.yaml)
