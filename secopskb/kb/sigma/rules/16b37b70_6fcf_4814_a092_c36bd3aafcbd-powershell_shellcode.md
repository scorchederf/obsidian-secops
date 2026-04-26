---
sigma_id: "16b37b70-6fcf-4814-a092-c36bd3aafcbd"
title: "PowerShell ShellCode"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_shellcode_b64.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_shellcode_b64.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "high"
logsource: "windows / ps_script"
aliases:
  - "16b37b70-6fcf-4814-a092-c36bd3aafcbd"
  - "PowerShell ShellCode"
attack_technique_ids:
  - "T1055"
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# PowerShell ShellCode

Detects Base64 encoded Shellcode

## Metadata

- Rule ID: 16b37b70-6fcf-4814-a092-c36bd3aafcbd
- Status: test
- Level: high
- Author: David Ledbetter (shellcode), Florian Roth (Nextron Systems)
- Date: 2018-11-17
- Modified: 2024-01-25
- Source Path: rules/windows/powershell/powershell_script/posh_ps_shellcode_b64.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1055-process_injection|T1055]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.001]]

## Detection

```yaml
selection:
  ScriptBlockText|contains:
  - OiCAAAAYInlM
  - OiJAAAAYInlM
condition: selection
```

## False Positives

- Unknown

## References

- https://twitter.com/cyb3rops/status/1063072865992523776

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_shellcode_b64.yml)
