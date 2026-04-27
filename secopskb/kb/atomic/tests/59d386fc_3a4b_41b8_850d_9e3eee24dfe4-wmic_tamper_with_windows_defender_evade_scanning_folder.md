---
atomic_guid: "59d386fc-3a4b-41b8-850d-9e3eee24dfe4"
title: "WMIC Tamper with Windows Defender Evade Scanning Folder"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.001"
attack_technique_name: "Impair Defenses: Disable or Modify Tools"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml"
build_date: "2026-04-27 19:12:28"
executor: "command_prompt"
aliases:
  - "59d386fc-3a4b-41b8-850d-9e3eee24dfe4"
  - "WMIC Tamper with Windows Defender Evade Scanning Folder"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

The following Atomic will attempt to exclude a folder within Defender leveraging WMI
Reference: https://www.bleepingcomputer.com/news/security/gootkit-malware-bypasses-windows-defender-by-setting-path-exclusions/

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses#^t1562001-disable-or-modify-tools|T1562.001: Disable or Modify Tools]]

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
wmic.exe /Namespace:\\root\Microsoft\Windows\Defender class MSFT_MpPreference call Add ExclusionPath=\"ATOMICREDTEAM\"
```

### Cleanup

```cmd
wmic.exe /Namespace:\\root\Microsoft\Windows\Defender class MSFT_MpPreference call Remove ExclusionPath=\"ATOMICREDTEAM\"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml)
