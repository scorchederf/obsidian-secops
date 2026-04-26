---
atomic_guid: "99c657aa-ebeb-4179-a665-69288fdd12b8"
title: "Disable Administrative Share Creation at Startup"
framework: "atomic"
generated: "true"
attack_technique_id: "T1070.005"
attack_technique_name: "Indicator Removal on Host: Network Share Connection Removal"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.005/T1070.005.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "99c657aa-ebeb-4179-a665-69288fdd12b8"
  - "Disable Administrative Share Creation at Startup"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Disable Administrative Share Creation at Startup

Administrative shares are hidden network shares created by Microsoft’s Windows NT operating systems that grant system administrators 
remote access to every disk volume on a network-connected system. These shares are automatically created at started unless they have been
purposefully disabled as is done in this Atomic test. As Microsoft puts it, "Missing administrative shares typically 
indicate that the computer in question has been compromised by malicious software."
https://threatpost.com/conti-ransomware-gang-has-full-log4shell-attack-chain/177173/

## Metadata

- Atomic GUID: 99c657aa-ebeb-4179-a665-69288fdd12b8
- Technique: T1070.005: Indicator Removal on Host: Network Share Connection Removal
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1070.005/T1070.005.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1070-indicator_removal|T1070.005]]

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters" /v AutoShareServer /t REG_DWORD /d 0 /f
reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters" /v AutoShareWks /t REG_DWORD /d 0 /f
```

### Cleanup

```cmd
reg delete "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters" /v AutoShareServer /f
reg delete "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters" /v AutoShareWks /f
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070.005/T1070.005.yaml)
