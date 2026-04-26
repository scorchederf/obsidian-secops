---
sigma_id: "bbb9495b-58fc-4016-b9df-9a3a1b67ca82"
title: "Password Policy Discovery With Get-AdDefaultDomainPasswordPolicy"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_susp_get_addefaultdomainpasswordpolicy.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_get_addefaultdomainpasswordpolicy.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "low"
logsource: "windows / ps_script"
aliases:
  - "bbb9495b-58fc-4016-b9df-9a3a1b67ca82"
  - "Password Policy Discovery With Get-AdDefaultDomainPasswordPolicy"
attack_technique_ids:
  - "T1201"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Password Policy Discovery With Get-AdDefaultDomainPasswordPolicy

Detetcts PowerShell activity in which Get-Addefaultdomainpasswordpolicy is used to get the default password policy for an Active Directory domain.

## Metadata

- Rule ID: bbb9495b-58fc-4016-b9df-9a3a1b67ca82
- Status: test
- Level: low
- Author: frack113
- Date: 2022-03-17
- Source Path: rules/windows/powershell/powershell_script/posh_ps_susp_get_addefaultdomainpasswordpolicy.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1201-password_policy_discovery|T1201]]

## Detection

```yaml
selection:
  ScriptBlockText|contains: Get-AdDefaultDomainPasswordPolicy
condition: selection
```

## False Positives

- Legitimate PowerShell scripts

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1201/T1201.md#atomic-test-9---enumerate-active-directory-password-policy-with-get-addefaultdomainpasswordpolicy
- https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-addefaultdomainpasswordpolicy?view=windowsserver2022-ps

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_get_addefaultdomainpasswordpolicy.yml)
