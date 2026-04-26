---
sigma_id: "cdfa73b6-3c9d-4bb8-97f8-ddbd8921f5c5"
title: "Potential Unconstrained Delegation Discovery Via Get-ADComputer - ScriptBlock"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_potential_unconstrained_delegation_discovery.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_potential_unconstrained_delegation_discovery.yml"
build_date: "2026-04-26 14:14:33"
status: "experimental"
level: "medium"
logsource: "windows / ps_script"
aliases:
  - "cdfa73b6-3c9d-4bb8-97f8-ddbd8921f5c5"
  - "Potential Unconstrained Delegation Discovery Via Get-ADComputer - ScriptBlock"
attack_technique_ids:
  - "T1018"
  - "T1558"
  - "T1589.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Unconstrained Delegation Discovery Via Get-ADComputer - ScriptBlock

Detects the use of the "Get-ADComputer" cmdlet in order to identify systems which are configured for unconstrained delegation.

## Metadata

- Rule ID: cdfa73b6-3c9d-4bb8-97f8-ddbd8921f5c5
- Status: experimental
- Level: medium
- Author: frack113
- Date: 2025-03-05
- Source Path: rules/windows/powershell/powershell_script/posh_ps_potential_unconstrained_delegation_discovery.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enable
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1018-remote_system_discovery|T1018]]
- [[kb/attack/techniques/T1558-steal_or_forge_kerberos_tickets|T1558]]
- [[kb/attack/techniques/T1589-gather_victim_identity_information|T1589.002]]

## Detection

```yaml
selection:
  ScriptBlockText|contains:
  - -Properties*TrustedForDelegation
  - -Properties*TrustedToAuthForDelegation
  - -Properties*msDS-AllowedToDelegateTo
  - -Properties*PrincipalsAllowedToDelegateToAccount
  - -LDAPFilter*(userAccountControl:1.2.840.113556.1.4.803:=524288)
condition: selection
```

## False Positives

- Legitimate use of the library for administrative activity

## References

- https://pentestlab.blog/2022/03/21/unconstrained-delegation/
- https://learn.microsoft.com/en-us/powershell/module/activedirectory/get-adcomputer?view=windowsserver2022-ps

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_potential_unconstrained_delegation_discovery.yml)
