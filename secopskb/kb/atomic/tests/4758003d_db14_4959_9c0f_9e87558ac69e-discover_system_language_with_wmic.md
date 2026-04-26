---
atomic_guid: "4758003d-db14-4959-9c0f-9e87558ac69e"
title: "Discover System Language with WMIC"
framework: "atomic"
generated: "true"
attack_technique_id: "T1614.001"
attack_technique_name: "System Location Discovery: System Language Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1614.001/T1614.001.yaml"
build_date: "2026-04-26 14:38:40"
executor: "command_prompt"
aliases:
  - "4758003d-db14-4959-9c0f-9e87558ac69e"
  - "Discover System Language with WMIC"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Discover System Language with WMIC

WMIC (Windows Management Instrumentation Command-line) is a command-line tool that provides a simplified interface to query and manage Windows system configurations, processes, and hardware information using WMI. 

The command in this test retrieves information about the system's locale, operating system language, and multilingual user interface (MUI) languages.

## Metadata

- Atomic GUID: 4758003d-db14-4959-9c0f-9e87558ac69e
- Technique: T1614.001: System Location Discovery: System Language Discovery
- Platforms: windows
- Executor: command_prompt
- Elevation Required: False
- Source Path: atomics/T1614.001/T1614.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1614-system_location_discovery|T1614.001]]

## Input Arguments

### format_style

- description: You can specify multipe output formats for wmic such as table, list and csv.
- type: string
- default: table

### target_host

- description: The host that will be queried.

If the host contains special characters, it may need to be wrapped in double quotes or double + single quotes. 

For example: "DESKTOP-123" or "'DESKTOP-123'".

- type: string
- default: localhost

## Executor

- elevation_required: False
- name: command_prompt

### Command

```commandprompt
wmic /node:#{target_host} os get Locale,OSLanguage,MUILanguages /format:#{format_style}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1614.001/T1614.001.yaml)
