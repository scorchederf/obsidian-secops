---
atomic_guid: "1dd59fb3-1cb3-4828-805d-cf80b4c3bbb5"
title: "Windows Add Registry Value to Load Service in Safe Mode without Network"
framework: "atomic"
generated: "true"
attack_technique_id: "T1112"
attack_technique_name: "Modify Registry"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "1dd59fb3-1cb3-4828-805d-cf80b4c3bbb5"
  - "Windows Add Registry Value to Load Service in Safe Mode without Network"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Windows Add Registry Value to Load Service in Safe Mode without Network

Modify the registry to allow a driver, service, to persist in Safe Mode.
see https://redcanary.com/blog/tracking-driver-inventory-to-expose-rootkits/ and https://blog.didierstevens.com/2007/03/26/playing-with-safe-mode/ for further details.
Adding a subkey to Minimal with the name of your service and a default value set to Service, makes that your service will be started when you boot into Safe Mode without networking. The same applies for the Network subkey.

## Metadata

- Atomic GUID: 1dd59fb3-1cb3-4828-805d-cf80b4c3bbb5
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

```cmd
REG ADD "HKLM\SYSTEM\CurrentControlSet\Control\SafeBoot\Minimal\AtomicSafeMode" /VE /T REG_SZ /F /D "Service"
```

### Cleanup

```cmd
reg delete "HKLM\SYSTEM\CurrentControlSet\Control\SafeBoot\Minimal\AtomicSafeMode" /f
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml)
