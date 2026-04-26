---
sigma_id: "8834e2f7-6b4b-4f09-8906-d2276470ee23"
title: "PsExec/PAExec Escalation to LOCAL SYSTEM"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_sysinternals_psexec_paexec_escalate_system.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sysinternals_psexec_paexec_escalate_system.yml"
build_date: "2026-04-26 17:03:21"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "8834e2f7-6b4b-4f09-8906-d2276470ee23"
  - "PsExec/PAExec Escalation to LOCAL SYSTEM"
attack_technique_ids:
  - "T1587.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# PsExec/PAExec Escalation to LOCAL SYSTEM

Detects suspicious commandline flags used by PsExec and PAExec to escalate a command line to LOCAL_SYSTEM rights

## Metadata

- Rule ID: 8834e2f7-6b4b-4f09-8906-d2276470ee23
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems), Nasreddine Bencherchali (Nextron Systems)
- Date: 2021-11-23
- Modified: 2024-03-05
- Source Path: rules/windows/process_creation/proc_creation_win_sysinternals_psexec_paexec_escalate_system.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1587-develop_capabilities|T1587.001]]

## Detection

```yaml
selection_sys:
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
selection_other:
  CommandLine|contains:
  - psexec
  - paexec
  - accepteula
condition: all of selection_*
```

## False Positives

- Admins that use PsExec or PAExec to escalate to the SYSTEM account for maintenance purposes (rare)
- Users that debug Microsoft Intune issues using the commands mentioned in the official documentation; see https://learn.microsoft.com/en-us/mem/intune/apps/intune-management-extension

## References

- https://learn.microsoft.com/en-us/sysinternals/downloads/psexec
- https://www.poweradmin.com/paexec/
- https://www.fireeye.com/blog/threat-research/2020/10/kegtap-and-singlemalt-with-a-ransomware-chaser.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_sysinternals_psexec_paexec_escalate_system.yml)
