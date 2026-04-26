---
atomic_guid: "d29f01ea-ac72-4efc-8a15-bea64b77fabf"
title: "Copy and Delete Mailbox Data on Windows"
framework: "atomic"
generated: "true"
attack_technique_id: "T1070.008"
attack_technique_name: "Email Collection: Mailbox Manipulation"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.008/T1070.008.yaml"
build_date: "2026-04-26 14:38:39"
executor: "powershell"
aliases:
  - "d29f01ea-ac72-4efc-8a15-bea64b77fabf"
  - "Copy and Delete Mailbox Data on Windows"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Copy and Delete Mailbox Data on Windows

Copies and deletes mail data on Windows

## Metadata

- Atomic GUID: d29f01ea-ac72-4efc-8a15-bea64b77fabf
- Technique: T1070.008: Email Collection: Mailbox Manipulation
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1070.008/T1070.008.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1070-indicator_removal|T1070.008]]

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
New-Item -Path "C:\Users\$env:USERNAME\AppData\Local\Comms\Unistore\data\copy" -ItemType Directory -ErrorAction Ignore
Get-ChildItem -Path "C:\Users\$env:USERNAME\AppData\Local\Comms\Unistore\data" -Exclude copy | ForEach-Object { Copy-Item -Path $_.FullName -Destination "C:\Users\$env:USERNAME\AppData\Local\Comms\Unistore\data\copy" -Recurse -Force -ErrorAction Ignore }
Remove-Item -Path "C:\Users\$env:USERNAME\AppData\Local\Comms\Unistore\data\copy" -Recurse -Force -ErrorAction Ignore
```

### Cleanup

```powershell
Remove-Item -Path "C:\Users\$env:USERNAME\AppData\Local\Comms\Unistore\data\copy" -Recurse -Force -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.008/T1070.008.yaml)
