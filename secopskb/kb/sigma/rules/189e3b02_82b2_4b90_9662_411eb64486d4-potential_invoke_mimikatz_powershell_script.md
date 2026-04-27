---
sigma_id: "189e3b02-82b2-4b90-9662-411eb64486d4"
title: "Potential Invoke-Mimikatz PowerShell Script"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_potential_invoke_mimikatz.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_potential_invoke_mimikatz.yml"
build_date: "2026-04-26 17:03:20"
status: "test"
level: "high"
logsource: "windows / ps_script"
aliases:
  - "189e3b02-82b2-4b90-9662-411eb64486d4"
  - "Potential Invoke-Mimikatz PowerShell Script"
attack_technique_ids:
  - "T1003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Potential Invoke-Mimikatz PowerShell Script

Detects Invoke-Mimikatz PowerShell script and alike. Mimikatz is a credential dumper capable of obtaining plaintext Windows account logins and passwords.

## Metadata

- Rule ID: 189e3b02-82b2-4b90-9662-411eb64486d4
- Status: test
- Level: high
- Author: Tim Rauch, Elastic (idea)
- Date: 2022-09-28
- Source Path: rules/windows/powershell/powershell_script/posh_ps_potential_invoke_mimikatz.yml

## Logsource

- category: ps_script
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003]]

## Detection

```yaml
selection_1:
  ScriptBlockText|contains|all:
  - DumpCreds
  - DumpCerts
selection_2:
  ScriptBlockText|contains: sekurlsa::logonpasswords
selection_3:
  ScriptBlockText|contains|all:
  - crypto::certificates
  - CERT_SYSTEM_STORE_LOCAL_MACHINE
condition: 1 of selection*
```

## False Positives

- Mimikatz can be useful for testing the security of networks

## References

- https://www.elastic.co/guide/en/security/current/potential-invoke-mimikatz-powershell-script.html#potential-invoke-mimikatz-powershell-script

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_potential_invoke_mimikatz.yml)
