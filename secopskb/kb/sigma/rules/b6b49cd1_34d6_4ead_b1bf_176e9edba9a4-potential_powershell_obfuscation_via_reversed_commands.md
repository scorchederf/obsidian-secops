---
sigma_id: "b6b49cd1-34d6-4ead-b1bf-176e9edba9a4"
title: "Potential PowerShell Obfuscation Via Reversed Commands"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_cmdline_reversed_strings.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_cmdline_reversed_strings.yml"
build_date: "2026-04-26 17:03:21"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "b6b49cd1-34d6-4ead-b1bf-176e9edba9a4"
  - "Potential PowerShell Obfuscation Via Reversed Commands"
attack_technique_ids:
  - "T1027"
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Potential PowerShell Obfuscation Via Reversed Commands

Detects the presence of reversed PowerShell commands in the CommandLine. This is often used as a method of obfuscation by attackers

## Metadata

- Rule ID: b6b49cd1-34d6-4ead-b1bf-176e9edba9a4
- Status: test
- Level: high
- Author: Teymur Kheirkhabarov (idea), Vasiliy Burov (rule), oscd.community, Tim Shelton
- Date: 2020-10-11
- Modified: 2023-05-31
- Source Path: rules/windows/process_creation/proc_creation_win_powershell_cmdline_reversed_strings.yml

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
  CommandLine|contains:
  - hctac
  - kaerb
  - dnammoc
  - ekovn
  - eliFd
  - rahc
  - etirw
  - golon
  - tninon
  - eddih
  - tpircS
  - ssecorp
  - llehsrewop
  - esnopser
  - daolnwod
  - tneilCbeW
  - tneilc
  - ptth
  - elifotevas
  - 46esab
  - htaPpmeTteG
  - tcejbO
  - maerts
  - hcaerof
  - retupmoc
filter_main_encoded_keyword:
  CommandLine|contains:
  - ' -EncodedCommand '
  - ' -enc '
condition: all of selection_* and not 1 of filter_main_*
```

## False Positives

- Unlikely

## References

- https://2019.offzone.moscow/ru/report/hunting-for-powershell-abuses/
- https://speakerdeck.com/heirhabarov/hunting-for-powershell-abuse?slide=66

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_cmdline_reversed_strings.yml)
