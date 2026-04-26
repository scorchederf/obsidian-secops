---
atomic_guid: "d9841bf8-f161-4c73-81e9-fd773a5ff8c1"
title: "Allow SMB and RDP on Microsoft Defender Firewall"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.004"
attack_technique_name: "Impair Defenses: Disable or Modify System Firewall"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.004/T1562.004.yaml"
build_date: "2026-04-26 14:38:40"
executor: "command_prompt"
aliases:
  - "d9841bf8-f161-4c73-81e9-fd773a5ff8c1"
  - "Allow SMB and RDP on Microsoft Defender Firewall"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Allow SMB and RDP on Microsoft Defender Firewall

Allow all SMB and RDP rules on the Microsoft Defender Firewall for all profiles.
Caution if you access remotely the host where the test runs! Especially with the cleanup command which will reset the firewall and risk disabling those services...

## Metadata

- Atomic GUID: d9841bf8-f161-4c73-81e9-fd773a5ff8c1
- Technique: T1562.004: Impair Defenses: Disable or Modify System Firewall
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1562.004/T1562.004.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses|T1562.004]]

## Executor

- name: command_prompt

### Command

```commandprompt
netsh advfirewall firewall set rule group="remote desktop" new enable=Yes
netsh advfirewall firewall set rule group="file and printer sharing" new enable=Yes
```

### Cleanup

```commandprompt
netsh advfirewall reset >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.004/T1562.004.yaml)
