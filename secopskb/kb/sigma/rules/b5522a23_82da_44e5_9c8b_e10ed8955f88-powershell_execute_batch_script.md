---
sigma_id: "b5522a23-82da-44e5-9c8b-e10ed8955f88"
title: "Powershell Execute Batch Script"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_susp_execute_batch_script.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_execute_batch_script.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "medium"
logsource: "windows / ps_script"
aliases:
  - "b5522a23-82da-44e5-9c8b-e10ed8955f88"
  - "Powershell Execute Batch Script"
attack_technique_ids:
  - "T1059.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Powershell Execute Batch Script

Adversaries may abuse the Windows command shell for execution.
The Windows command shell ([cmd](https://attack.mitre.org/software/S0106)) is the primary command prompt on Windows systems.
The Windows command prompt can be used to control almost any aspect of a system, with various permission levels required for different subsets of commands.
Batch files (ex: .bat or .cmd) also provide the shell with a list of sequential commands to run, as well as normal scripting operations such as conditionals and loops.
Common uses of batch files include long or repetitive tasks, or the need to run the same set of commands on multiple system

## Metadata

- Rule ID: b5522a23-82da-44e5-9c8b-e10ed8955f88
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-01-02
- Source Path: rules/windows/powershell/powershell_script/posh_ps_susp_execute_batch_script.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.003]]

## Detection

```yaml
selection_start:
  ScriptBlockText|contains: Start-Process
selection_batch:
  ScriptBlockText|contains:
  - .cmd
  - .bat
condition: all of selection_*
```

## False Positives

- Legitimate administration script

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1059.003/T1059.003.md#atomic-test-1---create-and-execute-batch-script

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_execute_batch_script.yml)
