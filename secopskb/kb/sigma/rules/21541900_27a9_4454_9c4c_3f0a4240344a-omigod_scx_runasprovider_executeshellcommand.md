---
sigma_id: "21541900-27a9-4454-9c4c-3f0a4240344a"
title: "OMIGOD SCX RunAsProvider ExecuteShellCommand"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_omigod_scx_runasprovider_executeshellcommand.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_omigod_scx_runasprovider_executeshellcommand.yml"
build_date: "2026-04-26 17:03:20"
status: "test"
level: "high"
logsource: "linux / process_creation"
aliases:
  - "21541900-27a9-4454-9c4c-3f0a4240344a"
  - "OMIGOD SCX RunAsProvider ExecuteShellCommand"
attack_technique_ids:
  - "T1068"
  - "T1190"
  - "T1203"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# OMIGOD SCX RunAsProvider ExecuteShellCommand

Rule to detect the use of the SCX RunAsProvider Invoke_ExecuteShellCommand to execute any UNIX/Linux command using the /bin/sh shell.
SCXcore, started as the Microsoft Operations Manager UNIX/Linux Agent, is now used in a host of products including
Microsoft Operations Manager, Microsoft Azure, and Microsoft Operations Management Suite.

## Metadata

- Rule ID: 21541900-27a9-4454-9c4c-3f0a4240344a
- Status: test
- Level: high
- Author: Roberto Rodriguez (Cyb3rWard0g), OTR (Open Threat Research), MSTIC
- Date: 2021-10-15
- Modified: 2022-10-05
- Source Path: rules/linux/process_creation/proc_creation_lnx_omigod_scx_runasprovider_executeshellcommand.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1068-exploitation_for_privilege_escalation|T1068]]
- [[kb/attack/techniques/T1190-exploit_public-facing_application|T1190]]
- [[kb/attack/techniques/T1203-exploitation_for_client_execution|T1203]]

## Detection

```yaml
selection:
  User: root
  LogonId: 0
  CurrentDirectory: /var/opt/microsoft/scx/tmp
  CommandLine|contains: /bin/sh
condition: selection
```

## False Positives

- Legitimate use of SCX RunAsProvider Invoke_ExecuteShellCommand.

## References

- https://www.wiz.io/blog/omigod-critical-vulnerabilities-in-omi-azure
- https://github.com/Azure/Azure-Sentinel/pull/3059

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_omigod_scx_runasprovider_executeshellcommand.yml)
