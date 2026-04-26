---
sigma_id: "6f8b3439-a203-45dc-a88b-abf57ea15ccf"
title: "HackTool - CrackMapExec PowerShell Obfuscation"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_crackmapexec_powershell_obfuscation.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_crackmapexec_powershell_obfuscation.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "6f8b3439-a203-45dc-a88b-abf57ea15ccf"
  - "HackTool - CrackMapExec PowerShell Obfuscation"
attack_technique_ids:
  - "T1059.001"
  - "T1027.005"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# HackTool - CrackMapExec PowerShell Obfuscation

The CrachMapExec pentesting framework implements a PowerShell obfuscation with some static strings detected by this rule.

## Metadata

- Rule ID: 6f8b3439-a203-45dc-a88b-abf57ea15ccf
- Status: test
- Level: high
- Author: Thomas Patzke
- Date: 2020-05-22
- Modified: 2023-02-21
- Source Path: rules/windows/process_creation/proc_creation_win_hktl_crackmapexec_powershell_obfuscation.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]
- [[kb/attack/techniques/T1027-obfuscated_files_or_information|T1027.005]]

## Detection

```yaml
selection_img:
- Image|endswith:
  - \powershell.exe
  - \pwsh.exe
- OriginalFileName:
  - PowerShell.EXE
  - pwsh.dll
selection_cli:
  CommandLine|contains:
  - join*split
  - ( $ShellId[1]+$ShellId[13]+'x')
  - ( $PSHome[*]+$PSHOME[*]+
  - ( $env:Public[13]+$env:Public[5]+'x')
  - ( $env:ComSpec[4,*,25]-Join'')
  - '[1,3]+''x''-Join'''')'
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://github.com/byt3bl33d3r/CrackMapExec
- https://github.com/byt3bl33d3r/CrackMapExec/blob/0a49f75347b625e81ee6aa8c33d3970b5515ea9e/cme/helpers/powershell.py#L242

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_crackmapexec_powershell_obfuscation.yml)
