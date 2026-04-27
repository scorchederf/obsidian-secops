---
title: "Dxcap.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OtherMSBinaries/Dxcap.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Dxcap.yml"
build_date: "2026-04-27 19:14:21"
category: "OtherMSBinaries"
aliases:
  - "Dxcap.exe"
functions:
  - "Execute"
attack_technique_ids:
  - "T1127"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

DirectX diagnostics/debugger included with Visual Studio.

## Paths

- `C:\Windows\System32\dxcap.exe`
- `C:\Windows\SysWOW64\dxcap.exe`

## Commands

### 1. Execute

Launch specified executable as a subprocess of dxcap.exe. Note that you should have write permissions in the current working directory for the command to succeed; alternatively, add '-file c:\path\to\writable\location.ext' as first argument.

```cmd
Dxcap.exe -c {PATH_ABSOLUTE:.exe}
```

- Use Case: Local execution of a process as a subprocess of dxcap.exe
- Privileges: User
- Operating System: Windows
- ATT&CK: [[kb/attack/techniques/T1127-trusted_developer_utilities_proxy_execution|T1127: Trusted Developer Utilities Proxy Execution]]

### 2. Execute

Once executed, `dxcap.exe` will execute `xperf.exe` in the same folder. Thus, if `dxcap.exe` is copied to a folder and an arbitrary executable is renamed to `xperf.exe`, `dxcap.exe` will spawn it.

```cmd
dxcap.exe -usage
```

- Use Case: Execute an arbitrary executable via trusted system executable.
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1127-trusted_developer_utilities_proxy_execution|T1127: Trusted Developer Utilities Proxy Execution]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_susp_dxcap.yml
- IOC: dxcap.exe executing from outside of System32/SysWOW64
- IOC: dxcap.exe spawning Xperf.exe
- IOC: Xperf.exe executing from unusual directories (if not running from ADK path)

## Resources

- {'Link': 'https://twitter.com/harr0ey/status/992008180904419328'}

## Acknowledgements

- {'Person': 'Matt harr0ey', 'Handle': '@harr0ey'}
- {'Person': 'Vikas Singh', 'Handle': '@vikas891'}
- {'Person': 'Naor Evgi', 'Handle': '@ghosts621'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Dxcap.yml)
