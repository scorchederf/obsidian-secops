---
sigma_id: "1277f594-a7d1-4f28-a2d3-73af5cbeab43"
title: "Windows Shell/Scripting Application File Write to Suspicious Folder"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_shell_write_susp_directory.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_shell_write_susp_directory.yml"
build_date: "2026-04-26 17:03:24"
status: "test"
level: "high"
logsource: "windows / file_event"
aliases:
  - "1277f594-a7d1-4f28-a2d3-73af5cbeab43"
  - "Windows Shell/Scripting Application File Write to Suspicious Folder"
attack_technique_ids:
  - "T1059"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Windows Shell/Scripting Application File Write to Suspicious Folder

Detects Windows shells and scripting applications that write files to suspicious folders

## Metadata

- Rule ID: 1277f594-a7d1-4f28-a2d3-73af5cbeab43
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2021-11-20
- Modified: 2023-03-29
- Source Path: rules/windows/file/file_event/file_event_win_shell_write_susp_directory.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059]]

## Detection

```yaml
selection_1:
  Image|endswith:
  - \bash.exe
  - \cmd.exe
  - \cscript.exe
  - \msbuild.exe
  - \powershell.exe
  - \pwsh.exe
  - \sh.exe
  - \wscript.exe
  TargetFilename|startswith:
  - C:\PerfLogs\
  - C:\Users\Public\
selection_2:
  Image|endswith:
  - \certutil.exe
  - \forfiles.exe
  - \mshta.exe
  - \schtasks.exe
  - \scriptrunner.exe
  - \wmic.exe
  TargetFilename|contains:
  - C:\PerfLogs\
  - C:\Users\Public\
  - C:\Windows\Temp\
condition: 1 of selection_*
```

## False Positives

- Unknown

## References

- Internal Research

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_shell_write_susp_directory.yml)
