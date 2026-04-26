---
atomic_guid: "c173c948-65e5-499c-afbe-433722ed5bd4"
title: "Windows Add Registry Value to Load Service in Safe Mode with Network"
framework: "atomic"
generated: "true"
attack_technique_id: "T1112"
attack_technique_name: "Modify Registry"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml"
build_date: "2026-04-26 14:38:40"
executor: "command_prompt"
aliases:
  - "c173c948-65e5-499c-afbe-433722ed5bd4"
  - "Windows Add Registry Value to Load Service in Safe Mode with Network"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Windows Add Registry Value to Load Service in Safe Mode with Network

Modify the registry to allow a driver, service, to persist in Safe Mode with networking.
see https://redcanary.com/blog/tracking-driver-inventory-to-expose-rootkits/ and https://blog.didierstevens.com/2007/03/26/playing-with-safe-mode/ for further details.
Adding a subkey to Netowrk with the name of your service and a default value set to Service, makes that your service will be started when you boot into Safe Mode with networking.

## Metadata

- Atomic GUID: c173c948-65e5-499c-afbe-433722ed5bd4
- Technique: T1112: Modify Registry
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1112/T1112.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1112-modify_registry|T1112]]

## Executor

- elevation_required: True
- name: command_prompt

### Command

```commandprompt
REG ADD "HKLM\SYSTEM\CurrentControlSet\Control\SafeBoot\Network\AtomicSafeMode" /VE /T REG_SZ /F /D "Service"
```

### Cleanup

```commandprompt
reg delete "HKLM\SYSTEM\CurrentControlSet\Control\SafeBoot\Network\AtomicSafeMode" /f
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml)
