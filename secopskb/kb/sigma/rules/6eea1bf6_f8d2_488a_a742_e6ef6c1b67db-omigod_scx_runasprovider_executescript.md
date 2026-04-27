---
sigma_id: "6eea1bf6-f8d2-488a-a742-e6ef6c1b67db"
title: "OMIGOD SCX RunAsProvider ExecuteScript"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_omigod_scx_runasprovider_executescript.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_omigod_scx_runasprovider_executescript.yml"
build_date: "2026-04-27 19:13:53"
status: "test"
level: "high"
logsource: "linux / process_creation"
aliases:
  - "6eea1bf6-f8d2-488a-a742-e6ef6c1b67db"
  - "OMIGOD SCX RunAsProvider ExecuteScript"
attack_technique_ids:
  - "T1068"
  - "T1190"
  - "T1203"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Rule to detect the use of the SCX RunAsProvider ExecuteScript to execute any UNIX/Linux script using the /bin/sh shell.
Script being executed gets created as a temp file in /tmp folder with a scx* prefix.
Then it is invoked from the following directory /etc/opt/microsoft/scx/conf/tmpdir/.
The file in that directory has the same prefix scx*. SCXcore, started as the Microsoft Operations Manager UNIX/Linux Agent, is now used in a host of products including
Microsoft Operations Manager, Microsoft Azure, and Microsoft Operations Management Suite.

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1068-exploitation_for_privilege_escalation|T1068: Exploitation for Privilege Escalation]]
- [[kb/attack/techniques/T1190-exploit_public-facing_application|T1190: Exploit Public-Facing Application]]
- [[kb/attack/techniques/T1203-exploitation_for_client_execution|T1203: Exploitation for Client Execution]]

## Detection

```yaml
selection:
  User: root
  LogonId: 0
  CurrentDirectory: /var/opt/microsoft/scx/tmp
  CommandLine|contains: /etc/opt/microsoft/scx/conf/tmpdir/scx
condition: selection
```

## False Positives

- Legitimate use of SCX RunAsProvider ExecuteScript.

## References

- https://www.wiz.io/blog/omigod-critical-vulnerabilities-in-omi-azure
- https://github.com/Azure/Azure-Sentinel/pull/3059

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_omigod_scx_runasprovider_executescript.yml)
