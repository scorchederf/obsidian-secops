---
sigma_id: "207b0396-3689-42d9-8399-4222658efc99"
title: "Potential Privilege Escalation To LOCAL SYSTEM"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_sysinternals_susp_psexec_paexec_flags.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sysinternals_susp_psexec_paexec_flags.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "207b0396-3689-42d9-8399-4222658efc99"
  - "Potential Privilege Escalation To LOCAL SYSTEM"
attack_technique_ids:
  - "T1587.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Privilege Escalation To LOCAL SYSTEM

Detects unknown program using commandline flags usually used by tools such as PsExec and PAExec to start programs with SYSTEM Privileges

## Metadata

- Rule ID: 207b0396-3689-42d9-8399-4222658efc99
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems), Nasreddine Bencherchali (Nextron Systems)
- Date: 2021-05-22
- Modified: 2024-03-05
- Source Path: rules/windows/process_creation/proc_creation_win_sysinternals_susp_psexec_paexec_flags.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1587-develop_capabilities|T1587.001]]

## Detection

```yaml
selection:
  CommandLine|contains|windash:
  - ' -s cmd'
  - ' -s -i cmd'
  - ' -i -s cmd'
  - ' -s pwsh'
  - ' -s -i pwsh'
  - ' -i -s pwsh'
  - ' -s powershell'
  - ' -s -i powershell'
  - ' -i -s powershell'
filter_main_exclude_coverage:
  CommandLine|contains:
  - paexec
  - PsExec
  - accepteula
condition: selection and not 1 of filter_main_*
```

## False Positives

- Weird admins that rename their tools
- Software companies that bundle PsExec/PAExec with their software and rename it, so that it is less embarrassing

## References

- https://learn.microsoft.com/en-us/sysinternals/downloads/psexec
- https://www.poweradmin.com/paexec/
- https://www.fireeye.com/blog/threat-research/2020/10/kegtap-and-singlemalt-with-a-ransomware-chaser.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sysinternals_susp_psexec_paexec_flags.yml)
