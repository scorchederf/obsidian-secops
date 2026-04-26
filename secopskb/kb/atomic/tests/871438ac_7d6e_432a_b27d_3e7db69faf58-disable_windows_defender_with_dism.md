---
atomic_guid: "871438ac-7d6e-432a-b27d-3e7db69faf58"
title: "Disable Windows Defender with DISM"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.001"
attack_technique_name: "Impair Defenses: Disable or Modify Tools"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml"
build_date: "2026-04-26 17:02:13"
executor: "command_prompt"
aliases:
  - "871438ac-7d6e-432a-b27d-3e7db69faf58"
  - "Disable Windows Defender with DISM"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Disable Windows Defender with DISM

The following Atomic will attempt to disable Windows-Defender using the built in DISM.exe, Deployment Image Servicing and Management tool. 
DISM is used to enumerate, install, uninstall, configure, and update features and packages in Windows images.
A successful execution will not standard-out any details. Remove the quiet switch if verbosity is needed.
This method will remove Defender and it's package.

## Metadata

- Atomic GUID: 871438ac-7d6e-432a-b27d-3e7db69faf58
- Technique: T1562.001: Impair Defenses: Disable or Modify Tools
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1562.001/T1562.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
Dism /online /Disable-Feature /FeatureName:Windows-Defender /Remove /NoRestart /quiet
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml)
