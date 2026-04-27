---
atomic_guid: "74094120-e1f5-47c9-b162-a418a0f624d5"
title: "Extract Edge Browsing History"
framework: "atomic"
generated: "true"
attack_technique_id: "T1217"
attack_technique_name: "Browser Bookmark Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1217/T1217.yaml"
build_date: "2026-04-27 19:12:27"
executor: "powershell"
aliases:
  - "74094120-e1f5-47c9-b162-a418a0f624d5"
  - "Extract Edge Browsing History"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

This test will extract Microsoft Edge browser's history of current user

## ATT&CK Mapping

- [[kb/attack/techniques/T1217-browser_information_discovery|T1217: Browser Information Discovery]]

## Input Arguments

### dest_path

- description: Target file path to where the history to be extracted
- type: String
- default: $Env:USERPROFILE\Downloads\edgebrowsinghistory.txt

### history_path

- description: Microsoft Edge browser history file path
- type: String
- default: $Env:LOCALAPPDATA\Microsoft\Edge\User Data\Default\History

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
$URL_Regex = '(htt(p|s))://([\w-]+\.)+[\w-]+(/[\w- ./?%&=]*)*?'
$History = Get-Content -Path "#{history_path}" | Select-String -AllMatches $URL_Regex | ForEach-Object { $_.Matches.Value } | Sort -Unique
$History | Out-File -FilePath "#{dest_path}"
```

### Cleanup

```powershell
Remove-Item -Path "#{dest_path}"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1217/T1217.yaml)
