---
sigma_id: "db92dd33-a3ad-49cf-8c2c-608c3e30ace0"
title: "Invoke-Obfuscation Via Use Clip - Powershell"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_invoke_obfuscation_via_use_clip.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_invoke_obfuscation_via_use_clip.yml"
build_date: "2026-04-27 19:13:52"
status: "test"
level: "high"
logsource: "windows / ps_script"
aliases:
  - "db92dd33-a3ad-49cf-8c2c-608c3e30ace0"
  - "Invoke-Obfuscation Via Use Clip - Powershell"
attack_technique_ids:
  - "T1027"
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects Obfuscated Powershell via use Clip.exe in Scripts

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1027-obfuscated_files_or_information|T1027: Obfuscated Files or Information]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter#^t1059001-powershell|T1059.001: PowerShell]]

## Detection

```yaml
selection_4104:
  ScriptBlockText|re: (?i)echo.*clip.*&&.*(Clipboard|i`?n`?v`?o`?k`?e`?)
condition: selection_4104
```

## False Positives

- Unknown

## References

- https://github.com/SigmaHQ/sigma/issues/1009

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_invoke_obfuscation_via_use_clip.yml)
