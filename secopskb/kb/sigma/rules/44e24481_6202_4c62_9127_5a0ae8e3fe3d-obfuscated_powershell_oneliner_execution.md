---
sigma_id: "44e24481-6202-4c62-9127-5a0ae8e3fe3d"
title: "Obfuscated PowerShell OneLiner Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_download_cradle_obfuscated.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_download_cradle_obfuscated.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "44e24481-6202-4c62-9127-5a0ae8e3fe3d"
  - "Obfuscated PowerShell OneLiner Execution"
attack_technique_ids:
  - "T1059.001"
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Obfuscated PowerShell OneLiner Execution

Detects the execution of a specific OneLiner to download and execute powershell modules in memory.

## Metadata

- Rule ID: 44e24481-6202-4c62-9127-5a0ae8e3fe3d
- Status: test
- Level: high
- Author: @Kostastsale, TheDFIRReport
- Date: 2022-05-09
- Modified: 2025-04-16
- Source Path: rules/windows/process_creation/proc_creation_win_powershell_download_cradle_obfuscated.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]
- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Detection

```yaml
selection:
  Image|endswith: \powershell.exe
  CommandLine|contains|all:
  - http://127.0.0.1
  - '%{(IRM $_)}'
  - Invoke
condition: selection
```

## False Positives

- Unknown

## References

- https://thedfirreport.com/2022/05/09/seo-poisoning-a-gootloader-story/
- https://gist.github.com/mgeeky/3b11169ab77a7de354f4111aa2f0df38

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_download_cradle_obfuscated.yml)
