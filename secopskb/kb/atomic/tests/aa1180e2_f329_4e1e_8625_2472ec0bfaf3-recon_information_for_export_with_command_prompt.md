---
atomic_guid: "aa1180e2-f329-4e1e-8625-2472ec0bfaf3"
title: "Recon information for export with Command Prompt"
framework: "atomic"
generated: "true"
attack_technique_id: "T1119"
attack_technique_name: "Automated Collection"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1119/T1119.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "aa1180e2-f329-4e1e-8625-2472ec0bfaf3"
  - "Recon information for export with Command Prompt"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Recon information for export with Command Prompt

collect information for exfiltration. Upon execution, check the users temp directory (%temp%) for files T1119_*.txt
to see what was collected.

## Metadata

- Atomic GUID: aa1180e2-f329-4e1e-8625-2472ec0bfaf3
- Technique: T1119: Automated Collection
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1119/T1119.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1119-automated_collection|T1119]]

## Executor

- name: command_prompt

### Command

```cmd
sc query type=service > %TEMP%\T1119_1.txt
doskey /history > %TEMP%\T1119_2.txt
wmic process list > %TEMP%\T1119_3.txt
tree C:\AtomicRedTeam\atomics > %TEMP%\T1119_4.txt
```

### Cleanup

```cmd
del %TEMP%\T1119_1.txt >nul 2>&1
del %TEMP%\T1119_2.txt >nul 2>&1
del %TEMP%\T1119_3.txt >nul 2>&1
del %TEMP%\T1119_4.txt >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1119/T1119.yaml)
