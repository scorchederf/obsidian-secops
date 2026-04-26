---
atomic_guid: "b5656f67-d67f-4de8-8e62-b5581630f528"
title: "Windows Internal Packet Capture"
framework: "atomic"
generated: "true"
attack_technique_id: "T1040"
attack_technique_name: "Network Sniffing"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1040/T1040.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "b5656f67-d67f-4de8-8e62-b5581630f528"
  - "Windows Internal Packet Capture"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Windows Internal Packet Capture

Uses the built-in Windows packet capture
After execution you should find a file named trace.etl and trace.cab in the temp directory

## Metadata

- Atomic GUID: b5656f67-d67f-4de8-8e62-b5581630f528
- Technique: T1040: Network Sniffing
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1040/T1040.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1040-network_sniffing|T1040]]

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
netsh trace start capture=yes tracefile=%temp%\trace.etl maxsize=10
```

### Cleanup

```cmd
netsh trace stop >nul 2>&1
TIMEOUT /T 5 >nul 2>&1
del %temp%\trace.etl >nul 2>&1
del %temp%\trace.cab >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1040/T1040.yaml)
