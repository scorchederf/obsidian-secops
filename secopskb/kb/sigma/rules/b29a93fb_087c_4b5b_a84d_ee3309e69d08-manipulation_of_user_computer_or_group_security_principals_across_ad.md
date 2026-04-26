---
sigma_id: "b29a93fb-087c-4b5b-a84d-ee3309e69d08"
title: "Manipulation of User Computer or Group Security Principals Across AD"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_directoryservices_accountmanagement.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_directoryservices_accountmanagement.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "medium"
logsource: "windows / ps_script"
aliases:
  - "b29a93fb-087c-4b5b-a84d-ee3309e69d08"
  - "Manipulation of User Computer or Group Security Principals Across AD"
attack_technique_ids:
  - "T1136.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Manipulation of User Computer or Group Security Principals Across AD

Adversaries may create a domain account to maintain access to victim systems.
Domain accounts are those managed by Active Directory Domain Services where access and permissions are configured across systems and services that are part of that domain..

## Metadata

- Rule ID: b29a93fb-087c-4b5b-a84d-ee3309e69d08
- Status: test
- Level: medium
- Author: frack113
- Date: 2021-12-28
- Source Path: rules/windows/powershell/powershell_script/posh_ps_directoryservices_accountmanagement.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1136-create_account|T1136.002]]

## Detection

```yaml
selection:
  ScriptBlockText|contains: System.DirectoryServices.AccountManagement
condition: selection
```

## False Positives

- Legitimate administrative script

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1136.002/T1136.002.md#atomic-test-3---create-a-new-domain-account-using-powershell
- https://learn.microsoft.com/en-us/dotnet/api/system.directoryservices.accountmanagement?view=net-8.0

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_directoryservices_accountmanagement.yml)
