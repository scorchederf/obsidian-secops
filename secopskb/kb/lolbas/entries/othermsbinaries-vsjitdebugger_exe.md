---
title: "vsjitdebugger.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OtherMSBinaries/Vsjitdebugger.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Vsjitdebugger.yml"
build_date: "2026-04-27 19:14:21"
category: "OtherMSBinaries"
aliases:
  - "vsjitdebugger.exe"
functions:
  - "Execute"
attack_technique_ids:
  - "T1127"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Just-In-Time (JIT) debugger included with Visual Studio

## Paths

- `c:\windows\system32\vsjitdebugger.exe`

## Commands

### 1. Execute

Executes specified executable as a subprocess of Vsjitdebugger.exe.

```cmd
Vsjitdebugger.exe {PATH:.exe}
```

- Use Case: Execution of local PE file as a subprocess of Vsjitdebugger.exe.
- Privileges: User
- Operating System: Windows
- ATT&CK: [[kb/attack/techniques/T1127-trusted_developer_utilities_proxy_execution|T1127: Trusted Developer Utilities Proxy Execution]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_susp_use_of_vsjitdebugger_bin.yml

## Resources

- {'Link': 'https://twitter.com/pabraeken/status/990758590020452353'}

## Acknowledgements

- {'Person': 'Pierre-Alexandre Braeken', 'Handle': '@pabraeken'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Vsjitdebugger.yml)
