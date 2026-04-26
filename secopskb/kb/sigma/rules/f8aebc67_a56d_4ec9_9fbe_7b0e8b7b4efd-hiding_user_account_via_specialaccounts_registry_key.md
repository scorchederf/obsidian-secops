---
sigma_id: "f8aebc67-a56d-4ec9-9fbe-7b0e8b7b4efd"
title: "Hiding User Account Via SpecialAccounts Registry Key"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_special_accounts.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_special_accounts.yml"
build_date: "2026-04-26 15:01:45"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "f8aebc67-a56d-4ec9-9fbe-7b0e8b7b4efd"
  - "Hiding User Account Via SpecialAccounts Registry Key"
attack_technique_ids:
  - "T1564.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Hiding User Account Via SpecialAccounts Registry Key

Detects modifications to the registry key "HKLM\Software\Microsoft\Windows NT\CurrentVersion\Winlogon\SpecialAccounts\Userlist" where the value is set to "0" in order to hide user account from being listed on the logon screen.

## Metadata

- Rule ID: f8aebc67-a56d-4ec9-9fbe-7b0e8b7b4efd
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems), frack113
- Date: 2022-07-12
- Modified: 2023-01-26
- Source Path: rules/windows/registry/registry_set/registry_set_special_accounts.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1564-hide_artifacts|T1564.002]]

## Detection

```yaml
selection:
  TargetObject|contains: \SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\SpecialAccounts\UserList
  Details: DWORD (0x00000000)
condition: selection
```

## False Positives

- Unknown

## Simulation

### Create Hidden User in Registry

- Atomic Test: [[kb/atomic/tests/173126b7_afe4_45eb_8680_fa9f6400431c-create_hidden_user_in_registry|173126b7-afe4-45eb-8680-fa9f6400431c]]
- atomic_guid: 173126b7-afe4-45eb-8680-fa9f6400431c
- name: Create Hidden User in Registry
- technique: T1564.002
- type: atomic-red-team

## References

- https://thedfirreport.com/2022/07/11/select-xmrig-from-sqlserver/
- https://github.com/redcanaryco/atomic-red-team/blob/40b77d63808dd4f4eafb83949805636735a1fd15/atomics/T1564.002/T1564.002.md#atomic-test-3---create-hidden-user-in-registry

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_special_accounts.yml)
