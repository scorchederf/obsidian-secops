---
sigma_id: "060c3ef1-fd0a-4091-bf46-e7d625f60b73"
title: "Suspicious Get-ADReplAccount"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_get_adreplaccount.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_get_adreplaccount.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "medium"
logsource: "windows / ps_script"
aliases:
  - "060c3ef1-fd0a-4091-bf46-e7d625f60b73"
  - "Suspicious Get-ADReplAccount"
attack_technique_ids:
  - "T1003.006"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Get-ADReplAccount

The DSInternals PowerShell Module exposes several internal features of Active Directory and Azure Active Directory.
These include FIDO2 and NGC key auditing, offline ntds.dit file manipulation, password auditing, DC recovery from IFM backups and password hash calculation.

## Metadata

- Rule ID: 060c3ef1-fd0a-4091-bf46-e7d625f60b73
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-02-06
- Source Path: rules/windows/powershell/powershell_script/posh_ps_get_adreplaccount.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.006]]

## Detection

```yaml
selection:
  ScriptBlockText|contains|all:
  - Get-ADReplAccount
  - '-All '
  - '-Server '
condition: selection
```

## False Positives

- Legitimate PowerShell scripts

## References

- https://www.powershellgallery.com/packages/DSInternals
- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1003.006/T1003.006.md#atomic-test-2---run-dsinternals-get-adreplaccount

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_get_adreplaccount.yml)
