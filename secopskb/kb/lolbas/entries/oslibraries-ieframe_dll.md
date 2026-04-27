---
title: "Ieframe.dll"
framework: "lolbas"
generated: "true"
source_path: "yml/OSLibraries/Ieframe.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSLibraries/Ieframe.yml"
build_date: "2026-04-27 19:14:21"
category: "OSLibraries"
aliases:
  - "Ieframe.dll"
functions:
  - "Execute"
attack_technique_ids:
  - "T1218.011"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Internet Browser DLL for translating HTML code.

## Paths

- `c:\windows\system32\ieframe.dll`
- `c:\windows\syswow64\ieframe.dll`

## Commands

### 1. Execute

Launch an executable payload via proxy through a(n) URL (information) file by calling OpenURL.

```cmd
rundll32.exe ieframe.dll,OpenURL {PATH_ABSOLUTE:.url}
```

- Use Case: Load an executable payload by calling a .url file with or without quotes. The .url file extension can be renamed.
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution#^t1218011-rundll32|T1218.011: Rundll32]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_rundll32_susp_activity.yml

## Resources

- {'Link': 'http://www.hexacorn.com/blog/2018/03/15/running-programs-via-proxy-jumping-on-a-edr-bypass-trampoline-part-5/'}
- {'Link': 'https://bohops.com/2018/03/17/abusing-exported-functions-and-exposed-dcom-interfaces-for-pass-thru-command-execution-and-lateral-movement/'}
- {'Link': 'https://twitter.com/bohops/status/997690405092290561'}
- {'Link': 'https://windows10dll.nirsoft.net/ieframe_dll.html'}

## Acknowledgements

- {'Person': 'Jimmy', 'Handle': '@bohops'}
- {'Person': 'Adam', 'Handle': '@hexacorn'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSLibraries/Ieframe.yml)
