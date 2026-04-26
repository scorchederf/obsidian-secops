---
sigma_id: "1883444f-084b-419b-ac62-e0d0c5b3693f"
title: "Suspicious Connection to Remote Account"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_susp_networkcredential.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_networkcredential.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "low"
logsource: "windows / ps_script"
aliases:
  - "1883444f-084b-419b-ac62-e0d0c5b3693f"
  - "Suspicious Connection to Remote Account"
attack_technique_ids:
  - "T1110.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Connection to Remote Account

Adversaries with no prior knowledge of legitimate credentials within the system or environment may guess passwords to attempt access to accounts.
Without knowledge of the password for an account, an adversary may opt to systematically guess the password using a repetitive or iterative mechanism

## Metadata

- Rule ID: 1883444f-084b-419b-ac62-e0d0c5b3693f
- Status: test
- Level: low
- Author: frack113
- Date: 2021-12-27
- Source Path: rules/windows/powershell/powershell_script/posh_ps_susp_networkcredential.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1110-brute_force|T1110.001]]

## Detection

```yaml
selection:
  ScriptBlockText|contains:
  - System.DirectoryServices.Protocols.LdapDirectoryIdentifier
  - System.Net.NetworkCredential
  - System.DirectoryServices.Protocols.LdapConnection
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1110.001/T1110.001.md#atomic-test-2---brute-force-credentials-of-single-active-directory-domain-user-via-ldap-against-domain-controller-ntlm-or-kerberos

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_networkcredential.yml)
