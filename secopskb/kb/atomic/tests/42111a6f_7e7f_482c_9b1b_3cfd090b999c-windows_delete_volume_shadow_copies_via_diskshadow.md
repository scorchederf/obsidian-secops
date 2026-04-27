---
atomic_guid: "42111a6f-7e7f-482c-9b1b-3cfd090b999c"
title: "Windows - Delete Volume Shadow Copies via Diskshadow"
framework: "atomic"
generated: "true"
attack_technique_id: "T1490"
attack_technique_name: "Inhibit System Recovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1490/T1490.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "42111a6f-7e7f-482c-9b1b-3cfd090b999c"
  - "Windows - Delete Volume Shadow Copies via Diskshadow"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Windows - Delete Volume Shadow Copies via Diskshadow

Deletes Windows Volume Shadow Copies via Diskshadow binary. This technique is used by numerous ransomware families such as Crytox. The binary is present by default in Windows Server operating systems (since Windows Server 2008). Upon execution, it will delete all shadow copies of the server.

## Metadata

- Atomic GUID: 42111a6f-7e7f-482c-9b1b-3cfd090b999c
- Technique: T1490: Inhibit System Recovery
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Dependency Executor: powershell
- Source Path: atomics/T1490/T1490.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1490-inhibit_system_recovery|T1490]]

## Dependencies

Create volume shadow copy of C:\ . This prereq command only works on Windows Server or Windows 8.

### Prerequisite Check

```powershell
if(!(vssadmin.exe list shadows | findstr "No items found that satisfy the query.")) { exit 0 } else { exit 1 }
```

### Get Prerequisite

```powershell
vssadmin.exe create shadow /for=c:
```

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
"delete shadows all" | diskshadow.exe
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1490/T1490.yaml)
