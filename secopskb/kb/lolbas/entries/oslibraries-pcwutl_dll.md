---
title: "Pcwutl.dll"
framework: "lolbas"
generated: "true"
source_path: "yml/OSLibraries/Pcwutl.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSLibraries/Pcwutl.yml"
build_date: "2026-04-27 19:14:21"
category: "OSLibraries"
aliases:
  - "Pcwutl.dll"
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

- `c:\windows\system32\pcwutl.dll`
- `c:\windows\syswow64\pcwutl.dll`

## Commands

### 1. Execute

Launch executable by calling the LaunchApplication function.

```cmd
rundll32.exe pcwutl.dll,LaunchApplication {PATH:.exe}
```

- Use Case: Launch an executable.
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution#^t1218011-rundll32|T1218.011: Rundll32]]

## Detections

- Analysis: https://redcanary.com/threat-detection-report/techniques/rundll32/
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_rundll32_susp_activity.yml

## Resources

- {'Link': 'https://twitter.com/harr0ey/status/989617817849876488'}
- {'Link': 'https://windows10dll.nirsoft.net/pcwutl_dll.html'}

## Acknowledgements

- {'Person': 'Matt harr0ey', 'Handle': '@harr0ey'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSLibraries/Pcwutl.yml)
