---
sigma_id: "88f680b8-070e-402c-ae11-d2914f2257f1"
title: "PowerShell Base64 Encoded IEX Cmdlet"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_base64_iex.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_base64_iex.yml"
build_date: "2026-04-26 17:03:21"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "88f680b8-070e-402c-ae11-d2914f2257f1"
  - "PowerShell Base64 Encoded IEX Cmdlet"
attack_technique_ids:
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# PowerShell Base64 Encoded IEX Cmdlet

Detects usage of a base64 encoded "IEX" cmdlet in a process command line

## Metadata

- Rule ID: 88f680b8-070e-402c-ae11-d2914f2257f1
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2019-08-23
- Modified: 2023-04-06
- Source Path: rules/windows/process_creation/proc_creation_win_powershell_base64_iex.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]

## Detection

```yaml
selection:
- CommandLine|base64offset|contains:
  - IEX ([
  - iex ([
  - iex (New
  - IEX (New
  - IEX([
  - iex([
  - iex(New
  - IEX(New
  - IEX(('
  - iex(('
- CommandLine|contains:
  - SQBFAFgAIAAoAFsA
  - kARQBYACAAKABbA
  - JAEUAWAAgACgAWw
  - aQBlAHgAIAAoAFsA
  - kAZQB4ACAAKABbA
  - pAGUAeAAgACgAWw
  - aQBlAHgAIAAoAE4AZQB3A
  - kAZQB4ACAAKABOAGUAdw
  - pAGUAeAAgACgATgBlAHcA
  - SQBFAFgAIAAoAE4AZQB3A
  - kARQBYACAAKABOAGUAdw
  - JAEUAWAAgACgATgBlAHcA
condition: selection
```

## False Positives

- Unknown

## References

- Internal Research

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_base64_iex.yml)
