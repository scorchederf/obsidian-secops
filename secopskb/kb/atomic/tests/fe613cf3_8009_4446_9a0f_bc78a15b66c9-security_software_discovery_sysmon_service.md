---
atomic_guid: "fe613cf3-8009-4446-9a0f-bc78a15b66c9"
title: "Security Software Discovery - Sysmon Service"
framework: "atomic"
generated: "true"
attack_technique_id: "T1518.001"
attack_technique_name: "Software Discovery: Security Software Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1518.001/T1518.001.yaml"
build_date: "2026-04-26 17:02:13"
executor: "command_prompt"
aliases:
  - "fe613cf3-8009-4446-9a0f-bc78a15b66c9"
  - "Security Software Discovery - Sysmon Service"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Security Software Discovery - Sysmon Service

Discovery of an installed Sysinternals Sysmon service using driver altitude (even if the name is changed).

when sucessfully executed, the test is going to display sysmon driver instance if it is installed.

## Metadata

- Atomic GUID: fe613cf3-8009-4446-9a0f-bc78a15b66c9
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

```cmd
fltmc.exe | findstr.exe 385201
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1518.001/T1518.001.yaml)
