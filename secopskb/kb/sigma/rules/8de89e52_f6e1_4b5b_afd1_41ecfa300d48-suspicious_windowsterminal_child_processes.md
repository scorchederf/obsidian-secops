---
sigma_id: "8de89e52-f6e1-4b5b-afd1-41ecfa300d48"
title: "Suspicious WindowsTerminal Child Processes"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_windows_terminal_susp_children.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_windows_terminal_susp_children.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "8de89e52-f6e1-4b5b-afd1-41ecfa300d48"
  - "Suspicious WindowsTerminal Child Processes"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious WindowsTerminal Child Processes

Detects suspicious children spawned via the Windows Terminal application which could be a sign of persistence via WindowsTerminal (see references section)

## Metadata

- Rule ID: 8de89e52-f6e1-4b5b-afd1-41ecfa300d48
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-07-25
- Modified: 2023-02-14
- Source Path: rules/windows/process_creation/proc_creation_win_windows_terminal_susp_children.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection_parent:
  ParentImage|endswith:
  - \WindowsTerminal.exe
  - \wt.exe
selection_susp:
- Image|endswith:
  - \rundll32.exe
  - \regsvr32.exe
  - \certutil.exe
  - \cscript.exe
  - \wscript.exe
  - \csc.exe
- Image|contains:
  - C:\Users\Public\
  - \Downloads\
  - \Desktop\
  - \AppData\Local\Temp\
  - \Windows\TEMP\
- CommandLine|contains:
  - ' iex '
  - ' icm'
  - Invoke-
  - 'Import-Module '
  - 'ipmo '
  - DownloadString(
  - ' /c '
  - ' /k '
  - ' /r '
filter_builtin_visual_studio_shell:
  CommandLine|contains|all:
  - Import-Module
  - Microsoft.VisualStudio.DevShell.dll
  - Enter-VsDevShell
filter_open_settings:
  CommandLine|contains|all:
  - \AppData\Local\Packages\Microsoft.WindowsTerminal_
  - \LocalState\settings.json
filter_vsdevcmd:
  CommandLine|contains|all:
  - C:\Program Files\Microsoft Visual Studio\
  - \Common7\Tools\VsDevCmd.bat
condition: all of selection_* and not 1 of filter_*
```

## False Positives

- Other legitimate "Windows Terminal" profiles

## References

- https://persistence-info.github.io/Data/windowsterminalprofile.html
- https://twitter.com/nas_bench/status/1550836225652686848

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_windows_terminal_susp_children.yml)
