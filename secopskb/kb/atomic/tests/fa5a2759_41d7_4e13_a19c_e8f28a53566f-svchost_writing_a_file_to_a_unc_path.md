---
atomic_guid: "fa5a2759-41d7-4e13-a19c-e8f28a53566f"
title: "svchost writing a file to a UNC path"
framework: "atomic"
generated: "true"
attack_technique_id: "T1105"
attack_technique_name: "Ingress Tool Transfer"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1105/T1105.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "fa5a2759-41d7-4e13-a19c-e8f28a53566f"
  - "svchost writing a file to a UNC path"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# svchost writing a file to a UNC path

svchost.exe writing a non-Microsoft Office file to a file with a UNC path.
Upon successful execution, this will rename cmd.exe as svchost.exe and move it to `c:\`, then execute svchost.exe with output to a txt file.

## Metadata

- Atomic GUID: fa5a2759-41d7-4e13-a19c-e8f28a53566f
- Technique: T1105: Ingress Tool Transfer
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1105/T1105.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
copy C:\Windows\System32\cmd.exe C:\svchost.exe
C:\svchost.exe /c echo T1105 > \\localhost\c$\T1105.txt
```

### Cleanup

```cmd
del C:\T1105.txt >nul 2>&1
del C:\\svchost.exe >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1105/T1105.yaml)
