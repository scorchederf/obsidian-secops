---
atomic_guid: "0128e48e-8c1a-433a-a11a-a5387384f1e1"
title: "Read-Write-Execute process Injection"
framework: "atomic"
generated: "true"
attack_technique_id: "T1055"
attack_technique_name: "Process Injection"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1055/T1055.yaml"
build_date: "2026-04-27 19:12:26"
executor: "powershell"
aliases:
  - "0128e48e-8c1a-433a-a11a-a5387384f1e1"
  - "Read-Write-Execute process Injection"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

This test exploited the vulnerability in legitimate PE formats where sections have RWX permission and enough space for shellcode.
The RWX injection avoided the use of VirtualAlloc, WriteVirtualMemory, and ProtectVirtualMemory, thus evading detection mechanisms 
that relied on API call sequences and heuristics. The RWX injection utilises API call sequences: LoadLibrary --> GetModuleInformation --> GetModuleHandleA --> RtlCopyMemory --> CreateThread.
The injected shellcode will open a message box and a notepad.
RWX Process Injection, also known as MockingJay, was introduced to the security community by SecurityJoes.
More details can be found at https://www.securityjoes.com/post/process-mockingjay-echoing-rwx-in-userland-to-achieve-code-execution.
The original injector and idea were developed for game cheats, as visible at https://github.com/M-r-J-o-h-n/SWH-Injector.

## ATT&CK Mapping

- [[kb/attack/techniques/T1055-process_injection|T1055: Process Injection]]

## Input Arguments

### vuln_dll

- description: vulnerable DLL
- type: path
- default: PathToAtomicsFolder\T1055\bin\x64\vuln_dll\msys-2.0.dll

## Dependencies

Utility to inject must exist on disk at specified location (#{vuln_dll})

### Prerequisite Check

```powershell
if (Test-Path "#{vuln_dll}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory (split-path "#{vuln_dll}") -ErrorAction ignore | Out-Null
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1055/bin/x64/vuln_dll/msys-2.0.dll" -OutFile "#{vuln_dll}"
```

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
$address = (& "$PathToAtomicsFolder\T1055\bin\x64\searchVuln.exe" "$PathToAtomicsFolder\T1055\bin\x64\vuln_dll\" | Out-String | Select-String -Pattern "VirtualAddress: (\w+)").Matches.Groups[1].Value
& "PathToAtomicsFolder\T1055\bin\x64\RWXinjectionLocal.exe" "#{vuln_dll}" $address
```

### Cleanup

```powershell
Get-Process -Name Notepad -ErrorAction SilentlyContinue | Stop-Process -Force
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1055/T1055.yaml)
