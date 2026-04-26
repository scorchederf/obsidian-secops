---
atomic_guid: "5cb0b071-8a5a-412f-839d-116beb2ed9f7"
title: "Driver Installation Using pnputil.exe"
framework: "atomic"
generated: "true"
attack_technique_id: "T1547"
attack_technique_name: "Boot or Logon Autostart Execution"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547/T1547.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "5cb0b071-8a5a-412f-839d-116beb2ed9f7"
  - "Driver Installation Using pnputil.exe"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Driver Installation Using pnputil.exe

pnputil.exe is a native command-line utility in Windows to install drivers, this can be abused by to install malicious drivers. Ref: https://lolbas-project.github.io/lolbas/Binaries/Pnputil/

## Metadata

- Atomic GUID: 5cb0b071-8a5a-412f-839d-116beb2ed9f7
- Technique: T1547: Boot or Logon Autostart Execution
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1547/T1547.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547]]

## Input Arguments

### driver_path

- description: Enter the driver file path to install (Default is used built-in windows driver - acpipmi.inf)
- type: path
- default: C:\Windows\INF\acpipmi.inf

## Executor

- name: powershell

### Command

```powershell
pnputil.exe -i -a #{driver_path}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547/T1547.yaml)
