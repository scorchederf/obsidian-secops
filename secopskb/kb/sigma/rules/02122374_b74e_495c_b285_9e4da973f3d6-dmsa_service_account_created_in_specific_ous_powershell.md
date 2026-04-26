---
sigma_id: "02122374-b74e-495c-b285-9e4da973f3d6"
title: "DMSA Service Account Created in Specific OUs - PowerShell"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_create_new_dmsasvc_account.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_create_new_dmsasvc_account.yml"
build_date: "2026-04-26 14:14:23"
status: "experimental"
level: "medium"
logsource: "windows / ps_script"
aliases:
  - "02122374-b74e-495c-b285-9e4da973f3d6"
  - "DMSA Service Account Created in Specific OUs - PowerShell"
attack_technique_ids:
  - "T1078.002"
  - "T1098"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# DMSA Service Account Created in Specific OUs - PowerShell

Detects the creation of a dMSA service account using the New-ADServiceAccount cmdlet in certain OUs.
The fact that the cmdlet is used to create a dMSASvc account in a specific OU is highly suspicious.
It is a pattern trying to exploit the BadSuccessor privilege escalation vulnerability in Windows Server 2025.
On top of that, if the user that is creating the dMSASvc account is not a legitimate administrator or does not have the necessary permissions,
it is a strong signal of an attempted or successful abuse of the BaDSuccessor vulnerability for privilege escalation within the Windows Server 2025 Active Directory environment.

## Metadata

- Rule ID: 02122374-b74e-495c-b285-9e4da973f3d6
- Status: experimental
- Level: medium
- Author: Swachchhanda Shrawan Poudel (Nextron Systems)
- Date: 2025-05-24
- Source Path: rules/windows/powershell/powershell_script/posh_ps_create_new_dmsasvc_account.yml

## Logsource

- category: ps_script
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1078-valid_accounts|T1078.002]]
- [[kb/attack/techniques/T1098-account_manipulation|T1098]]

## Detection

```yaml
selection:
  ScriptBlockText|contains|all:
  - New-ADServiceAccount
  - -CreateDelegatedServiceAccount
  - -path
condition: selection
```

## False Positives

- Unknown

## References

- https://www.akamai.com/blog/security-research/abusing-bad-successor-for-privilege-escalation-in-active-directory

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_create_new_dmsasvc_account.yml)
