---
sigma_id: "bb780e0c-16cf-4383-8383-1e5471db6cf9"
title: "Suspicious XOR Encoded PowerShell Command"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_xor_commandline.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_xor_commandline.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "bb780e0c-16cf-4383-8383-1e5471db6cf9"
  - "Suspicious XOR Encoded PowerShell Command"
attack_technique_ids:
  - "T1059.001"
  - "T1140"
  - "T1027"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious XOR Encoded PowerShell Command

Detects presence of a potentially xor encoded powershell command

## Metadata

- Rule ID: bb780e0c-16cf-4383-8383-1e5471db6cf9
- Status: test
- Level: medium
- Author: Sami Ruohonen, Harish Segar, Tim Shelton, Teymur Kheirkhabarov, Vasiliy Burov, oscd.community, Nasreddine Bencherchali
- Date: 2018-09-05
- Modified: 2023-01-30
- Source Path: rules/windows/process_creation/proc_creation_win_powershell_xor_commandline.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]
- [[kb/attack/techniques/T1140-deobfuscate_decode_files_or_information|T1140]]
- [[kb/attack/techniques/T1027-obfuscated_files_or_information|T1027]]

## Detection

```yaml
selection_img:
- Image|endswith:
  - \powershell.exe
  - \pwsh.exe
- OriginalFileName:
  - PowerShell.EXE
  - pwsh.dll
- Description: Windows PowerShell
- Product: PowerShell Core 6
selection_cli_xor:
  CommandLine|contains: bxor
selection_cli_other:
  CommandLine|contains:
  - ForEach
  - for(
  - 'for '
  - '-join '
  - -join'
  - -join"
  - -join`
  - ::Join
  - '[char]'
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://speakerdeck.com/heirhabarov/hunting-for-powershell-abuse?slide=65
- https://redcanary.com/blog/yellow-cockatoo/
- https://zero2auto.com/2020/05/19/netwalker-re/
- https://mez0.cc/posts/cobaltstrike-powershell-exec/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_xor_commandline.yml)
