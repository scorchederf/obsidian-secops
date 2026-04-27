---
title: "te.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OtherMSBinaries/Te.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Te.yml"
build_date: "2026-04-27 19:14:21"
category: "OtherMSBinaries"
aliases:
  - "te.exe"
functions:
  - "Execute"
attack_technique_ids:
  - "T1127"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Testing tool included with Microsoft Test Authoring and Execution Framework (TAEF).

## Paths

- `no default`

## Commands

### 1. Execute

Run COM Scriptlets (e.g. VBScript) by calling a Windows Script Component (WSC) file.

```cmd
te.exe {PATH:.wsc}
```

- Use Case: Execute Visual Basic script stored in local Windows Script Component file.
- Privileges: User
- Operating System: Windows
- ATT&CK: [[kb/attack/techniques/T1127-trusted_developer_utilities_proxy_execution|T1127: Trusted Developer Utilities Proxy Execution]]

### 2. Execute

Execute commands from a DLL file with Test Authoring and Execution Framework (TAEF) tests. See resources section for required structures.

```cmd
te.exe {PATH:.dll}
```

- Use Case: Execute DLL file.
- Privileges: User
- Operating System: Windows
- ATT&CK: [[kb/attack/techniques/T1127-trusted_developer_utilities_proxy_execution|T1127: Trusted Developer Utilities Proxy Execution]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_susp_use_of_te_bin.yml

## Resources

- {'Link': 'https://twitter.com/gn3mes1s/status/927680266390384640'}
- {'Link': 'https://github.com/LOLBAS-Project/LOLBAS/pull/359'}
- {'Link': 'https://learn.microsoft.com/en-us/windows-hardware/drivers/taef/authoring-tests'}

## Acknowledgements

- {'Person': 'Giuseppe N3mes1s', 'Handle': '@gN3mes1s'}
- {'Person': 'Avihay Eldad', 'Handle': '@AvihayEldad'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Te.yml)
