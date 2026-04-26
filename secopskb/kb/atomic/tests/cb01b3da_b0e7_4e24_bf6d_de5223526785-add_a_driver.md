---
atomic_guid: "cb01b3da-b0e7-4e24-bf6d-de5223526785"
title: "Add a driver"
framework: "atomic"
generated: "true"
attack_technique_id: "T1547"
attack_technique_name: "Boot or Logon Autostart Execution"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547/T1547.yaml"
build_date: "2026-04-26 17:02:13"
executor: "command_prompt"
aliases:
  - "cb01b3da-b0e7-4e24-bf6d-de5223526785"
  - "Add a driver"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Add a driver

Install a driver via pnputil.exe lolbin

## Metadata

- Atomic GUID: cb01b3da-b0e7-4e24-bf6d-de5223526785
- Technique: T1547: Boot or Logon Autostart Execution
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1547/T1547.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547]]

## Input Arguments

### driver_inf

- description: A built-in, already installed windows driver inf
- type: path
- default: C:\Windows\INF\usbstor.inf

## Executor

- name: command_prompt

### Command

```cmd
pnputil.exe /add-driver "#{driver_inf}"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547/T1547.yaml)
