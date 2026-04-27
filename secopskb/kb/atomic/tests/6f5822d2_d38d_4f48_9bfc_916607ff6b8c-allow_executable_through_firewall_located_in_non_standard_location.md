---
atomic_guid: "6f5822d2-d38d-4f48-9bfc-916607ff6b8c"
title: "Allow Executable Through Firewall Located in Non-Standard Location"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.004"
attack_technique_name: "Impair Defenses: Disable or Modify System Firewall"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.004/T1562.004.yaml"
build_date: "2026-04-27 19:12:28"
executor: "powershell"
aliases:
  - "6f5822d2-d38d-4f48-9bfc-916607ff6b8c"
  - "Allow Executable Through Firewall Located in Non-Standard Location"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

This test will attempt to allow an executable through the system firewall located in the Users directory

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses#^t1562004-disable-or-modify-system-firewall|T1562.004: Disable or Modify System Firewall]]

## Input Arguments

### exe_file_path

- description: path to exe file
- type: path
- default: PathToAtomicsFolder\T1562.004\bin\AtomicTest.exe

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
Copy-Item "#{exe_file_path}" -Destination "C:\Users\$env:UserName" -Force
netsh advfirewall firewall add rule name="Atomic Test" dir=in action=allow program="C:\Users\$env:UserName\AtomicTest.exe" enable=yes
```

### Cleanup

```powershell
netsh advfirewall firewall delete rule name="Atomic Test" | Out-Null
Remove-Item C:\Users\$env:UserName\AtomicTest.exe -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.004/T1562.004.yaml)
