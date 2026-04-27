---
atomic_guid: "b4115c7a-0e92-47f0-a61e-17e7218b2435"
title: "Indicator Removal using FSUtil"
framework: "atomic"
generated: "true"
attack_technique_id: "T1070"
attack_technique_name: "Indicator Removal on Host"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070/T1070.yaml"
build_date: "2026-04-27 19:12:26"
executor: "command_prompt"
aliases:
  - "b4115c7a-0e92-47f0-a61e-17e7218b2435"
  - "Indicator Removal using FSUtil"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Manages the update sequence number (USN) change journal, which provides a persistent log of all changes made to files on the volume. Upon execution, no output
will be displayed. More information about fsutil can be found at https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/fsutil-usn

## ATT&CK Mapping

- [[kb/attack/techniques/T1070-indicator_removal|T1070: Indicator Removal]]

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
fsutil usn deletejournal /D C:
```

### Cleanup

```cmd
fsutil usn createjournal m=1000 a=100 c:
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1070/T1070.yaml)
