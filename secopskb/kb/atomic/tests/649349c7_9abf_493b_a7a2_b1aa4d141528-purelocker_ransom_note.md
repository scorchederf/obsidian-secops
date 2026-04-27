---
atomic_guid: "649349c7-9abf-493b-a7a2-b1aa4d141528"
title: "PureLocker Ransom Note"
framework: "atomic"
generated: "true"
attack_technique_id: "T1486"
attack_technique_name: "Data Encrypted for Impact"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1486/T1486.yaml"
build_date: "2026-04-27 19:12:27"
executor: "command_prompt"
aliases:
  - "649349c7-9abf-493b-a7a2-b1aa4d141528"
  - "PureLocker Ransom Note"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

building the IOC (YOUR_FILES.txt) for the PureLocker ransomware 
https://www.bleepingcomputer.com/news/security/purelocker-ransomware-can-lock-files-on-windows-linux-and-macos/

## ATT&CK Mapping

- [[kb/attack/techniques/T1486-data_encrypted_for_impact|T1486: Data Encrypted for Impact]]

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
echo T1486 - Purelocker Ransom Note > %USERPROFILE%\Desktop\YOUR_FILES.txt
```

### Cleanup

```cmd
del %USERPROFILE%\Desktop\YOUR_FILES.txt >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1486/T1486.yaml)
