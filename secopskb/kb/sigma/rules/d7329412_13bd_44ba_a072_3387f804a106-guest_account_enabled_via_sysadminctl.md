---
sigma_id: "d7329412-13bd-44ba-a072-3387f804a106"
title: "Guest Account Enabled Via Sysadminctl"
framework: "sigma"
generated: "true"
source_path: "rules/macos/process_creation/proc_creation_macos_sysadminctl_enable_guest_account.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_sysadminctl_enable_guest_account.yml"
build_date: "2026-04-26 14:14:26"
status: "test"
level: "low"
logsource: "macos / process_creation"
aliases:
  - "d7329412-13bd-44ba-a072-3387f804a106"
  - "Guest Account Enabled Via Sysadminctl"
attack_technique_ids:
  - "T1078"
  - "T1078.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Guest Account Enabled Via Sysadminctl

Detects attempts to enable the guest account using the sysadminctl utility

## Metadata

- Rule ID: d7329412-13bd-44ba-a072-3387f804a106
- Status: test
- Level: low
- Author: Sohan G (D4rkCiph3r)
- Date: 2023-02-18
- Source Path: rules/macos/process_creation/proc_creation_macos_sysadminctl_enable_guest_account.yml

## Logsource

- category: process_creation
- product: macos

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1078-valid_accounts|T1078]]
- [[kb/attack/techniques/T1078-valid_accounts|T1078.001]]

## Detection

```yaml
selection:
  Image|endswith: /sysadminctl
  CommandLine|contains|all:
  - ' -guestAccount'
  - ' on'
condition: selection
```

## False Positives

- Unknown

## References

- https://ss64.com/osx/sysadminctl.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_sysadminctl_enable_guest_account.yml)
