---
sigma_id: "bf72941a-cba0-41ea-b18c-9aca3925690d"
title: "PowerShell ADRecon Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_adrecon_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_adrecon_execution.yml"
build_date: "2026-04-27 19:13:54"
status: "test"
level: "high"
logsource: "windows / ps_script"
aliases:
  - "bf72941a-cba0-41ea-b18c-9aca3925690d"
  - "PowerShell ADRecon Execution"
attack_technique_ids:
  - "T1059.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects execution of ADRecon.ps1 for AD reconnaissance which has been reported to be actively used by FIN7

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
  - Function Get-ADRExcelComOb
  - Get-ADRGPO
  - Get-ADRDomainController
  - ADRecon-Report.xlsx
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/sense-of-security/ADRecon/blob/11881a24e9c8b207f31b56846809ce1fb189bcc9/ADRecon.ps1
- https://bi-zone.medium.com/from-pentest-to-apt-attack-cybercriminal-group-fin7-disguises-its-malware-as-an-ethical-hackers-c23c9a75e319

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_adrecon_execution.yml)
