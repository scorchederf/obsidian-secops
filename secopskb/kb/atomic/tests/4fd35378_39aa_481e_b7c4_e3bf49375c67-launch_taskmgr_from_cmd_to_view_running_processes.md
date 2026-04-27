---
atomic_guid: "4fd35378-39aa-481e-b7c4-e3bf49375c67"
title: "Launch Taskmgr from cmd to View running processes"
framework: "atomic"
generated: "true"
attack_technique_id: "T1057"
attack_technique_name: "Process Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1057/T1057.yaml"
build_date: "2026-04-27 19:12:26"
executor: "command_prompt"
aliases:
  - "4fd35378-39aa-481e-b7c4-e3bf49375c67"
  - "Launch Taskmgr from cmd to View running processes"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

An adverary may launch taskmgr.exe with the /7 switch via command prompt to view processes running on the system.
[Reference](https://github.com/trellix-enterprise/ac3-threat-sightings/blob/main/sightings/Sightings_Conti_Ransomware.yml)

## ATT&CK Mapping

- [[kb/attack/techniques/T1057-process_discovery|T1057: Process Discovery]]

## Executor

- elevation_required: False
- name: command_prompt

### Command

```cmd
taskmgr.exe /7
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1057/T1057.yaml)
