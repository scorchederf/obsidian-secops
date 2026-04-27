---
sigma_id: "2a4b3e61-9d22-4e4a-b60f-6e8f0cde6f25"
title: "Potential Provisioning Registry Key Abuse For Binary Proxy Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_registry_provlaunch_provisioning_command.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_registry_provlaunch_provisioning_command.yml"
build_date: "2026-04-26 17:03:21"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "2a4b3e61-9d22-4e4a-b60f-6e8f0cde6f25"
  - "Potential Provisioning Registry Key Abuse For Binary Proxy Execution"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Potential Provisioning Registry Key Abuse For Binary Proxy Execution

Detects potential abuse of the provisioning registry key for indirect command execution through "Provlaunch.exe".

## Metadata

- Rule ID: 2a4b3e61-9d22-4e4a-b60f-6e8f0cde6f25
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems), Swachchhanda Shrawan Poudel
- Date: 2023-08-08
- Source Path: rules/windows/process_creation/proc_creation_win_registry_provlaunch_provisioning_command.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection:
  CommandLine|contains: SOFTWARE\Microsoft\Provisioning\Commands\
condition: selection
```

## False Positives

- Unknown

## References

- https://lolbas-project.github.io/lolbas/Binaries/Provlaunch/
- https://twitter.com/0gtweet/status/1674399582162153472

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_registry_provlaunch_provisioning_command.yml)
