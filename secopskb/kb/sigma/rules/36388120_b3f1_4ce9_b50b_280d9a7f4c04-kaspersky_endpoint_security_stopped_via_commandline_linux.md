---
sigma_id: "36388120-b3f1-4ce9-b50b-280d9a7f4c04"
title: "Kaspersky Endpoint Security Stopped Via CommandLine - Linux"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_av_kaspersky_av_disabled.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_av_kaspersky_av_disabled.yml"
build_date: "2026-04-26 17:03:19"
status: "experimental"
level: "high"
logsource: "linux / process_creation"
aliases:
  - "36388120-b3f1-4ce9-b50b-280d9a7f4c04"
  - "Kaspersky Endpoint Security Stopped Via CommandLine - Linux"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Kaspersky Endpoint Security Stopped Via CommandLine - Linux

Detects execution of the Kaspersky init.d stop script on Linux systems either directly or via systemctl.
This activity may indicate a manual interruption of the antivirus service by an administrator, or it could be a sign of potential tampering or evasion attempts by malicious actors.

## Metadata

- Rule ID: 36388120-b3f1-4ce9-b50b-280d9a7f4c04
- Status: experimental
- Level: high
- Author: Milad Cheraghi
- Date: 2025-10-18
- Source Path: rules/linux/process_creation/proc_creation_lnx_av_kaspersky_av_disabled.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Detection

```yaml
selection:
  Image|endswith:
  - /systemctl
  - /bash
  - /sh
  CommandLine|contains|all:
  - stop
  - kesl
condition: selection
```

## False Positives

- System administrator manually stopping Kaspersky services

## References

- https://support.kaspersky.com/KES4Linux/12.0.0/en-US/197929.htm

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_av_kaspersky_av_disabled.yml)
