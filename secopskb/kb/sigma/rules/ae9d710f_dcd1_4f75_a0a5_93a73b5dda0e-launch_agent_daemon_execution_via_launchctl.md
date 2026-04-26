---
sigma_id: "ae9d710f-dcd1-4f75-a0a5-93a73b5dda0e"
title: "Launch Agent/Daemon Execution Via Launchctl"
framework: "sigma"
generated: "true"
source_path: "rules/macos/process_creation/proc_creation_macos_launchctl_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_launchctl_execution.yml"
build_date: "2026-04-26 14:14:28"
status: "test"
level: "medium"
logsource: "macos / process_creation"
aliases:
  - "ae9d710f-dcd1-4f75-a0a5-93a73b5dda0e"
  - "Launch Agent/Daemon Execution Via Launchctl"
attack_technique_ids:
  - "T1569.001"
  - "T1543.001"
  - "T1543.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Launch Agent/Daemon Execution Via Launchctl

Detects the execution of programs as Launch Agents or Launch Daemons using launchctl on macOS.

## Metadata

- Rule ID: ae9d710f-dcd1-4f75-a0a5-93a73b5dda0e
- Status: test
- Level: medium
- Author: Pratinav Chandra
- Date: 2024-05-13
- Source Path: rules/macos/process_creation/proc_creation_macos_launchctl_execution.yml

## Logsource

- category: process_creation
- product: macos

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1569-system_services|T1569.001]]
- [[kb/attack/techniques/T1543-create_or_modify_system_process|T1543.001]]
- [[kb/attack/techniques/T1543-create_or_modify_system_process|T1543.004]]

## Detection

```yaml
selection:
  Image|endswith: /launchctl
  CommandLine|contains:
  - submit
  - load
  - start
condition: selection
```

## False Positives

- Legitimate administration activities is expected to trigger false positives. Investigate the command line being passed to determine if the service or launch agent are suspicious.

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1569.001/T1569.001.md
- https://www.sentinelone.com/labs/20-common-tools-techniques-used-by-macos-threat-actors-malware/
- https://www.welivesecurity.com/2020/07/16/mac-cryptocurrency-trading-application-rebranded-bundled-malware/
- https://www.trendmicro.com/en_us/research/18/d/new-macos-backdoor-linked-to-oceanlotus-found.html
- https://www.loobins.io/binaries/launchctl/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_launchctl_execution.yml)
