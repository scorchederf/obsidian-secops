---
atomic_guid: "69f625ba-938f-4900-bdff-82ada3df5d9c"
title: "Discover System Language with dism.exe"
framework: "atomic"
generated: "true"
attack_technique_id: "T1614.001"
attack_technique_name: "System Location Discovery: System Language Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1614.001/T1614.001.yaml"
build_date: "2026-04-26 17:02:13"
executor: "command_prompt"
aliases:
  - "69f625ba-938f-4900-bdff-82ada3df5d9c"
  - "Discover System Language with dism.exe"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Discover System Language with dism.exe

The Windows utility DISM (Deployment Image Servicing and Management) can be used to display information about international settings and languages on the currently installed Windows image using an elevated terminal.

## Metadata

- Atomic GUID: 69f625ba-938f-4900-bdff-82ada3df5d9c
- Technique: T1614.001: System Location Discovery: System Language Discovery
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1614.001/T1614.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1614-system_location_discovery|T1614.001]]

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
dism.exe /online /Get-Intl
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1614.001/T1614.001.yaml)
