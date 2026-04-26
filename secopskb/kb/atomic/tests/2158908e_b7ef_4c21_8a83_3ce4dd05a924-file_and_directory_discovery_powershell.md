---
atomic_guid: "2158908e-b7ef-4c21-8a83-3ce4dd05a924"
title: "File and Directory Discovery (PowerShell)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1083"
attack_technique_name: "File and Directory Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1083/T1083.yaml"
build_date: "2026-04-26 14:38:39"
executor: "powershell"
aliases:
  - "2158908e-b7ef-4c21-8a83-3ce4dd05a924"
  - "File and Directory Discovery (PowerShell)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# File and Directory Discovery (PowerShell)

Find or discover files on the file system. Upon execution, file and folder information will be displayed.

## Metadata

- Atomic GUID: 2158908e-b7ef-4c21-8a83-3ce4dd05a924
- Technique: T1083: File and Directory Discovery
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1083/T1083.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1083-file_and_directory_discovery|T1083]]

## Executor

- name: powershell

### Command

```powershell
ls -recurse
get-childitem -recurse
gci -recurse
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1083/T1083.yaml)
