---
sigma_id: "2db93a3f-3249-4f73-9e68-0e77a0f8ae7e"
title: "Remote Access Tool - TacticalRMM Agent Registration to Potentially Attacker-Controlled Server"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_remote_access_tools_tacticalrmm_agent_registration_via_cli.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_remote_access_tools_tacticalrmm_agent_registration_via_cli.yml"
build_date: "2026-04-26 14:14:34"
status: "experimental"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "2db93a3f-3249-4f73-9e68-0e77a0f8ae7e"
  - "Remote Access Tool - TacticalRMM Agent Registration to Potentially Attacker-Controlled Server"
attack_technique_ids:
  - "T1219"
  - "T1105"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Remote Access Tool - TacticalRMM Agent Registration to Potentially Attacker-Controlled Server

Detects TacticalRMM agent installations where the --api, --auth, and related flags are used on the command line.
These parameters configure the agent to connect to a specific RMM server with authentication, client ID, and site ID.
This technique could indicate a threat actor attempting to register the agent with an attacker-controlled RMM infrastructure silently.

## Metadata

- Rule ID: 2db93a3f-3249-4f73-9e68-0e77a0f8ae7e
- Status: experimental
- Level: medium
- Author: Ahmed Nosir (@egycondor)
- Date: 2025-05-29
- Source Path: rules/windows/process_creation/proc_creation_win_remote_access_tools_tacticalrmm_agent_registration_via_cli.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1219-remote_access_tools|T1219]]
- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

## Detection

```yaml
selection:
  Image|contains: \TacticalAgent\tacticalrmm.exe
  CommandLine|contains|all:
  - --api
  - --auth
  - --client-id
  - --site-id
  - --agent-type
condition: selection
```

## False Positives

- Legitimate system administrator deploying TacticalRMM

## References

- https://github.com/amidaware/tacticalrmm
- https://apophis133.medium.com/powershell-script-tactical-rmm-installation-45afb639eff3

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_remote_access_tools_tacticalrmm_agent_registration_via_cli.yml)
