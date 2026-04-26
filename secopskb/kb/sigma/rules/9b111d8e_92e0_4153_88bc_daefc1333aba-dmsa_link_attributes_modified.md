---
sigma_id: "9b111d8e-92e0-4153-88bc-daefc1333aba"
title: "DMSA Link Attributes Modified"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_modification_of_dmsa_link_attribute.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_modification_of_dmsa_link_attribute.yml"
build_date: "2026-04-26 14:14:23"
status: "experimental"
level: "low"
logsource: "windows / ps_script"
aliases:
  - "9b111d8e-92e0-4153-88bc-daefc1333aba"
  - "DMSA Link Attributes Modified"
attack_technique_ids:
  - "T1078.002"
  - "T1098"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# DMSA Link Attributes Modified

Detects modification of dMSA link attributes (msDS-ManagedAccountPrecededByLink) via PowerShell scripts.
This command line pattern could be an indicator an attempt to exploit the BadSuccessor privilege escalation vulnerability in Windows Server 2025.

## Metadata

- Rule ID: 9b111d8e-92e0-4153-88bc-daefc1333aba
- Status: experimental
- Level: low
- Author: Swachchhanda Shrawan Poudel (Nextron Systems)
- Date: 2025-05-24
- Source Path: rules/windows/powershell/powershell_script/posh_ps_modification_of_dmsa_link_attribute.yml

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
  - .Put("msDS-ManagedAccountPrecededByLink
  - CN=
condition: selection
```

## False Positives

- Legitimate administrative tasks modifying these attributes.

## References

- https://www.akamai.com/blog/security-research/abusing-bad-successor-for-privilege-escalation-in-active-directory

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_modification_of_dmsa_link_attribute.yml)
