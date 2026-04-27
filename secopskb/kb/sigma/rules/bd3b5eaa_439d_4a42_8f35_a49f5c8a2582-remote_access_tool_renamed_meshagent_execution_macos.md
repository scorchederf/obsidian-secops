---
sigma_id: "bd3b5eaa-439d-4a42-8f35-a49f5c8a2582"
title: "Remote Access Tool - Renamed MeshAgent Execution - MacOS"
framework: "sigma"
generated: "true"
source_path: "rules/macos/process_creation/proc_creation_macos_remote_access_tools_renamed_meshagent_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_remote_access_tools_renamed_meshagent_execution.yml"
build_date: "2026-04-26 17:03:21"
status: "experimental"
level: "high"
logsource: "macos / process_creation"
aliases:
  - "bd3b5eaa-439d-4a42-8f35-a49f5c8a2582"
  - "Remote Access Tool - Renamed MeshAgent Execution - MacOS"
attack_technique_ids:
  - "T1219.002"
  - "T1036.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Remote Access Tool - Renamed MeshAgent Execution - MacOS

Detects the execution of a renamed instance of the Remote Monitoring and Management (RMM) tool, MeshAgent.
RMM tools such as MeshAgent are commonly utilized by IT administrators for legitimate remote support and system management.
However, malicious actors may exploit these tools by renaming them to bypass detection mechanisms, enabling unauthorized access and control over compromised systems.

## Metadata

- Rule ID: bd3b5eaa-439d-4a42-8f35-a49f5c8a2582
- Status: experimental
- Level: high
- Author: Norbert Jaśniewicz (AlphaSOC)
- Date: 2025-05-19
- Source Path: rules/macos/process_creation/proc_creation_macos_remote_access_tools_renamed_meshagent_execution.yml

## Logsource

- category: process_creation
- product: macos

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1219-remote_access_tools|T1219.002]]
- [[kb/attack/techniques/T1036-masquerading|T1036.003]]

## Detection

```yaml
selection_meshagent:
- CommandLine|contains: --meshServiceName
- OriginalFileName|contains: meshagent
filter_main_legitimate:
  Image|endswith:
  - /meshagent
  - /meshagent_osx64
condition: selection_meshagent and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://www.huntress.com/blog/know-thy-enemy-a-novel-november-case-on-persistent-remote-access
- https://thecyberexpress.com/ukraine-hit-by-meshagent-malware-campaign/
- https://wazuh.com/blog/how-to-detect-meshagent-with-wazuh/
- https://www.security.com/threat-intelligence/medusa-ransomware-attacks

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_remote_access_tools_renamed_meshagent_execution.yml)
