---
sigma_id: "f4264e47-f522-4c38-a420-04525d5b880f"
title: "Renamed AutoIt Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_renamed_autoit.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_renamed_autoit.yml"
build_date: "2026-04-26 17:03:22"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "f4264e47-f522-4c38-a420-04525d5b880f"
  - "Renamed AutoIt Execution"
attack_technique_ids:
  - "T1027"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Renamed AutoIt Execution

Detects the execution of a renamed AutoIt2.exe or AutoIt3.exe.
AutoIt is a scripting language and automation tool for Windows systems. While primarily used for legitimate automation tasks, it can be misused in cyber attacks.
Attackers can leverage AutoIt to create and distribute malware, including keyloggers, spyware, and botnets. A renamed AutoIt executable is particularly suspicious.

## Metadata

- Rule ID: f4264e47-f522-4c38-a420-04525d5b880f
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2023-06-04
- Modified: 2024-11-23
- Source Path: rules/windows/process_creation/proc_creation_win_renamed_autoit.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1027-obfuscated_files_or_information|T1027]]

## Detection

```yaml
selection_1:
  CommandLine|contains:
  - ' /AutoIt3ExecuteScript'
  - ' /ErrorStdOut'
selection_2:
  Hashes|contains:
  - IMPHASH=FDC554B3A8683918D731685855683DDF
  - IMPHASH=CD30A61B60B3D60CECDB034C8C83C290
  - IMPHASH=F8A00C72F2D667D2EDBB234D0C0AE000
selection_3:
  OriginalFileName:
  - AutoIt3.exe
  - AutoIt2.exe
  - AutoIt.exe
filter_main_legit_name:
  Image|endswith:
  - \AutoIt.exe
  - \AutoIt2.exe
  - \AutoIt3_x64.exe
  - \AutoIt3.exe
condition: 1 of selection_* and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://twitter.com/malmoeb/status/1665463817130725378?s=12&t=C0_T_re0wRP_NfKa27Xw9w
- https://www.autoitscript.com/site/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_renamed_autoit.yml)
