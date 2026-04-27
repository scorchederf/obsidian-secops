---
atomic_guid: "f9f2fe59-96f7-4a7d-ba9f-a9783200d4c9"
title: "Creating W32Time similar named service using schtasks"
framework: "atomic"
generated: "true"
attack_technique_id: "T1036.004"
attack_technique_name: "Masquerading: Masquerade Task or Service"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1036.004/T1036.004.yaml"
build_date: "2026-04-27 19:12:25"
executor: "command_prompt"
aliases:
  - "f9f2fe59-96f7-4a7d-ba9f-a9783200d4c9"
  - "Creating W32Time similar named service using schtasks"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Creating W32Time similar named service (win32times) using schtasks just like threat actor dubbed "Operation Wocao"

## ATT&CK Mapping

- [[kb/attack/techniques/T1036-masquerading#^t1036004-masquerade-task-or-service|T1036.004: Masquerade Task or Service]]

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
schtasks /create /ru system /sc daily /tr "cmd /c powershell.exe -ep bypass -file c:\T1036.004_NonExistingScript.ps1" /tn win32times /f
schtasks /query /tn win32times
```

### Cleanup

```cmd
schtasks /tn win32times /delete /f
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1036.004/T1036.004.yaml)
