---
sigma_id: "ae9b0bd7-8888-4606-b444-0ed7410cb728"
title: "Writing Of Malicious Files To The Fonts Folder"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_hiding_malware_in_fonts_folder.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_hiding_malware_in_fonts_folder.yml"
build_date: "2026-04-26 14:14:40"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "ae9b0bd7-8888-4606-b444-0ed7410cb728"
  - "Writing Of Malicious Files To The Fonts Folder"
attack_technique_ids:
  - "T1211"
  - "T1059"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Writing Of Malicious Files To The Fonts Folder

Monitors for the hiding possible malicious files in the C:\Windows\Fonts\ location. This folder doesn't require admin privillege to be written and executed from.

## Metadata

- Rule ID: ae9b0bd7-8888-4606-b444-0ed7410cb728
- Status: test
- Level: medium
- Author: Sreeman
- Date: 2020-04-21
- Modified: 2022-03-08
- Source Path: rules/windows/process_creation/proc_creation_win_susp_hiding_malware_in_fonts_folder.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1211-exploitation_for_defense_evasion|T1211]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059]]

## Detection

```yaml
selection_1:
  CommandLine|contains:
  - echo
  - copy
  - type
  - file createnew
  - cacls
selection_2:
  CommandLine|contains: C:\Windows\Fonts\
selection_3:
  CommandLine|contains:
  - .sh
  - .exe
  - .dll
  - .bin
  - .bat
  - .cmd
  - .js
  - .msh
  - .reg
  - .scr
  - .ps
  - .vb
  - .jar
  - .pl
  - '.inf'
  - .cpl
  - .hta
  - .msi
  - .vbs
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://thedfirreport.com/2020/04/20/sqlserver-or-the-miner-in-the-basement/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_hiding_malware_in_fonts_folder.yml)
