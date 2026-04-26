---
atomic_guid: "a1230893-56ac-4c81-b644-2108e982f8f5"
title: "Disable Arbitrary Security Windows Service"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.001"
attack_technique_name: "Impair Defenses: Disable or Modify Tools"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml"
build_date: "2026-04-26 14:38:40"
executor: "command_prompt"
aliases:
  - "a1230893-56ac-4c81-b644-2108e982f8f5"
  - "Disable Arbitrary Security Windows Service"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Disable Arbitrary Security Windows Service

With administrative rights, an adversary can disable Windows Services related to security products. This test requires McAfeeDLPAgentService to be installed.
Change the service_name input argument for your AV solution. Upon exeuction, infomration will be displayed stating the status of the service.
To verify that the service has stopped, run "sc query McAfeeDLPAgentService"

## Metadata

- Atomic GUID: a1230893-56ac-4c81-b644-2108e982f8f5
- Technique: T1562.001: Impair Defenses: Disable or Modify Tools
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1562.001/T1562.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Input Arguments

### service_name

- description: The name of the service to stop
- type: string
- default: McAfeeDLPAgentService

## Executor

- elevation_required: True
- name: command_prompt

### Command

```commandprompt
net.exe stop #{service_name}
sc.exe config #{service_name} start= disabled
```

### Cleanup

```commandprompt
sc.exe config #{service_name} start= auto >nul 2>&1
net.exe start #{service_name} >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml)
