---
atomic_guid: "faab755e-4299-48ec-8202-fc7885eb6545"
title: "List Google Chrome / Opera Bookmarks on Windows with powershell"
framework: "atomic"
generated: "true"
attack_technique_id: "T1217"
attack_technique_name: "Browser Bookmark Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1217/T1217.yaml"
build_date: "2026-04-27 19:12:27"
executor: "powershell"
aliases:
  - "faab755e-4299-48ec-8202-fc7885eb6545"
  - "List Google Chrome / Opera Bookmarks on Windows with powershell"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Searches for Google Chrome's and Opera's Bookmarks file (on Windows distributions) that contains bookmarks.
Upon execution, paths that contain bookmark files will be displayed.

## ATT&CK Mapping

- [[kb/attack/techniques/T1217-browser_information_discovery|T1217: Browser Information Discovery]]

## Executor

- name: powershell

### Command

```powershell
Get-ChildItem -Path C:\Users\ -Filter Bookmarks -Recurse -ErrorAction SilentlyContinue -Force
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1217/T1217.yaml)
