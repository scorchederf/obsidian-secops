---
sigma_id: "16b37b70-6fcf-4814-a092-c36bd3aafcbd"
title: "PowerShell ShellCode"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_shellcode_b64.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_shellcode_b64.yml"
build_date: "2026-04-27 19:13:55"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects Base64 encoded Shellcode

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1055-process_injection|T1055: Process Injection]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter#^t1059001-powershell|T1059.001: PowerShell]]

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
