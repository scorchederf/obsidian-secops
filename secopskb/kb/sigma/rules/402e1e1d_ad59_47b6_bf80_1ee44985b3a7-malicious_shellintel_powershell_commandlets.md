---
sigma_id: "402e1e1d-ad59-47b6-bf80-1ee44985b3a7"
title: "Malicious ShellIntel PowerShell Commandlets"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_shellintel_malicious_commandlets.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_shellintel_malicious_commandlets.yml"
build_date: "2026-04-27 19:13:52"
status: "test"
level: "high"
logsource: "windows / ps_script"
aliases:
  - "402e1e1d-ad59-47b6-bf80-1ee44985b3a7"
  - "Malicious ShellIntel PowerShell Commandlets"
attack_technique_ids:
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects Commandlet names from ShellIntel exploitation scripts.

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter#^t1059001-powershell|T1059.001: PowerShell]]

## Detection

```yaml
selection:
  ScriptBlockText|contains:
  - Invoke-SMBAutoBrute
  - Invoke-GPOLinks
  - Invoke-Potato
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/Shellntel/scripts/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_shellintel_malicious_commandlets.yml)
