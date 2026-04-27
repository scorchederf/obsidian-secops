---
atomic_guid: "c3d24a39-2bfe-4c6a-b064-90cd73896cb0"
title: "Masquerading - windows exe running as different windows exe"
framework: "atomic"
generated: "true"
attack_technique_id: "T1036.003"
attack_technique_name: "Masquerading: Rename System Utilities"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1036.003/T1036.003.yaml"
build_date: "2026-04-27 19:12:25"
executor: "powershell"
aliases:
  - "c3d24a39-2bfe-4c6a-b064-90cd73896cb0"
  - "Masquerading - windows exe running as different windows exe"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Copies a windows exe, renames it as another windows exe, and launches it to masquerade as second windows exe

## ATT&CK Mapping

- [[kb/attack/techniques/T1036-masquerading#^t1036003-rename-legitimate-utilities|T1036.003: Rename Legitimate Utilities]]

## Input Arguments

### inputfile

- description: path of file to copy
- type: path
- default: $env:ComSpec

### outputfile

- description: path of file to execute
- type: path
- default: ($env:TEMP + "\svchost.exe")

## Executor

- name: powershell

### Command

```powershell
copy "#{inputfile}" #{outputfile}
$myT1036_003 = (Start-Process -PassThru -FilePath #{outputfile}).Id
Stop-Process -ID $myT1036_003
```

### Cleanup

```powershell
Remove-Item #{outputfile} -Force -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1036.003/T1036.003.yaml)
