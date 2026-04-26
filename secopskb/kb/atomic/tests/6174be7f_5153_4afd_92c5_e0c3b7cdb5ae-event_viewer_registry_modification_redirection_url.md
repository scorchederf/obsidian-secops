---
atomic_guid: "6174be7f-5153-4afd-92c5-e0c3b7cdb5ae"
title: "Event Viewer Registry Modification - Redirection URL"
framework: "atomic"
generated: "true"
attack_technique_id: "T1112"
attack_technique_name: "Modify Registry"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml"
build_date: "2026-04-26 14:38:40"
executor: "command_prompt"
aliases:
  - "6174be7f-5153-4afd-92c5-e0c3b7cdb5ae"
  - "Event Viewer Registry Modification - Redirection URL"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Event Viewer Registry Modification - Redirection URL

Modify event viewer registry values to alter the behavior of the online help redirection. Upon opening an event in event viewer and attempting to view the help page for the event, it will open the URL or execute the program defined in the redirection URL registry entry.

## Metadata

- Atomic GUID: 6174be7f-5153-4afd-92c5-e0c3b7cdb5ae
- Technique: T1112: Modify Registry
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1112/T1112.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1112-modify_registry|T1112]]

## Input Arguments

### redirection_url

- description: URL to open or file URI to execute upon opening the event help
- type: url
- default: file://C:\windows\system32\notepad.exe

## Executor

- elevation_required: True
- name: command_prompt

### Command

```commandprompt
reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Event Viewer" /v MicrosoftRedirectionURL /t REG_SZ /d "#{redirection_url}" /f
```

### Cleanup

```commandprompt
reg add "HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Event Viewer" /v MicrosoftRedirectionURL /t REG_SZ /d "http://go.microsoft.com/fwlink/events.asp" /f
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1112/T1112.yaml)
