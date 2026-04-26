---
atomic_guid: "b721c6ef-472c-4263-a0d9-37f1f4ecff66"
title: "Creating W32Time similar named service using sc"
framework: "atomic"
generated: "true"
attack_technique_id: "T1036.004"
attack_technique_name: "Masquerading: Masquerade Task or Service"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1036.004/T1036.004.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "b721c6ef-472c-4263-a0d9-37f1f4ecff66"
  - "Creating W32Time similar named service using sc"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Creating W32Time similar named service using sc

Creating W32Time similar named service (win32times) using sc just like threat actor dubbed "Operation Wocao"

## Metadata

- Atomic GUID: b721c6ef-472c-4263-a0d9-37f1f4ecff66
- Technique: T1036.004: Masquerading: Masquerade Task or Service
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1036.004/T1036.004.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1036-masquerading|T1036.004]]

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
sc create win32times binPath= "cmd /c start c:\T1036.004_NonExistingScript.ps1"
sc qc win32times
```

### Cleanup

```cmd
sc delete win32times
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1036.004/T1036.004.yaml)
