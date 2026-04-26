---
sigma_id: "74403157-20f5-415d-89a7-c505779585cf"
title: "ConvertTo-SecureString Cmdlet Usage Via CommandLine"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_cmdline_convertto_securestring.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_cmdline_convertto_securestring.yml"
build_date: "2026-04-26 14:14:22"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "74403157-20f5-415d-89a7-c505779585cf"
  - "ConvertTo-SecureString Cmdlet Usage Via CommandLine"
attack_technique_ids:
  - "T1027"
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# ConvertTo-SecureString Cmdlet Usage Via CommandLine

Detects usage of the "ConvertTo-SecureString" cmdlet via the commandline. Which is fairly uncommon and could indicate potential suspicious activity

## Metadata

- Rule ID: 74403157-20f5-415d-89a7-c505779585cf
- Status: test
- Level: medium
- Author: Teymur Kheirkhabarov (idea), Vasiliy Burov (rule), oscd.community, Tim Shelton
- Date: 2020-10-11
- Modified: 2023-02-01
- Source Path: rules/windows/process_creation/proc_creation_win_powershell_cmdline_convertto_securestring.yml

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
selection_cli:
  CommandLine|contains: ConvertTo-SecureString
condition: all of selection_*
```

## False Positives

- Legitimate use to pass password to different powershell commands

## References

- https://speakerdeck.com/heirhabarov/hunting-for-powershell-abuse?slide=65
- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.security/convertto-securestring?view=powershell-7.3#examples

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_cmdline_convertto_securestring.yml)
