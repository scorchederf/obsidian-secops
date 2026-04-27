---
title: "Zipfldr.dll"
framework: "lolbas"
generated: "true"
source_path: "yml/OSLibraries/Zipfldr.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSLibraries/Zipfldr.yml"
build_date: "2026-04-27 19:14:21"
category: "OSLibraries"
aliases:
  - "Zipfldr.dll"
functions:
  - "Execute"
attack_technique_ids:
  - "T1218.011"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Compressed Folder library

## Paths

- `c:\windows\system32\zipfldr.dll`
- `c:\windows\syswow64\zipfldr.dll`

## Commands

### 1. Execute

Launch an executable payload by calling RouteTheCall.

```cmd
rundll32.exe zipfldr.dll,RouteTheCall {PATH:.exe}
```

- Use Case: Launch an executable.
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution#^t1218011-rundll32|T1218.011: Rundll32]]

### 2. Execute

Launch an executable payload by calling RouteTheCall (obfuscated).

```cmd
rundll32.exe zipfldr.dll,RouteTheCall file://^C^:^/^W^i^n^d^o^w^s^/^s^y^s^t^e^m^3^2^/^c^a^l^c^.^e^x^e
```

- Use Case: Launch an executable.
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution#^t1218011-rundll32|T1218.011: Rundll32]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_rundll32_susp_activity.yml

## Resources

- {'Link': 'https://twitter.com/moriarty_meng/status/977848311603380224'}
- {'Link': 'https://twitter.com/bohops/status/997896811904929792'}
- {'Link': 'https://windows10dll.nirsoft.net/zipfldr_dll.html'}

## Acknowledgements

- {'Person': 'Moriarty (Execution)', 'Handle': '@moriarty_meng'}
- {'Person': 'r0lan (Obfuscation)', 'Handle': '@r0lan'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSLibraries/Zipfldr.yml)
