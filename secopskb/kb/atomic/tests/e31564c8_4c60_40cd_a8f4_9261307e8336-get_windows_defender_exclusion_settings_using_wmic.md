---
atomic_guid: "e31564c8-4c60-40cd-a8f4-9261307e8336"
title: "Get Windows Defender exclusion settings using WMIC"
framework: "atomic"
generated: "true"
attack_technique_id: "T1518.001"
attack_technique_name: "Software Discovery: Security Software Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1518.001/T1518.001.yaml"
build_date: "2026-04-26 17:02:13"
executor: "command_prompt"
aliases:
  - "e31564c8-4c60-40cd-a8f4-9261307e8336"
  - "Get Windows Defender exclusion settings using WMIC"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Get Windows Defender exclusion settings using WMIC

In this test, a WMIC command is used to probe the local Windows system for the configuration of Windows Defender's exclusions. This command targets the MSFT_MpPreference 
class within the Windows Management Instrumentation (WMI) namespace, allowing the retrieval of critical settings such as disabled real-time monitoring and specified 
exclusion paths, file extensions, and processes. Attackers might use this approach to understand what is excluded from antivirus scans, enabling further exploitation.

## Metadata

- Atomic GUID: e31564c8-4c60-40cd-a8f4-9261307e8336
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
wmic /Node:localhost /Namespace:\\root\Microsoft\Windows\Defender Path MSFT_MpPreference Get /format:list | findstr /i /C:"DisableRealtimeMonitoring" /C:"ExclusionPath" /C:"ExclusionExtension" /C:"ExclusionProcess"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1518.001/T1518.001.yaml)
