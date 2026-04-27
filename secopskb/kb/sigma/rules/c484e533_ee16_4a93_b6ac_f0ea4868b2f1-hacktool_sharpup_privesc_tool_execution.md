---
sigma_id: "c484e533-ee16-4a93-b6ac-f0ea4868b2f1"
title: "HackTool - SharpUp PrivEsc Tool Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_sharpup.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_sharpup.yml"
build_date: "2026-04-27 19:13:51"
status: "test"
level: "critical"
logsource: "windows / process_creation"
aliases:
  - "c484e533-ee16-4a93-b6ac-f0ea4868b2f1"
  - "HackTool - SharpUp PrivEsc Tool Execution"
attack_technique_ids:
  - "T1615"
  - "T1569.002"
  - "T1574.005"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the use of SharpUp, a tool for local privilege escalation

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1615-group_policy_discovery|T1615: Group Policy Discovery]]
- [[kb/attack/techniques/T1569-system_services#^t1569002-service-execution|T1569.002: Service Execution]]
- [[kb/attack/techniques/T1574-hijack_execution_flow#^t1574005-executable-installer-file-permissions-weakness|T1574.005: Executable Installer File Permissions Weakness]]

## Detection

```yaml
selection:
- Image|endswith: \SharpUp.exe
- Description: SharpUp
- CommandLine|contains:
  - HijackablePaths
  - UnquotedServicePath
  - ProcessDLLHijack
  - ModifiableServiceBinaries
  - ModifiableScheduledTask
  - DomainGPPPassword
  - CachedGPPPassword
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/GhostPack/SharpUp

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_sharpup.yml)
