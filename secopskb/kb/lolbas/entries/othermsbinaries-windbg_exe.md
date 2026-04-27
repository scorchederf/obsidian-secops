---
title: "WinDbg.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OtherMSBinaries/WinDbg.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/WinDbg.yml"
build_date: "2026-04-27 19:14:21"
category: "OtherMSBinaries"
aliases:
  - "WinDbg.exe"
functions:
  - "Execute"
attack_technique_ids:
  - "T1127"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Windows Debugger for advanced user-mode and kernel-mode debugging.

## Paths

- `C:\Program Files (x86)\Windows Kits\10\Debuggers\x64\windbg.exe`
- `C:\Program Files (x86)\Windows Kits\10\Debuggers\x86\windbg.exe`
- `C:\Program Files (x86)\Windows Kits\10\Debuggers\arm\windbg.exe`
- `C:\Program Files (x86)\Windows Kits\10\Debuggers\arm64\windbg.exe`

## Commands

### 1. Execute

Launches a command line through the debugging process; optionally add `-G` to exit the debugger automatically.

```cmd
windbg.exe -g {CMD}
```

- Use Case: Executes an executable under a trusted microsoft signed binary.
- Privileges: User
- Operating System: Windows
- ATT&CK: [[kb/attack/techniques/T1127-trusted_developer_utilities_proxy_execution|T1127: Trusted Developer Utilities Proxy Execution]]

## Resources

- {'Link': 'https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/windbg-command-line-options'}

## Acknowledgements

- {'Person': 'Avihay Eldad', 'Handle': '@AvihayEldad'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/WinDbg.yml)
