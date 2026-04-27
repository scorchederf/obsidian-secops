---
atomic_guid: "15e57006-79dd-46df-9bf9-31bc24fb5a80"
title: "Opening ports for proxy - HARDRAIN"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.004"
attack_technique_name: "Impair Defenses: Disable or Modify System Firewall"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.004/T1562.004.yaml"
build_date: "2026-04-26 17:02:13"
executor: "command_prompt"
aliases:
  - "15e57006-79dd-46df-9bf9-31bc24fb5a80"
  - "Opening ports for proxy - HARDRAIN"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Opening ports for proxy - HARDRAIN

This test creates a listening interface on a victim device. This tactic was used by HARDRAIN for proxying.

reference: https://www.us-cert.gov/sites/default/files/publications/MAR-10135536-F.pdf

## Metadata

- Atomic GUID: 15e57006-79dd-46df-9bf9-31bc24fb5a80
- Technique: T1562.004: Impair Defenses: Disable or Modify System Firewall
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1562.004/T1562.004.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses|T1562.004]]

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
netsh advfirewall firewall add rule name="atomic testing" action=allow dir=in protocol=TCP localport=450
```

### Cleanup

```cmd
netsh advfirewall firewall delete rule name="atomic testing" protocol=TCP localport=450 >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.004/T1562.004.yaml)
