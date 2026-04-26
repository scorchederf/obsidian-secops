---
sigma_id: "f2bed782-994e-4f40-9cd5-518198cb3fba"
title: "Linux Sudo Chroot Execution"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_chroot_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_chroot_execution.yml"
build_date: "2026-04-26 14:14:28"
status: "experimental"
level: "low"
logsource: "linux / process_creation"
aliases:
  - "f2bed782-994e-4f40-9cd5-518198cb3fba"
  - "Linux Sudo Chroot Execution"
attack_technique_ids:
  - "T1068"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Linux Sudo Chroot Execution

Detects the execution of 'sudo' command with '--chroot' option, which is used to change the root directory for command execution.
Attackers may use this technique to evade detection and execute commands in a modified environment.
This can be part of a privilege escalation strategy, as it allows the execution of commands with elevated privileges in a controlled environment as seen in CVE-2025-32463.
While investigating, look out for unusual or unexpected use of 'sudo --chroot' in conjunction with other commands or scripts such as execution from temporary directories or unusual user accounts.

## Metadata

- Rule ID: f2bed782-994e-4f40-9cd5-518198cb3fba
- Status: experimental
- Level: low
- Author: Swachchhanda Shrawn Poudel (Nextron Systems)
- Date: 2025-10-02
- Source Path: rules/linux/process_creation/proc_creation_lnx_chroot_execution.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1068-exploitation_for_privilege_escalation|T1068]]

## Detection

```yaml
selection:
  Image|endswith: /sudo
  CommandLine|contains:
  - ' --chroot '
  - 'sudo -R '
condition: selection
```

## False Positives

- Legitimate administrative tasks or scripts that use 'sudo --chroot' for containerization, testing, or system management.

## References

- https://github.com/kh4sh3i/CVE-2025-32463/blob/81bb430f84fa2089224733c3ed4bfa434c197ad4/exploit.sh

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_chroot_execution.yml)
