---
sigma_id: "38a1ac5f-9c74-47d2-a345-dd6f5eb4e7c8"
title: "HKTL - SharpSuccessor Privilege Escalation Tool Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_sharpsuccessor_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_sharpsuccessor_execution.yml"
build_date: "2026-04-26 15:01:44"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# HKTL - SharpSuccessor Privilege Escalation Tool Execution

Detects the execution of SharpSuccessor, a tool used to exploit the BadSuccessor attack for privilege escalation in WinServer 2025 Active Directory environments.
Successful usage of this tool can let the attackers gain the domain admin privileges by exploiting the BadSuccessor vulnerability.

## Metadata

- Rule ID: 38a1ac5f-9c74-47d2-a345-dd6f5eb4e7c8
- Status: experimental
- Level: high
- Author: Swachchhanda Shrawan Poudel (Nextron Systems)
- Date: 2025-06-06
- Source Path: rules/windows/process_creation/proc_creation_win_hktl_sharpsuccessor_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1068-exploitation_for_privilege_escalation|T1068]]

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
