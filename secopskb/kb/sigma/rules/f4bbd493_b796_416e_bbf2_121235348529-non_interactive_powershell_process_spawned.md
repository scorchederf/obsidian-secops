---
sigma_id: "f4bbd493-b796-416e-bbf2-121235348529"
title: "Non Interactive PowerShell Process Spawned"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_non_interactive_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_non_interactive_execution.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "low"
logsource: "windows / process_creation"
aliases:
  - "f4bbd493-b796-416e-bbf2-121235348529"
  - "Non Interactive PowerShell Process Spawned"
attack_technique_ids:
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Non Interactive PowerShell Process Spawned

Detects non-interactive PowerShell activity by looking at the "powershell" process with a non-user GUI process such as "explorer.exe" as a parent.

## Metadata

- Rule ID: f4bbd493-b796-416e-bbf2-121235348529
- Status: test
- Level: low
- Author: Roberto Rodriguez @Cyb3rWard0g (rule), oscd.community (improvements)
- Date: 2019-09-12
- Modified: 2025-02-28
- Source Path: rules/windows/process_creation/proc_creation_win_powershell_non_interactive_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]

## Detection

```yaml
selection:
- Image|endswith:
  - \powershell.exe
  - \pwsh.exe
- OriginalFileName:
  - PowerShell.EXE
  - pwsh.dll
filter_main_generic:
  ParentImage|endswith:
  - :\Windows\explorer.exe
  - :\Windows\System32\CompatTelRunner.exe
  - :\Windows\SysWOW64\explorer.exe
filter_main_windows_update:
  ParentImage: :\$WINDOWS.~BT\Sources\SetupHost.exe
filter_optional_vscode:
  ParentImage|endswith: \AppData\Local\Programs\Microsoft VS Code\Code.exe
  ParentCommandLine|contains: ' --ms-enable-electron-run-as-node '
filter_optional_terminal:
  ParentImage|contains: :\Program Files\WindowsApps\Microsoft.WindowsTerminal_
  ParentImage|endswith: \WindowsTerminal.exe
filter_optional_defender:
  ParentImage|endswith: :\Program Files\Windows Defender Advanced Threat Protection\SenseIR.exe
condition: selection and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- Likely. Many admin scripts and tools leverage PowerShell in their BAT or VB scripts which may trigger this rule often. It is best to add additional filters or use this to hunt for anomalies

## References

- https://web.archive.org/web/20200925032237/https://threathunterplaybook.com/notebooks/windows/02_execution/WIN-190410151110.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_non_interactive_execution.yml)
