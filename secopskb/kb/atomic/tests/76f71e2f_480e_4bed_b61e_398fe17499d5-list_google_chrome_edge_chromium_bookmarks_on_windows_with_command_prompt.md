---
atomic_guid: "76f71e2f-480e-4bed-b61e-398fe17499d5"
title: "List Google Chrome / Edge Chromium Bookmarks on Windows with command prompt"
framework: "atomic"
generated: "true"
attack_technique_id: "T1217"
attack_technique_name: "Browser Bookmark Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1217/T1217.yaml"
build_date: "2026-04-27 19:12:27"
executor: "command_prompt"
aliases:
  - "76f71e2f-480e-4bed-b61e-398fe17499d5"
  - "List Google Chrome / Edge Chromium Bookmarks on Windows with command prompt"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Searches for Google Chromes's and Edge Chromium's Bookmarks file (on Windows distributions) that contains bookmarks.
Upon execution, paths that contain bookmark files will be displayed.

## ATT&CK Mapping

- [[kb/attack/techniques/T1217-browser_information_discovery|T1217: Browser Information Discovery]]

## Executor

- name: command_prompt

### Command

```cmd
where /R C:\Users\ Bookmarks
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1217/T1217.yaml)
