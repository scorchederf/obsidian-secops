---
atomic_guid: "fb32c935-ee2e-454b-8fa3-1c46b42e8dfb"
title: "Winlogon Userinit Key Persistence - PowerShell"
framework: "atomic"
generated: "true"
attack_technique_id: "T1547.004"
attack_technique_name: "Boot or Logon Autostart Execution: Winlogon Helper DLL"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547.004/T1547.004.yaml"
build_date: "2026-04-27 19:12:27"
executor: "powershell"
aliases:
  - "fb32c935-ee2e-454b-8fa3-1c46b42e8dfb"
  - "Winlogon Userinit Key Persistence - PowerShell"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

PowerShell code to set Winlogon userinit key to execute a binary at logon along with userinit.exe.

Upon successful execution, PowerShell will modify a registry value to execute cmd.exe upon logon/logoff.

## ATT&CK Mapping

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution#^t1547004-winlogon-helper-dll|T1547.004: Winlogon Helper DLL]]

## Input Arguments

### binary_to_execute

- description: Path of binary to execute
- type: path
- default: C:\Windows\System32\cmd.exe

## Executor

- name: powershell

### Command

```powershell
Set-ItemProperty "HKCU:\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\" "Userinit" "Userinit.exe, #{binary_to_execute}" -Force
```

### Cleanup

```powershell
Remove-ItemProperty -Path "HKCU:\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\" -Name "Userinit" -Force -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547.004/T1547.004.yaml)
