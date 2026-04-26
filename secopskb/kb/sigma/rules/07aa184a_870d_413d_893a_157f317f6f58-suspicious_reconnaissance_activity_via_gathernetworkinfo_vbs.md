---
sigma_id: "07aa184a-870d-413d-893a-157f317f6f58"
title: "Suspicious Reconnaissance Activity Via GatherNetworkInfo.VBS"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_gather_network_info_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_gather_network_info_execution.yml"
build_date: "2026-04-26 15:01:52"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "07aa184a-870d-413d-893a-157f317f6f58"
  - "Suspicious Reconnaissance Activity Via GatherNetworkInfo.VBS"
attack_technique_ids:
  - "T1615"
  - "T1059.005"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Suspicious Reconnaissance Activity Via GatherNetworkInfo.VBS

Detects execution of the built-in script located in "C:\Windows\System32\gatherNetworkInfo.vbs". Which can be used to gather information about the target machine

## Metadata

- Rule ID: 07aa184a-870d-413d-893a-157f317f6f58
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-02-08
- Source Path: rules/windows/process_creation/proc_creation_win_susp_gather_network_info_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1615-group_policy_discovery|T1615]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.005]]

## Detection

```yaml
selection:
  CommandLine|contains: gatherNetworkInfo.vbs
filter:
  Image|endswith:
  - \cscript.exe
  - \wscript.exe
condition: selection and not filter
```

## False Positives

- Unknown

## References

- https://posts.slayerlabs.com/living-off-the-land/#gathernetworkinfovbs
- https://www.mandiant.com/resources/blog/trojanized-windows-installers-ukrainian-government

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_gather_network_info_execution.yml)
