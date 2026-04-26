---
sigma_id: "e56d3073-83ff-4021-90fe-c658e0709e72"
title: "Gpresult Display Group Policy Information"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_gpresult_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_gpresult_execution.yml"
build_date: "2026-04-26 14:14:26"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "e56d3073-83ff-4021-90fe-c658e0709e72"
  - "Gpresult Display Group Policy Information"
attack_technique_ids:
  - "T1615"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Gpresult Display Group Policy Information

Detects cases in which a user uses the built-in Windows utility gpresult to display the Resultant Set of Policy (RSoP) information

## Metadata

- Rule ID: e56d3073-83ff-4021-90fe-c658e0709e72
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-05-01
- Source Path: rules/windows/process_creation/proc_creation_win_gpresult_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1615-group_policy_discovery|T1615]]

## Detection

```yaml
selection:
  Image|endswith: \gpresult.exe
  CommandLine|contains:
  - /z
  - /v
condition: selection
```

## False Positives

- Unknown

## Simulation

### Display group policy information via gpresult

- atomic_guid: 0976990f-53b1-4d3f-a185-6df5be429d3b
- name: Display group policy information via gpresult
- technique: T1615
- type: atomic-red-team

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1615/T1615.md
- https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/gpresult
- https://unit42.paloaltonetworks.com/emissary-trojan-changelog-did-operation-lotus-blossom-cause-it-to-evolve/
- https://www.welivesecurity.com/wp-content/uploads/2020/05/ESET_Turla_ComRAT.pdf

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_gpresult_execution.yml)
