---
sigma_id: "067d8238-7127-451c-a9ec-fa78045b618b"
title: "Linux Doas Tool Execution"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_doas_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_doas_execution.yml"
build_date: "2026-04-26 14:14:28"
status: "stable"
level: "low"
logsource: "linux / process_creation"
aliases:
  - "067d8238-7127-451c-a9ec-fa78045b618b"
  - "Linux Doas Tool Execution"
attack_technique_ids:
  - "T1548"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Linux Doas Tool Execution

Detects the doas tool execution in linux host platform. This utility tool allow standard users to perform tasks as root, the same way sudo does.

## Metadata

- Rule ID: 067d8238-7127-451c-a9ec-fa78045b618b
- Status: stable
- Level: low
- Author: Sittikorn S, Teoderick Contreras
- Date: 2022-01-20
- Source Path: rules/linux/process_creation/proc_creation_lnx_doas_execution.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548]]

## Detection

```yaml
selection:
  Image|endswith: /doas
condition: selection
```

## False Positives

- Unlikely

## References

- https://research.splunk.com/endpoint/linux_doas_tool_execution/
- https://www.makeuseof.com/how-to-install-and-use-doas/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_doas_execution.yml)
