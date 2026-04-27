---
atomic_guid: "de323a93-2f18-4bd5-ba60-d6fca6aeff76"
title: "Indirect Command Execution - RunMRU Dialog"
framework: "atomic"
generated: "true"
attack_technique_id: "T1202"
attack_technique_name: "Indirect Command Execution"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1202/T1202.yaml"
build_date: "2026-04-27 19:12:27"
executor: "powershell"
aliases:
  - "de323a93-2f18-4bd5-ba60-d6fca6aeff76"
  - "Indirect Command Execution - RunMRU Dialog"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Simulates execution of commands via the Windows Run dialog (Win+R) by programmatically opening the Run dialog, 
copying a command to clipboard, and automating the paste and execution. This generates artifacts in the RunMRU registry key,
which is commonly abused by threat actors to execute malicious commands disguised as CAPTCHA verification steps.
Upon execution, a test PowerShell command will be executed through the Run dialog.

## ATT&CK Mapping

- [[kb/attack/techniques/T1202-indirect_command_execution|T1202: Indirect Command Execution]]

## Input Arguments

### command

- description: Command to execute via Run dialog
- type: string
- default: calc.exe

## Executor

- name: powershell

### Command

```powershell
# Copy command to clipboard
Set-Clipboard -Value '#{command}'

# Open Run dialog
Start-Process -FilePath "powershell" -ArgumentList "-c (New-Object -ComObject 'Shell.Application').FileRun()" -WindowStyle Hidden

# Wait for Run dialog to open
Start-Sleep -Seconds 1

# Paste command and execute
Add-Type -AssemblyName System.Windows.Forms
[System.Windows.Forms.SendKeys]::SendWait('^v')
Start-Sleep -Milliseconds 500
[System.Windows.Forms.SendKeys]::SendWait('{ENTER}')
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1202/T1202.yaml)
