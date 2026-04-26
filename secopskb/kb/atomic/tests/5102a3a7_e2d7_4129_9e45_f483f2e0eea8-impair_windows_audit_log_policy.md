---
atomic_guid: "5102a3a7-e2d7-4129-9e45-f483f2e0eea8"
title: "Impair Windows Audit Log Policy"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.002"
attack_technique_name: "Impair Defenses: Disable Windows Event Logging"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.002/T1562.002.yaml"
build_date: "2026-04-26 14:38:40"
executor: "command_prompt"
aliases:
  - "5102a3a7-e2d7-4129-9e45-f483f2e0eea8"
  - "Impair Windows Audit Log Policy"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Impair Windows Audit Log Policy

Disables the windows audit policy to prevent key host based telemetry being written into the event logs.
[Solarigate example](https://www.microsoft.com/security/blog/2021/01/20/deep-dive-into-the-solorigate-second-stage-activation-from-sunburst-to-teardrop-and-raindrop/)

## Metadata

- Atomic GUID: 5102a3a7-e2d7-4129-9e45-f483f2e0eea8
- Technique: T1562.002: Impair Defenses: Disable Windows Event Logging
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1562.002/T1562.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses|T1562.002]]

## Executor

- elevation_required: True
- name: command_prompt

### Command

```commandprompt
auditpol /set /category:"Account Logon" /success:disable /failure:disable
auditpol /set /category:"Logon/Logoff" /success:disable /failure:disable
auditpol /set /category:"Detailed Tracking" /success:disable
```

### Cleanup

```commandprompt
auditpol /set /category:"Account Logon" /success:enable /failure:enable
auditpol /set /category:"Detailed Tracking" /success:enable
auditpol /set /category:"Logon/Logoff" /success:enable /failure:enable
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.002/T1562.002.yaml)
