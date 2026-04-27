---
atomic_guid: "2a78362e-b79a-4482-8e24-be397bce4d85"
title: "Safe Mode Boot"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.009"
attack_technique_name: "Impair Defenses: Safe Boot Mode"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.009/T1562.009.yaml"
build_date: "2026-04-27 19:12:28"
executor: "command_prompt"
aliases:
  - "2a78362e-b79a-4482-8e24-be397bce4d85"
  - "Safe Mode Boot"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Allows adversaries to abuse safe mode to disable endpoint defenses that may not start with limited boot

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses#^t1562009-safe-mode-boot|T1562.009: Safe Mode Boot]]

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
bcdedit /set safeboot network
```

### Cleanup

```cmd
bcdedit /deletevalue {current} safeboot
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.009/T1562.009.yaml)
