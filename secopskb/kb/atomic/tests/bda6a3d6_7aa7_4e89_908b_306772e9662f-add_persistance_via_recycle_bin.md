---
atomic_guid: "bda6a3d6-7aa7-4e89-908b-306772e9662f"
title: "Add persistance via Recycle bin"
framework: "atomic"
generated: "true"
attack_technique_id: "T1547.001"
attack_technique_name: "Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547.001/T1547.001.yaml"
build_date: "2026-04-26 17:02:13"
executor: "command_prompt"
aliases:
  - "bda6a3d6-7aa7-4e89-908b-306772e9662f"
  - "Add persistance via Recycle bin"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Add persistance via Recycle bin

Add a persistance via Recycle bin [vxunderground](https://github.com/vxunderground/VXUG-Papers/blob/main/The%20Persistence%20Series/Persistence%20via%20Recycle%20Bin/Persistence_via_Recycle_Bin.pdf)
User have to clic on the recycle bin to lauch the payload (here calc)

## Metadata

- Atomic GUID: bda6a3d6-7aa7-4e89-908b-306772e9662f
- Technique: T1547.001: Boot or Logon Autostart Execution: Registry Run Keys / Startup Folder
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1547.001/T1547.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547.001]]

## Executor

- name: command_prompt

### Command

```cmd
reg ADD "HKCR\CLSID\{645FF040-5081-101B-9F08-00AA002F954E}\shell\open\command" /ve /d "calc.exe" /f
```

### Cleanup

```cmd
reg DELETE "HKCR\CLSID\{645FF040-5081-101B-9F08-00AA002F954E}\shell\open" /f
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1547.001/T1547.001.yaml)
