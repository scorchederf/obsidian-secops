---
atomic_guid: "cfe6315c-4945-40f7-b5a4-48f7af2262af"
title: "Extract chrome Browsing History"
framework: "atomic"
generated: "true"
attack_technique_id: "T1217"
attack_technique_name: "Browser Bookmark Discovery"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1217/T1217.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "cfe6315c-4945-40f7-b5a4-48f7af2262af"
  - "Extract chrome Browsing History"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Extract chrome Browsing History

This test will extract browsing history of the chrome user

## Metadata

- Atomic GUID: cfe6315c-4945-40f7-b5a4-48f7af2262af
- Technique: T1217: Browser Bookmark Discovery
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1217/T1217.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1217-browser_information_discovery|T1217]]

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
$Username = (whoami).Split('\')[1]
$URL_Regex = '(htt(p|s))://([\w-]+\.)+[\w-]+(/[\w- ./?%&=]*)*?'
$History = Get-Content -Path "$Env:systemdrive\Users\$UserName\AppData\Local\Google\Chrome\User Data\Default\History" | Select-String -AllMatches $URL_Regex | ForEach-Object { $_.Matches.Value } | Sort -Unique
$History | Out-File -FilePath "$Env:USERPROFILE\Downloads\chromebrowsinghistory.txt"
```

### Cleanup

```powershell
Remove-Item -Path "$Env:USERPROFILE\Downloads\chromebrowsinghistory.txt"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1217/T1217.yaml)
