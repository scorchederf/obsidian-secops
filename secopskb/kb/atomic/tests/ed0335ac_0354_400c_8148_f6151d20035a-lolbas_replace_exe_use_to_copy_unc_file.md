---
atomic_guid: "ed0335ac-0354-400c-8148-f6151d20035a"
title: "Lolbas replace.exe use to copy UNC file"
framework: "atomic"
generated: "true"
attack_technique_id: "T1105"
attack_technique_name: "Ingress Tool Transfer"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1105/T1105.yaml"
build_date: "2026-04-27 19:12:27"
executor: "command_prompt"
aliases:
  - "ed0335ac-0354-400c-8148-f6151d20035a"
  - "Lolbas replace.exe use to copy UNC file"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Copy UNC file to destination
Reference: https://lolbas-project.github.io/lolbas/Binaries/Replace/

## ATT&CK Mapping

- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]]

## Input Arguments

### Path_replace

- description: Path to replace.exe
- type: path
- default: C:\Windows\System32\replace.exe

### replace_cab

- description: UNC Path to the cab file
- type: path
- default: \\127.0.0.1\c$\AtomicRedTeam\atomics\T1105\src\redcanary.cab

## Executor

- name: command_prompt

### Command

```cmd
del %TEMP%\redcanary.cab >nul 2>&1
#{Path_replace} #{replace_cab} %TEMP% /A
```

### Cleanup

```cmd
del %TEMP%\redcanary.cab >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1105/T1105.yaml)
