---
atomic_guid: "6b2903ac-8f36-450d-9ad5-b220e8a2dcb9"
title: "Simulate BlackByte Ransomware Print Bombing"
framework: "atomic"
generated: "true"
attack_technique_id: "T1059.003"
attack_technique_name: "Command and Scripting Interpreter: Windows Command Shell"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.003/T1059.003.yaml"
build_date: "2026-04-26 14:38:39"
executor: "powershell"
aliases:
  - "6b2903ac-8f36-450d-9ad5-b220e8a2dcb9"
  - "Simulate BlackByte Ransomware Print Bombing"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Simulate BlackByte Ransomware Print Bombing

This test attempts to open a file a specified number of times in Wordpad, then prints the contents. 
It is designed to mimic BlackByte ransomware's print bombing technique, where tree.dll, which contains the ransom note, is opened in Wordpad 75 times and then printed. 
See https://redcanary.com/blog/blackbyte-ransomware/.

## Metadata

- Atomic GUID: 6b2903ac-8f36-450d-9ad5-b220e8a2dcb9
- Technique: T1059.003: Command and Scripting Interpreter: Windows Command Shell
- Platforms: windows
- Executor: powershell
- Dependency Executor: powershell
- Source Path: atomics/T1059.003/T1059.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.003]]

## Input Arguments

### file_to_print

- description: File to be opened/printed by Wordpad.
- type: string
- default: PathToAtomicsFolder\..\ExternalPayloads\T1059_003note.txt

### max_to_print

- description: The maximum number of Wordpad windows the test will open/print.
- type: integer
- default: 75

## Dependencies

File to print must exist on disk at specified location (#{file_to_print})

### Prerequisite Check

```text
if (test-path "#{file_to_print}"){exit 0} else {exit 1}
```

### Get Prerequisite

```text
new-item "#{file_to_print}" -value "This file has been created by T1059.003 Test 4" -Force | Out-Null
```

## Executor

- name: powershell

### Command

```powershell
cmd /c "for /l %x in (1,1,#{max_to_print}) do start wordpad.exe /p #{file_to_print}" | out-null
```

### Cleanup

```powershell
stop-process -name wordpad -force -erroraction silentlycontinue
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1059.003/T1059.003.yaml)
