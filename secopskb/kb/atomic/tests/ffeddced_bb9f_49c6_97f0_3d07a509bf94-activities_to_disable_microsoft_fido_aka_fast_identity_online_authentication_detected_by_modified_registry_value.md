---
atomic_guid: "ffeddced-bb9f-49c6-97f0-3d07a509bf94"
title: "Activities To Disable Microsoft [FIDO Aka Fast IDentity Online] Authentication Detected By Modified Registry Value."
framework: "atomic"
generated: "true"
attack_technique_id: "T1112"
attack_technique_name: "Modify Registry"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml"
build_date: "2026-04-27 19:12:27"
executor: "command_prompt"
aliases:
  - "ffeddced-bb9f-49c6-97f0-3d07a509bf94"
  - "Activities To Disable Microsoft [FIDO Aka Fast IDentity Online] Authentication Detected By Modified Registry Value."
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detect the Microsoft FIDO authentication disable activities that adversary attempt to gains access to login credentials (e.g., passwords), they may be able to impersonate the user and access sensitive accounts or data and also increases the risk of falling victim to phishing attacks.
See the related article (https://admx.help/?Category=Windows_10_2016&Policy=Microsoft.Policies.FidoAuthentication::AllowFidoDeviceSignon).

## ATT&CK Mapping

- [[kb/attack/techniques/T1112-modify_registry|T1112: Modify Registry]]

## Executor

- name: command_prompt

### Command

```cmd
reg add "HKLM\SOFTWARE\Policies\Microsoft\FIDO" /v "AllowExternalDeviceSignon" /t REG_DWORD /d 0 /f
```

### Cleanup

```cmd
reg add "HKLM\SOFTWARE\Policies\Microsoft\FIDO" /v "AllowExternalDeviceSignon" /t REG_DWORD /d 1 /f
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml)
