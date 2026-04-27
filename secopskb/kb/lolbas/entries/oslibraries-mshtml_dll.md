---
title: "Mshtml.dll"
framework: "lolbas"
generated: "true"
source_path: "yml/OSLibraries/Mshtml.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSLibraries/Mshtml.yml"
build_date: "2026-04-27 19:14:21"
category: "OSLibraries"
aliases:
  - "Mshtml.dll"
functions:
  - "Execute"
attack_technique_ids:
  - "T1218.011"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Microsoft HTML Viewer

## Paths

- `c:\windows\system32\mshtml.dll`
- `c:\windows\syswow64\mshtml.dll`

## Commands

### 1. Execute

Invoke an HTML Application via mshta.exe (note: pops a security warning and a print dialogue box).

```cmd
rundll32.exe Mshtml.dll,PrintHTML {PATH_ABSOLUTE:.hta}
```

- Use Case: Launch an HTA application.
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution#^t1218011-rundll32|T1218.011: Rundll32]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_rundll32_susp_activity.yml

## Resources

- {'Link': 'https://twitter.com/pabraeken/status/998567549670477824'}
- {'Link': 'https://windows10dll.nirsoft.net/mshtml_dll.html'}

## Acknowledgements

- {'Person': 'Pierre-Alexandre Braeken', 'Handle': '@pabraeken'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSLibraries/Mshtml.yml)
