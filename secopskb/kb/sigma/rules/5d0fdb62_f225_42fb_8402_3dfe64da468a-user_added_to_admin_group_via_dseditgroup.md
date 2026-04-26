---
sigma_id: "5d0fdb62-f225-42fb-8402-3dfe64da468a"
title: "User Added To Admin Group Via DseditGroup"
framework: "sigma"
generated: "true"
source_path: "rules/macos/process_creation/proc_creation_macos_dseditgroup_add_to_admin_group.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_dseditgroup_add_to_admin_group.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "macos / process_creation"
aliases:
  - "5d0fdb62-f225-42fb-8402-3dfe64da468a"
  - "User Added To Admin Group Via DseditGroup"
attack_technique_ids:
  - "T1078.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# User Added To Admin Group Via DseditGroup

Detects attempts to create and/or add an account to the admin group, thus granting admin privileges.

## Metadata

- Rule ID: 5d0fdb62-f225-42fb-8402-3dfe64da468a
- Status: test
- Level: medium
- Author: Sohan G (D4rkCiph3r)
- Date: 2023-08-22
- Source Path: rules/macos/process_creation/proc_creation_macos_dseditgroup_add_to_admin_group.yml

## Logsource

- category: process_creation
- product: macos

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1078-valid_accounts|T1078.003]]

## Detection

```yaml
selection:
  Image|endswith: /dseditgroup
  CommandLine|contains|all:
  - ' -o edit '
  - ' -a '
  - ' -t user'
  - admin
condition: selection
```

## False Positives

- Legitimate administration activities

## References

- https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1078.003/T1078.003.md#atomic-test-5---add-a-newexisting-user-to-the-admin-group-using-dseditgroup-utility---macos
- https://ss64.com/osx/dseditgroup.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_dseditgroup_add_to_admin_group.yml)
