---
sigma_id: "2fbbe9ff-0afc-470b-bdc0-592198339968"
title: "Remote Access Tool - Potential MeshAgent Execution - Windows"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_remote_access_tools_meshagent_arguments.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_remote_access_tools_meshagent_arguments.yml"
build_date: "2026-04-26 14:14:34"
status: "experimental"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "2fbbe9ff-0afc-470b-bdc0-592198339968"
  - "Remote Access Tool - Potential MeshAgent Execution - Windows"
attack_technique_ids:
  - "T1219.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Remote Access Tool - Potential MeshAgent Execution - Windows

Detects potential execution of MeshAgent which is a tool used for remote access.
Historical data shows that threat actors rename MeshAgent binary to evade detection.
Matching command lines with the '--meshServiceName' argument can indicate that the MeshAgent is being used for remote access.

## Metadata

- Rule ID: 2fbbe9ff-0afc-470b-bdc0-592198339968
- Status: experimental
- Level: medium
- Author: Norbert Jaśniewicz (AlphaSOC)
- Date: 2025-05-19
- Source Path: rules/windows/process_creation/proc_creation_win_remote_access_tools_meshagent_arguments.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1219-remote_access_tools|T1219.002]]

## Detection

```yaml
selection:
  CommandLine|contains: --meshServiceName
condition: selection
```

## False Positives

- Environments that legitimately use MeshAgent

## References

- https://www.huntress.com/blog/know-thy-enemy-a-novel-november-case-on-persistent-remote-access
- https://thecyberexpress.com/ukraine-hit-by-meshagent-malware-campaign/
- https://wazuh.com/blog/how-to-detect-meshagent-with-wazuh/
- https://www.security.com/threat-intelligence/medusa-ransomware-attacks

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_remote_access_tools_meshagent_arguments.yml)
