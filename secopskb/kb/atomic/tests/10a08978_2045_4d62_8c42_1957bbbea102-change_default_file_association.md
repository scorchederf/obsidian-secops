---
atomic_guid: "10a08978-2045-4d62-8c42-1957bbbea102"
title: "Change Default File Association"
framework: "atomic"
generated: "true"
attack_technique_id: "T1546.001"
attack_technique_name: "Event Triggered Execution: Change Default File Association"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546.001/T1546.001.yaml"
build_date: "2026-04-27 19:12:27"
executor: "command_prompt"
aliases:
  - "10a08978-2045-4d62-8c42-1957bbbea102"
  - "Change Default File Association"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Change Default File Association From cmd.exe of hta to notepad.

Upon successful execution, cmd.exe will change the file association of .hta to notepad.exe.

## ATT&CK Mapping

- [[kb/attack/techniques/T1546-event_triggered_execution#^t1546001-change-default-file-association|T1546.001: Change Default File Association]]

## Input Arguments

### extension_to_change

- description: File Extension To Hijack
- type: string
- default: .hta

### original_extension_handler

- description: File Extension To Revert
- type: string
- default: htafile

### target_extension_handler

- description: txtfile maps to notepad.exe
- type: path
- default: txtfile

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
assoc #{extension_to_change}=#{target_extension_handler}
```

### Cleanup

```cmd
assoc  #{extension_to_change}=#{original_extension_handler}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1546.001/T1546.001.yaml)
