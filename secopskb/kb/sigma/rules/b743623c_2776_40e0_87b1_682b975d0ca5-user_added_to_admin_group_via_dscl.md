---
sigma_id: "b743623c-2776-40e0-87b1-682b975d0ca5"
title: "User Added To Admin Group Via Dscl"
framework: "sigma"
generated: "true"
source_path: "rules/macos/process_creation/proc_creation_macos_dscl_add_user_to_admin_group.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_dscl_add_user_to_admin_group.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "macos / process_creation"
aliases:
  - "b743623c-2776-40e0-87b1-682b975d0ca5"
  - "User Added To Admin Group Via Dscl"
attack_technique_ids:
  - "T1078.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# User Added To Admin Group Via Dscl

Detects attempts to create and add an account to the admin group via "dscl"

## Metadata

- Rule ID: b743623c-2776-40e0-87b1-682b975d0ca5
- Status: test
- Level: medium
- Author: Sohan G (D4rkCiph3r)
- Date: 2023-03-19
- Source Path: rules/macos/process_creation/proc_creation_macos_dscl_add_user_to_admin_group.yml

## Logsource

- category: process_creation
- product: macos

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1078-valid_accounts|T1078.003]]

## Detection

```yaml
selection:
  Image|endswith: /dscl
  CommandLine|contains|all:
  - ' -append '
  - ' /Groups/admin '
  - ' GroupMembership '
condition: selection
```

## False Positives

- Legitimate administration activities

## References

- https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1078.003/T1078.003.md#atomic-test-2---create-local-account-with-admin-privileges---macos
- https://ss64.com/osx/dscl.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_dscl_add_user_to_admin_group.yml)
