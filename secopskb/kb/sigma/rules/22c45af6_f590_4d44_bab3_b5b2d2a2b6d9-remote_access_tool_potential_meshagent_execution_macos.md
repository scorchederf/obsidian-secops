---
sigma_id: "22c45af6-f590-4d44-bab3-b5b2d2a2b6d9"
title: "Remote Access Tool - Potential MeshAgent Execution - MacOS"
framework: "sigma"
generated: "true"
source_path: "rules/macos/process_creation/proc_creation_macos_remote_access_tools_meshagent_arguments.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_remote_access_tools_meshagent_arguments.yml"
build_date: "2026-04-26 14:14:34"
status: "experimental"
level: "medium"
logsource: "macos / process_creation"
aliases:
  - "22c45af6-f590-4d44-bab3-b5b2d2a2b6d9"
  - "Remote Access Tool - Potential MeshAgent Execution - MacOS"
attack_technique_ids:
  - "T1219.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Remote Access Tool - Potential MeshAgent Execution - MacOS

Detects potential execution of MeshAgent which is a tool used for remote access.
Historical data shows that threat actors rename MeshAgent binary to evade detection.
Matching command lines with the '--meshServiceName' argument can indicate that the MeshAgent is being used for remote access.

## Metadata

- Rule ID: 22c45af6-f590-4d44-bab3-b5b2d2a2b6d9
- Status: experimental
- Level: medium
- Author: Norbert Jaśniewicz (AlphaSOC)
- Date: 2025-05-19
- Source Path: rules/macos/process_creation/proc_creation_macos_remote_access_tools_meshagent_arguments.yml

## Logsource

- category: process_creation
- product: macos

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

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_remote_access_tools_meshagent_arguments.yml)
