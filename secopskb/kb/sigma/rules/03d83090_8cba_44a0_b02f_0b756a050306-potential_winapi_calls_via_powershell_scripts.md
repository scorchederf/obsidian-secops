---
sigma_id: "03d83090-8cba-44a0-b02f-0b756a050306"
title: "Potential WinAPI Calls Via PowerShell Scripts"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_win_api_susp_access.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_win_api_susp_access.yml"
build_date: "2026-04-27 19:13:54"
status: "test"
level: "high"
logsource: "windows / ps_script"
aliases:
  - "03d83090-8cba-44a0-b02f-0b756a050306"
  - "Potential WinAPI Calls Via PowerShell Scripts"
attack_technique_ids:
  - "T1059.001"
  - "T1106"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects use of WinAPI functions in PowerShell scripts

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter#^t1059001-powershell|T1059.001: PowerShell]]
- [[kb/attack/techniques/T1106-native_api|T1106: Native API]]

## Detection

```yaml
selection_injection:
  ScriptBlockText|contains|all:
  - VirtualAlloc
  - OpenProcess
  - WriteProcessMemory
  - CreateRemoteThread
selection_token_steal:
  ScriptBlockText|contains|all:
  - OpenProcessToken
  - LookupPrivilegeValue
  - AdjustTokenPrivileges
selection_duplicate_token:
  ScriptBlockText|contains|all:
  - OpenProcessToken
  - DuplicateTokenEx
  - CloseHandle
selection_process_write_read:
  ScriptBlockText|contains|all:
  - WriteProcessMemory
  - VirtualAlloc
  - ReadProcessMemory
  - VirtualFree
condition: 1 of selection_*
```

## False Positives

- Unknown

## References

- https://speakerdeck.com/heirhabarov/hunting-for-powershell-abuse

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_win_api_susp_access.yml)
