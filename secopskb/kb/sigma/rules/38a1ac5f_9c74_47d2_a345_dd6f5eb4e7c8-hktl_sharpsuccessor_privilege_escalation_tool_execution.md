---
sigma_id: "38a1ac5f-9c74-47d2-a345-dd6f5eb4e7c8"
title: "HKTL - SharpSuccessor Privilege Escalation Tool Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_sharpsuccessor_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_sharpsuccessor_execution.yml"
build_date: "2026-04-27 19:13:51"
status: "experimental"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "38a1ac5f-9c74-47d2-a345-dd6f5eb4e7c8"
  - "HKTL - SharpSuccessor Privilege Escalation Tool Execution"
attack_technique_ids:
  - "T1068"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the execution of SharpSuccessor, a tool used to exploit the BadSuccessor attack for privilege escalation in WinServer 2025 Active Directory environments.
Successful usage of this tool can let the attackers gain the domain admin privileges by exploiting the BadSuccessor vulnerability.

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1068-exploitation_for_privilege_escalation|T1068: Exploitation for Privilege Escalation]]

## Detection

```yaml
selection:
- Image|endswith: \SharpSuccessor.exe
- OriginalFileName: SharpSuccessor.exe
- CommandLine|contains: SharpSuccessor
- CommandLine|contains|all:
  - ' add '
  - ' /impersonate'
  - ' /path'
  - ' /account'
  - ' /name'
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/logangoins/SharpSuccessor

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_sharpsuccessor_execution.yml)
