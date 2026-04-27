---
sigma_id: "84c174ab-d3ef-481f-9c86-a50d0b8e3edb"
title: "PowerShell Get-Process LSASS in ScriptBlock"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_susp_getprocess_lsass.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_getprocess_lsass.yml"
build_date: "2026-04-27 19:13:55"
status: "test"
level: "high"
logsource: "windows / ps_script"
aliases:
  - "84c174ab-d3ef-481f-9c86-a50d0b8e3edb"
  - "PowerShell Get-Process LSASS in ScriptBlock"
attack_technique_ids:
  - "T1003.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects a Get-Process command on lsass process, which is in almost all cases a sign of malicious activity

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping#^t1003001-lsass-memory|T1003.001: LSASS Memory]]

## Detection

```yaml
selection:
  ScriptBlockText|contains: Get-Process lsass
condition: selection
```

## False Positives

- Legitimate certificate exports invoked by administrators or users (depends on processes in the environment - filter if unusable)

## References

- https://web.archive.org/web/20220205033028/https://twitter.com/PythonResponder/status/1385064506049630211

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_getprocess_lsass.yml)
