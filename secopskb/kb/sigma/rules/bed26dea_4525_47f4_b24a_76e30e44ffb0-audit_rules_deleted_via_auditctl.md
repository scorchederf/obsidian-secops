---
sigma_id: "bed26dea-4525-47f4-b24a-76e30e44ffb0"
title: "Audit Rules Deleted Via Auditctl"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_auditctl_clear_rules.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_auditctl_clear_rules.yml"
build_date: "2026-04-26 17:03:18"
status: "experimental"
level: "high"
logsource: "linux / process_creation"
aliases:
  - "bed26dea-4525-47f4-b24a-76e30e44ffb0"
  - "Audit Rules Deleted Via Auditctl"
attack_technique_ids:
  - "T1562.012"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Audit Rules Deleted Via Auditctl

Detects the execution of 'auditctl' with the '-D' command line parameter, which deletes all configured audit rules and watches on Linux systems.
This technique is commonly used by attackers to disable audit logging and cover their tracks by removing monitoring capabilities.
Removal of audit rules can significantly impair detection of malicious activities on the affected system.

## Metadata

- Rule ID: bed26dea-4525-47f4-b24a-76e30e44ffb0
- Status: experimental
- Level: high
- Author: Mohamed LAKRI
- Date: 2025-10-17
- Source Path: rules/linux/process_creation/proc_creation_lnx_auditctl_clear_rules.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.012]]

## Detection

```yaml
selection:
  Image|endswith: /auditctl
  CommandLine|re: -D
condition: selection
```

## False Positives

- An administrator troubleshooting. Investigate all attempts.

## References

- https://www.atomicredteam.io/atomic-red-team/atomics/T1562.012
- https://linux.die.net/man/8/auditct

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_auditctl_clear_rules.yml)
