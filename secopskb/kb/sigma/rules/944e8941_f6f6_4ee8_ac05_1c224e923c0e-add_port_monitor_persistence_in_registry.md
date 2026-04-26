---
sigma_id: "944e8941-f6f6-4ee8-ac05-1c224e923c0e"
title: "Add Port Monitor Persistence in Registry"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_add_port_monitor.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_add_port_monitor.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "windows / registry_set"
aliases:
  - "944e8941-f6f6-4ee8-ac05-1c224e923c0e"
  - "Add Port Monitor Persistence in Registry"
attack_technique_ids:
  - "T1547.010"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Add Port Monitor Persistence in Registry

Adversaries may use port monitors to run an attacker supplied DLL during system boot for persistence or privilege escalation.
A port monitor can be set through the AddMonitor API call to set a DLL to be loaded at startup.

## Metadata

- Rule ID: 944e8941-f6f6-4ee8-ac05-1c224e923c0e
- Status: test
- Level: medium
- Author: frack113
- Date: 2021-12-30
- Modified: 2024-03-25
- Source Path: rules/windows/registry/registry_set/registry_set_add_port_monitor.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547.010]]

## Detection

```yaml
selection:
  TargetObject|contains: \Control\Print\Monitors\
  Details|endswith: .dll
filter_optional_cutepdf:
  Image: C:\Windows\System32\spoolsv.exe
  TargetObject|contains: \Control\Print\Monitors\CutePDF Writer Monitor v4.0\Driver
  Details: cpwmon64_v40.dll
  User|contains:
  - AUTHORI
  - AUTORI
filter_optional_monvnc:
  TargetObject|contains: \Control\Print\Monitors\MONVNC\Driver
filter_optional_vnc:
  TargetObject|contains|all:
  - Control\Print\Environments\
  - \Drivers\
  - \VNC Printer
condition: selection and not 1 of filter_optional_*
```

## False Positives

- Unknown

## Simulation

### Add Port Monitor persistence in Registry

- atomic_guid: d34ef297-f178-4462-871e-9ce618d44e50
- name: Add Port Monitor persistence in Registry
- technique: T1547.010
- type: atomic-red-team

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1547.010/T1547.010.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_add_port_monitor.yml)
