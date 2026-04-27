---
atomic_guid: "16bdbe52-371c-4ccf-b708-79fba61f1db4"
title: "Enable RDP via Registry (fDenyTSConnections)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1112"
attack_technique_name: "Modify Registry"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "16bdbe52-371c-4ccf-b708-79fba61f1db4"
  - "Enable RDP via Registry (fDenyTSConnections)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Enable RDP via Registry (fDenyTSConnections)

Modify the registry value of fDenyTSConnections to allow incoming RDP connections. 
This activity has been observed by multiple ransomware groups, including Hive ransomware. 
[Reference](https://www.rapid7.com/blog/post/2023/01/11/increasing-the-sting-of-hive-ransomware/)

## Metadata

- Atomic GUID: 16bdbe52-371c-4ccf-b708-79fba61f1db4
- Technique: T1112: Modify Registry
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1112/T1112.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1112-modify_registry|T1112]]

## Input Arguments

### remove_rdp_access_during_cleanup

- description: Set to 1 if you want the cleanup to remove RDP access to machine
- type: integer
- default: 0

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
reg add "HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0 /f
```

### Cleanup

```cmd
if #{remove_rdp_access_during_cleanup} EQU 1 (reg delete "HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /f >nul 2>&1)
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml)
