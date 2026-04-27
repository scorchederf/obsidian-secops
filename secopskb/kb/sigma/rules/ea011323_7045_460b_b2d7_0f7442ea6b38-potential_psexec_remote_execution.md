---
sigma_id: "ea011323-7045-460b-b2d7-0f7442ea6b38"
title: "Potential PsExec Remote Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_sysinternals_psexec_remote_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sysinternals_psexec_remote_execution.yml"
build_date: "2026-04-27 19:13:54"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "ea011323-7045-460b-b2d7-0f7442ea6b38"
  - "Potential PsExec Remote Execution"
attack_technique_ids:
  - "T1587.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects potential psexec command that initiate execution on a remote systems via common commandline flags used by the utility

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1587-develop_capabilities#^t1587001-malware|T1587.001: Malware]]

## Detection

```yaml
selection:
  CommandLine|contains|all:
  - accepteula
  - ' -u '
  - ' -p '
  - ' \\\\'
filter_main_localhost:
  CommandLine|contains:
  - \\\\localhost
  - \\\\127.
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://learn.microsoft.com/en-us/sysinternals/downloads/psexec
- https://www.poweradmin.com/paexec/
- https://www.fireeye.com/blog/threat-research/2020/10/kegtap-and-singlemalt-with-a-ransomware-chaser.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sysinternals_psexec_remote_execution.yml)
