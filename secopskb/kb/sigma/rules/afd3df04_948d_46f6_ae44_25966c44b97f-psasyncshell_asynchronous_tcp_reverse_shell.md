---
sigma_id: "afd3df04-948d-46f6-ae44-25966c44b97f"
title: "PSAsyncShell - Asynchronous TCP Reverse Shell"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_psasyncshell.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_psasyncshell.yml"
build_date: "2026-04-26 17:03:20"
status: "test"
level: "high"
logsource: "windows / ps_script"
aliases:
  - "afd3df04-948d-46f6-ae44-25966c44b97f"
  - "PSAsyncShell - Asynchronous TCP Reverse Shell"
attack_technique_ids:
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# PSAsyncShell - Asynchronous TCP Reverse Shell

Detects the use of PSAsyncShell an Asynchronous TCP Reverse Shell written in powershell

## Metadata

- Rule ID: afd3df04-948d-46f6-ae44-25966c44b97f
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-10-04
- Source Path: rules/windows/powershell/powershell_script/posh_ps_psasyncshell.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]

## Detection

```yaml
selection:
  ScriptBlockText|contains: PSAsyncShell
condition: selection
```

## False Positives

- Unlikely

## References

- https://github.com/JoelGMSec/PSAsyncShell

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_psasyncshell.yml)
