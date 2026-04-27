---
atomic_guid: "727dbcdb-e495-4ab1-a6c4-80c7f77aef85"
title: "List Internet Explorer Bookmarks using the command prompt"
framework: "atomic"
generated: "true"
attack_technique_id: "T1217"
attack_technique_name: "Browser Bookmark Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1217/T1217.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "727dbcdb-e495-4ab1-a6c4-80c7f77aef85"
  - "List Internet Explorer Bookmarks using the command prompt"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# List Internet Explorer Bookmarks using the command prompt

This test will list the bookmarks for Internet Explorer that are found in the Favorites folder

## Metadata

- Atomic GUID: 727dbcdb-e495-4ab1-a6c4-80c7f77aef85
- Technique: T1217: Browser Bookmark Discovery
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1217/T1217.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1217-browser_information_discovery|T1217]]

## Executor

- name: command_prompt

### Command

```cmd
dir /s /b %USERPROFILE%\Favorites
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1217/T1217.yaml)
