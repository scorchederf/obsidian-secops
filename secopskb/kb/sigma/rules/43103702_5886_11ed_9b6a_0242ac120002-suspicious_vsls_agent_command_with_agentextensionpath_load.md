---
sigma_id: "43103702-5886-11ed-9b6a-0242ac120002"
title: "Suspicious Vsls-Agent Command With AgentExtensionPath Load"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_vslsagent_agentextensionpath_load.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_vslsagent_agentextensionpath_load.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "43103702-5886-11ed-9b6a-0242ac120002"
  - "Suspicious Vsls-Agent Command With AgentExtensionPath Load"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Vsls-Agent Command With AgentExtensionPath Load

Detects Microsoft Visual Studio vsls-agent.exe lolbin execution with a suspicious library load using the --agentExtensionPath parameter

## Metadata

- Rule ID: 43103702-5886-11ed-9b6a-0242ac120002
- Status: test
- Level: medium
- Author: bohops
- Date: 2022-10-30
- Source Path: rules/windows/process_creation/proc_creation_win_vslsagent_agentextensionpath_load.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection:
  Image|endswith: \vsls-agent.exe
  CommandLine|contains: --agentExtensionPath
filter:
  CommandLine|contains: Microsoft.VisualStudio.LiveShare.Agent.
condition: selection and not filter
```

## False Positives

- False positives depend on custom use of vsls-agent.exe

## References

- https://twitter.com/bohops/status/1583916360404729857

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_vslsagent_agentextensionpath_load.yml)
