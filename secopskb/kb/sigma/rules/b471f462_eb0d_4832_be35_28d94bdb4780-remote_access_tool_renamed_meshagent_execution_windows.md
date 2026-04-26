---
sigma_id: "b471f462-eb0d-4832-be35-28d94bdb4780"
title: "Remote Access Tool - Renamed MeshAgent Execution - Windows"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_remote_access_tools_renamed_meshagent_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_remote_access_tools_renamed_meshagent_execution.yml"
build_date: "2026-04-26 15:01:50"
status: "experimental"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "b471f462-eb0d-4832-be35-28d94bdb4780"
  - "Remote Access Tool - Renamed MeshAgent Execution - Windows"
attack_technique_ids:
  - "T1219.002"
  - "T1036.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Remote Access Tool - Renamed MeshAgent Execution - Windows

Detects the execution of a renamed instance of the Remote Monitoring and Management (RMM) tool, MeshAgent.
RMM tools such as MeshAgent are commonly utilized by IT administrators for legitimate remote support and system management.
However, malicious actors may exploit these tools by renaming them to bypass detection mechanisms, enabling unauthorized access and control over compromised systems.

## Metadata

- Rule ID: b471f462-eb0d-4832-be35-28d94bdb4780
- Status: experimental
- Level: high
- Author: Norbert Jaśniewicz (AlphaSOC)
- Date: 2025-05-19
- Source Path: rules/windows/process_creation/proc_creation_win_remote_access_tools_renamed_meshagent_execution.yml

## Logsource

- category: process_creation
- product: windows

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
  Image|endswith: \meshagent.exe
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

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_remote_access_tools_renamed_meshagent_execution.yml)
