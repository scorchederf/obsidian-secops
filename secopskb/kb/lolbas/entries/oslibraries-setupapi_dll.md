---
title: "Setupapi.dll"
framework: "lolbas"
generated: "true"
source_path: "yml/OSLibraries/Setupapi.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSLibraries/Setupapi.yml"
build_date: "2026-04-27 19:14:21"
category: "OSLibraries"
aliases:
  - "Setupapi.dll"
functions:
  - "AWL Bypass"
  - "Execute"
attack_technique_ids:
  - "T1218.011"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Windows Setup Application Programming Interface

## Paths

- `c:\windows\system32\setupapi.dll`
- `c:\windows\syswow64\setupapi.dll`

## Commands

### 1. AWL Bypass

Execute the specified (local or remote) .wsh/.sct script with scrobj.dll in the .inf file by calling an information file directive (section name specified).

```cmd
rundll32.exe setupapi.dll,InstallHinfSection DefaultInstall 128 {PATH_ABSOLUTE:.inf}
```

- Use Case: Run local or remote script(let) code through INF file specification.
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution#^t1218011-rundll32|T1218.011: Rundll32]]

### 2. Execute

Launch an executable file via the InstallHinfSection function and .inf file section directive.

```cmd
rundll32.exe setupapi.dll,InstallHinfSection DefaultInstall 128 {PATH_ABSOLUTE:.inf}
```

- Use Case: Load an executable payload.
- Privileges: User
- Operating System: Windows
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution#^t1218011-rundll32|T1218.011: Rundll32]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_rundll32_setupapi_installhinfsection.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_rundll32_susp_activity.yml
- Splunk: https://github.com/splunk/security_content/blob/86a5b644a44240f01274c8b74d19a435c7dae66e/detections/endpoint/detect_rundll32_application_control_bypass___setupapi.yml

## Resources

- {'Link': 'https://github.com/huntresslabs/evading-autoruns'}
- {'Link': 'https://twitter.com/pabraeken/status/994742106852941825'}
- {'Link': 'https://windows10dll.nirsoft.net/setupapi_dll.html'}

## Acknowledgements

- {'Person': 'Kyle Hanslovan (COM Scriptlet)', 'Handle': '@KyleHanslovan'}
- {'Person': 'Huntress Labs (COM Scriptlet)', 'Handle': '@HuntressLabs'}
- {'Person': 'Casey Smith (COM Scriptlet)', 'Handle': '@subTee'}
- {'Person': 'Nick Carr (Threat Intel)', 'Handle': '@ItsReallyNick'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSLibraries/Setupapi.yml)
