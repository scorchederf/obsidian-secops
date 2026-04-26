---
sigma_id: "cdf05894-89e7-4ead-b2b0-0a5f97a90f2f"
title: "Potential Encoded PowerShell Patterns In CommandLine"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_encoding_patterns.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_encoding_patterns.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "low"
logsource: "windows / process_creation"
aliases:
  - "cdf05894-89e7-4ead-b2b0-0a5f97a90f2f"
  - "Potential Encoded PowerShell Patterns In CommandLine"
attack_technique_ids:
  - "T1027"
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Encoded PowerShell Patterns In CommandLine

Detects specific combinations of encoding methods in PowerShell via the commandline

## Metadata

- Rule ID: cdf05894-89e7-4ead-b2b0-0a5f97a90f2f
- Status: test
- Level: low
- Author: Teymur Kheirkhabarov (idea), Vasiliy Burov (rule), oscd.community, Tim Shelton
- Date: 2020-10-11
- Modified: 2023-01-26
- Source Path: rules/windows/process_creation/proc_creation_win_powershell_encoding_patterns.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1027-obfuscated_files_or_information|T1027]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]

## Detection

```yaml
selection_img:
- Image|endswith:
  - \powershell.exe
  - \pwsh.exe
- OriginalFileName:
  - PowerShell.EXE
  - pwsh.dll
selection_to_1:
  CommandLine|contains:
  - ToInt
  - ToDecimal
  - ToByte
  - ToUint
  - ToSingle
  - ToSByte
selection_to_2:
  CommandLine|contains:
  - ToChar
  - ToString
  - String
selection_gen_1:
  CommandLine|contains|all:
  - char
  - join
selection_gen_2:
  CommandLine|contains|all:
  - split
  - join
condition: selection_img and (all of selection_to_* or 1 of selection_gen_*)
```

## False Positives

- Unknown

## References

- https://speakerdeck.com/heirhabarov/hunting-for-powershell-abuse?slide=65

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_encoding_patterns.yml)
