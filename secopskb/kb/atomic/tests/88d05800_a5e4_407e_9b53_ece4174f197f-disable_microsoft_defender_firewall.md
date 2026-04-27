---
atomic_guid: "88d05800-a5e4-407e-9b53-ece4174f197f"
title: "Disable Microsoft Defender Firewall"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.004"
attack_technique_name: "Impair Defenses: Disable or Modify System Firewall"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.004/T1562.004.yaml"
build_date: "2026-04-27 19:12:28"
executor: "command_prompt"
aliases:
  - "88d05800-a5e4-407e-9b53-ece4174f197f"
  - "Disable Microsoft Defender Firewall"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Disables the Microsoft Defender Firewall for the current profile.
Caution if you access remotely the host where the test runs! Especially with the cleanup command which will re-enable firewall for the current profile...

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses#^t1562004-disable-or-modify-system-firewall|T1562.004: Disable or Modify System Firewall]]

## Executor

- name: command_prompt

### Command

```cmd
netsh advfirewall set currentprofile state off
```

### Cleanup

```cmd
netsh advfirewall set currentprofile state on >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.004/T1562.004.yaml)
