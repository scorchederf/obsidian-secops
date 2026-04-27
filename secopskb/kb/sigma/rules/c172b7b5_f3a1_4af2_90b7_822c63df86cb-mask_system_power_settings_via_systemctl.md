---
sigma_id: "c172b7b5-f3a1-4af2-90b7-822c63df86cb"
title: "Mask System Power Settings Via Systemctl"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_systemctl_mask_power_settings.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_systemctl_mask_power_settings.yml"
build_date: "2026-04-26 17:03:20"
status: "experimental"
level: "high"
logsource: "linux / process_creation"
aliases:
  - "c172b7b5-f3a1-4af2-90b7-822c63df86cb"
  - "Mask System Power Settings Via Systemctl"
attack_technique_ids:
  - "T1653"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Mask System Power Settings Via Systemctl

Detects the use of systemctl mask to disable system power management targets such as suspend, hibernate, or hybrid sleep.
Adversaries may mask these targets to prevent a system from entering sleep or shutdown states, ensuring their malicious processes remain active and uninterrupted.
This behavior can be associated with persistence or defense evasion, as it impairs normal system power operations to maintain long-term access or avoid termination of malicious activity.

## Metadata

- Rule ID: c172b7b5-f3a1-4af2-90b7-822c63df86cb
- Status: experimental
- Level: high
- Author: Milad Cheraghi, Nasreddine Bencherchali
- Date: 2025-10-17
- Source Path: rules/linux/process_creation/proc_creation_lnx_systemctl_mask_power_settings.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1653-power_settings|T1653]]

## Detection

```yaml
selection_systemctl:
  Image|endswith: /systemctl
  CommandLine|contains: ' mask'
selection_power_options:
  CommandLine|contains:
  - suspend.target
  - hibernate.target
  - hybrid-sleep.target
condition: all of selection_*
```

## False Positives

- Unlikely

## References

- https://www.man7.org/linux/man-pages/man1/systemctl.1.html
- https://linux-audit.com/systemd/faq/what-is-the-difference-between-systemctl-disable-and-systemctl-mask/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_systemctl_mask_power_settings.yml)
