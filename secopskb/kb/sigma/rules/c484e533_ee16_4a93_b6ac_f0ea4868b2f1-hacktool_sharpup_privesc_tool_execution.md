---
sigma_id: "c484e533-ee16-4a93-b6ac-f0ea4868b2f1"
title: "HackTool - SharpUp PrivEsc Tool Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_sharpup.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_sharpup.yml"
build_date: "2026-04-26 14:14:27"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# HackTool - SharpUp PrivEsc Tool Execution

Detects the use of SharpUp, a tool for local privilege escalation

## Metadata

- Rule ID: c484e533-ee16-4a93-b6ac-f0ea4868b2f1
- Status: test
- Level: critical
- Author: Florian Roth (Nextron Systems)
- Date: 2022-08-20
- Modified: 2023-02-13
- Source Path: rules/windows/process_creation/proc_creation_win_hktl_sharpup.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1615-group_policy_discovery|T1615]]
- [[kb/attack/techniques/T1569-system_services|T1569.002]]
- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.005]]

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
