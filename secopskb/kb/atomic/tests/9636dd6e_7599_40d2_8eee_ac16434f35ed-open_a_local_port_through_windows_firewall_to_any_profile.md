---
atomic_guid: "9636dd6e-7599-40d2-8eee-ac16434f35ed"
title: "Open a local port through Windows Firewall to any profile"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.004"
attack_technique_name: "Impair Defenses: Disable or Modify System Firewall"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.004/T1562.004.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "9636dd6e-7599-40d2-8eee-ac16434f35ed"
  - "Open a local port through Windows Firewall to any profile"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Open a local port through Windows Firewall to any profile

This test will attempt to open a local port defined by input arguments to any profile

## Metadata

- Atomic GUID: 9636dd6e-7599-40d2-8eee-ac16434f35ed
- Technique: T1562.004: Impair Defenses: Disable or Modify System Firewall
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1562.004/T1562.004.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses|T1562.004]]

## Input Arguments

### local_port

- description: This is the local port you wish to test opening
- type: integer
- default: 3389

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
netsh advfirewall firewall add rule name="Open Port to Any" dir=in protocol=tcp localport=#{local_port} action=allow profile=any
```

### Cleanup

```powershell
netsh advfirewall firewall delete rule name="Open Port to Any" | Out-Null
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.004/T1562.004.yaml)
