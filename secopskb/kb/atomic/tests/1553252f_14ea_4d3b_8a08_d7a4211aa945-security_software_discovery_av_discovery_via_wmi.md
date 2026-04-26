---
atomic_guid: "1553252f-14ea-4d3b-8a08-d7a4211aa945"
title: "Security Software Discovery - AV Discovery via WMI"
framework: "atomic"
generated: "true"
attack_technique_id: "T1518.001"
attack_technique_name: "Software Discovery: Security Software Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1518.001/T1518.001.yaml"
build_date: "2026-04-26 14:38:40"
executor: "command_prompt"
aliases:
  - "1553252f-14ea-4d3b-8a08-d7a4211aa945"
  - "Security Software Discovery - AV Discovery via WMI"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Security Software Discovery - AV Discovery via WMI

Discovery of installed antivirus products via a WMI query.

when sucessfully executed, the test is going to display installed AV software.

## Metadata

- Atomic GUID: 1553252f-14ea-4d3b-8a08-d7a4211aa945
- Technique: T1518.001: Software Discovery: Security Software Discovery
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1518.001/T1518.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1518-software_discovery|T1518.001]]

## Executor

- elevation_required: True
- name: command_prompt

### Command

```commandprompt
wmic.exe /Namespace:\\root\SecurityCenter2 Path AntiVirusProduct Get displayName /Format:List
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1518.001/T1518.001.yaml)
