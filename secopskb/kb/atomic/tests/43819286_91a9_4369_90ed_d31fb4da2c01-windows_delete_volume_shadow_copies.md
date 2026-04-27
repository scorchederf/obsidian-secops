---
atomic_guid: "43819286-91a9-4369-90ed-d31fb4da2c01"
title: "Windows - Delete Volume Shadow Copies"
framework: "atomic"
generated: "true"
attack_technique_id: "T1490"
attack_technique_name: "Inhibit System Recovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1490/T1490.yaml"
build_date: "2026-04-27 19:12:27"
executor: "command_prompt"
aliases:
  - "43819286-91a9-4369-90ed-d31fb4da2c01"
  - "Windows - Delete Volume Shadow Copies"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Deletes Windows Volume Shadow Copies. This technique is used by numerous ransomware families and APT malware such as Olympic Destroyer. Upon
execution, if no shadow volumes exist the message "No items found that satisfy the query." will be displayed. If shadow volumes are present, it
will delete them without printing output to the screen. This is because the /quiet parameter was passed which also suppresses the y/n
confirmation prompt. Shadow copies can only be created on Windows server or Windows 8.

https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-R2-and-2012/cc788055(v=ws.11)

## ATT&CK Mapping

- [[kb/attack/techniques/T1490-inhibit_system_recovery|T1490: Inhibit System Recovery]]

## Dependencies

Create volume shadow copy of C:\ . This prereq command only works on Windows Server or Windows 8.

### Prerequisite Check

```powershell
if(!(vssadmin.exe list shadows | findstr "No items found that satisfy the query.")) { exit 0 } else { exit 1 }
```

### Get Prerequisite

```powershell
vssadmin.exe create shadow /for=c:
```

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
vssadmin.exe delete shadows /all /quiet
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1490/T1490.yaml)
