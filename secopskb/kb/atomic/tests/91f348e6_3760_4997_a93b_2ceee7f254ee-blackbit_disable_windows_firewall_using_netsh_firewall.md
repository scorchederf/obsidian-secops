---
atomic_guid: "91f348e6-3760-4997-a93b-2ceee7f254ee"
title: "Blackbit - Disable Windows Firewall using netsh firewall"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.004"
attack_technique_name: "Impair Defenses: Disable or Modify System Firewall"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.004/T1562.004.yaml"
build_date: "2026-04-26 17:02:13"
executor: "command_prompt"
aliases:
  - "91f348e6-3760-4997-a93b-2ceee7f254ee"
  - "Blackbit - Disable Windows Firewall using netsh firewall"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Blackbit - Disable Windows Firewall using netsh firewall

An adversary tries to modify the windows firewall configuration using the deprecated netsh firewall command (command still works).

## Metadata

- Atomic GUID: 91f348e6-3760-4997-a93b-2ceee7f254ee
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
netsh firewall set opmode mode=disable
```

### Cleanup

```cmd
netsh firewall set opmode mode=enable >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.004/T1562.004.yaml)
