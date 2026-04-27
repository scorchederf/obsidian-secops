---
atomic_guid: "e3ad8e83-3089-49ff-817f-e52f8c948090"
title: "Enabling Remote Desktop Protocol via Remote Registry"
framework: "atomic"
generated: "true"
attack_technique_id: "T1112"
attack_technique_name: "Modify Registry"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml"
build_date: "2026-04-27 19:12:27"
executor: "command_prompt"
aliases:
  - "e3ad8e83-3089-49ff-817f-e52f8c948090"
  - "Enabling Remote Desktop Protocol via Remote Registry"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Enabling RDP through remote registry.

## ATT&CK Mapping

- [[kb/attack/techniques/T1112-modify_registry|T1112: Modify Registry]]

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
reg add "hklm\SYSTEM\CurrentControlSet\Control\Terminal Server\Winstations\RDP-Tcp" /v SecurityLayer /t REG_DWORD /d 0 /f
```

### Cleanup

```cmd
reg add "hklm\SYSTEM\CurrentControlSet\Control\Terminal Server\Winstations\RDP-Tcp" /v SecurityLayer /t REG_DWORD /d 2 /f
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml)
