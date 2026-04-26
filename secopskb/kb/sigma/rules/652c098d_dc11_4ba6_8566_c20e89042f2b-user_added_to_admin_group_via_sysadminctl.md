---
sigma_id: "652c098d-dc11-4ba6-8566-c20e89042f2b"
title: "User Added To Admin Group Via Sysadminctl"
framework: "sigma"
generated: "true"
source_path: "rules/macos/process_creation/proc_creation_macos_sysadminctl_add_user_to_admin_group.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_sysadminctl_add_user_to_admin_group.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "macos / process_creation"
aliases:
  - "652c098d-dc11-4ba6-8566-c20e89042f2b"
  - "User Added To Admin Group Via Sysadminctl"
attack_technique_ids:
  - "T1078.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# User Added To Admin Group Via Sysadminctl

Detects attempts to create and add an account to the admin group via "sysadminctl"

## Metadata

- Rule ID: 652c098d-dc11-4ba6-8566-c20e89042f2b
- Status: test
- Level: medium
- Author: Sohan G (D4rkCiph3r)
- Date: 2023-03-19
- Source Path: rules/macos/process_creation/proc_creation_macos_sysadminctl_add_user_to_admin_group.yml

## Logsource

- category: process_creation
- product: macos

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1078-valid_accounts|T1078.003]]

## Detection

```yaml
selection:
  Image|endswith: /sysadminctl
  CommandLine|contains|all:
  - ' -addUser '
  - ' -admin '
condition: selection
```

## False Positives

- Legitimate administration activities

## References

- https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1078.003/T1078.003.md#atomic-test-3---create-local-account-with-admin-privileges-using-sysadminctl-utility---macos
- https://ss64.com/osx/sysadminctl.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_sysadminctl_add_user_to_admin_group.yml)
