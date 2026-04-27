---
title: "Microsoft.NodejsTools.PressAnyKey.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OtherMSBinaries/Microsoft.NodejsTools.PressAnyKey.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Microsoft.NodejsTools.PressAnyKey.yml"
build_date: "2026-04-27 18:39:01"
category: "OtherMSBinaries"
aliases:
  - "Microsoft.NodejsTools.PressAnyKey.exe"
functions:
  - "Execute"
attack_technique_ids:
  - "T1127"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Microsoft.NodejsTools.PressAnyKey.exe

Part of the NodeJS Visual Studio tools.

## Metadata

- Category: OtherMSBinaries
- Created: 2022-01-20
- Author: mr.d0x
- Source Path: yml/OtherMSBinaries/Microsoft.NodejsTools.PressAnyKey.yml

## Paths

- `C:\Program Files\Microsoft Visual Studio\<version>\Community\Common7\IDE\Extensions\Microsoft\NodeJsTools\NodeJsTools\Microsoft.NodejsTools.PressAnyKey.exe`
- `C:\Program Files (x86)\Microsoft Visual Studio\<version>\Community\Common7\IDE\Extensions\Microsoft\NodeJsTools\NodeJsTools\Microsoft.NodejsTools.PressAnyKey.exe`

## Commands

### 1. Execute

Launch specified executable as a subprocess of Microsoft.NodejsTools.PressAnyKey.exe.

```cmd
Microsoft.NodejsTools.PressAnyKey.exe normal 1 {PATH:.exe}
```

- Use Case: Spawn a new process via Microsoft.NodejsTools.PressAnyKey.exe.
- Privileges: User
- Operating System: Windows
- ATT&CK: [[kb/attack/techniques/T1127-trusted_developer_utilities_proxy_execution|T1127]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/b02e3b698afbaae143ac4fb36236eb0b41122ed7/rules/windows/process_creation/proc_creation_win_renamed_pressanykey.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/b02e3b698afbaae143ac4fb36236eb0b41122ed7/rules/windows/process_creation/proc_creation_win_pressanykey_lolbin_execution.yml

## Resources

- {'Link': 'https://twitter.com/mrd0x/status/1463526834918854661'}

## Acknowledgements

- {'Person': 'mr.d0x', 'Handle': '@mrd0x'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Microsoft.NodejsTools.PressAnyKey.yml)
