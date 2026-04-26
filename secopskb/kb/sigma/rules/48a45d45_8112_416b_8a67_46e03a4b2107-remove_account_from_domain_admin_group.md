---
sigma_id: "48a45d45-8112-416b-8a67-46e03a4b2107"
title: "Remove Account From Domain Admin Group"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_susp_remove_adgroupmember.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_remove_adgroupmember.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "medium"
logsource: "windows / ps_script"
aliases:
  - "48a45d45-8112-416b-8a67-46e03a4b2107"
  - "Remove Account From Domain Admin Group"
attack_technique_ids:
  - "T1531"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Remove Account From Domain Admin Group

Adversaries may interrupt availability of system and network resources by inhibiting access to accounts utilized by legitimate users.
Accounts may be deleted, locked, or manipulated (ex: changed credentials) to remove access to accounts.

## Metadata

- Rule ID: 48a45d45-8112-416b-8a67-46e03a4b2107
- Status: test
- Level: medium
- Author: frack113
- Date: 2021-12-26
- Source Path: rules/windows/powershell/powershell_script/posh_ps_susp_remove_adgroupmember.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1531-account_access_removal|T1531]]

## Detection

```yaml
selection:
  ScriptBlockText|contains|all:
  - Remove-ADGroupMember
  - '-Identity '
  - '-Members '
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1531/T1531.md#atomic-test-3---remove-account-from-domain-admin-group

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_remove_adgroupmember.yml)
