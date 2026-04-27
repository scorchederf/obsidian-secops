---
title: "Ntsd.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OtherMSBinaries/Ntsd.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Ntsd.yml"
build_date: "2026-04-27 19:14:21"
category: "OtherMSBinaries"
aliases:
  - "Ntsd.exe"
functions:
  - "Execute"
attack_technique_ids:
  - "T1127"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Symbolic Debugger for Windows.

## Paths

- `C:\Program Files (x86)\Windows Kits\10\Debuggers\x64\ntsd.exe`
- `C:\Program Files (x86)\Windows Kits\10\Debuggers\x86\ntsd.exe`
- `C:\Program Files (x86)\Windows Kits\10\Debuggers\arm\ntsd.exe`
- `C:\Program Files (x86)\Windows Kits\10\Debuggers\arm64\ntsd.exe`

## Commands

### 1. Execute

Launches command through the debugging process; optionally add `-G` to exit the debugger automatically.

```cmd
ntsd.exe -g {CMD}
```

- Use Case: Executes an executable under a trusted microsoft signed binary.
- Privileges: User
- Operating System: Windows
- ATT&CK: [[kb/attack/techniques/T1127-trusted_developer_utilities_proxy_execution|T1127: Trusted Developer Utilities Proxy Execution]]

## Resources

- {'Link': 'https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/cdb-command-line-options'}
- {'Link': 'https://strontic.github.io/xcyclopedia/library/ntsd.exe-629EA12D527237B9CD945AC44C2DE80D.html'}

## Acknowledgements

- {'Person': 'Avihay Eldad', 'Handle': '@AvihayEldad'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Ntsd.yml)
