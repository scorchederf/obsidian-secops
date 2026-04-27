---
atomic_guid: "6fb4c4c5-f949-4fd2-8af5-ddbc61595223"
title: "Reg query for AlwaysInstallElevated status"
framework: "atomic"
generated: "true"
attack_technique_id: "T1012"
attack_technique_name: "Query Registry"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1012/T1012.yaml"
build_date: "2026-04-27 19:12:25"
executor: "command_prompt"
aliases:
  - "6fb4c4c5-f949-4fd2-8af5-ddbc61595223"
  - "Reg query for AlwaysInstallElevated status"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

The reg query commands allows to check the status of the AlwaysInstallElevated registry key for both the user and the machine. If both queries return a value of 0x1, then AlwaysInstallElevated is enabled for both user and machine thus allowing a regular user to install a Microsoft Windows Installer package with system level privileges. This can be abused by an attacker to escalate privileges in the host to SYSTEM level.

## ATT&CK Mapping

- [[kb/attack/techniques/T1012-query_registry|T1012: Query Registry]]

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
reg query HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer /v AlwaysInstallElevated
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1012/T1012.yaml)
