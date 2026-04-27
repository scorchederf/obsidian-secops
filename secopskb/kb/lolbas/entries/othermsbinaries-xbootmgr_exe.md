---
title: "XBootMgr.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OtherMSBinaries/XBootMgr.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/XBootMgr.yml"
build_date: "2026-04-27 19:14:21"
category: "OtherMSBinaries"
aliases:
  - "XBootMgr.exe"
functions:
  - "Execute"
attack_technique_ids:
  - "T1202"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Windows Performance Toolkit binary used to start performance traces.

## Paths

- `C:\Program Files\Windows Kits\10\Windows Performance Toolkit\xbootmgr.exe`
- `C:\Program Files (x86)\Windows Kits\10\Windows Performance Toolkit\xbootmgr.exe`

## Commands

### 1. Execute

Executes an executable after the trace is complete using the callBack parameter.

```cmd
xbootmgr.exe -trace "{boot|hibernate|standby|shutdown|rebootCycle}" -callBack {PATH:.exe}
```

- Use Case: Executes code as part of post-trace automation flow.
- Privileges: Administrator
- Operating System: Windows
- ATT&CK: [[kb/attack/techniques/T1202-indirect_command_execution|T1202: Indirect Command Execution]]

### 2. Execute

Executes an executable before each trace run using the preTraceCmd parameter.

```cmd
xbootmgr.exe -trace "{boot|hibernate|standby|shutdown|rebootCycle}" -preTraceCmd {PATH:.exe}
```

- Use Case: Executes code as part of pre-trace automation or staging.
- Privileges: Administrator
- Operating System: Windows
- ATT&CK: [[kb/attack/techniques/T1202-indirect_command_execution|T1202: Indirect Command Execution]]

## Resources

- {'Link': 'https://learn.microsoft.com/en-us/previous-versions/windows/desktop/xperf/reference'}

## Acknowledgements

- {'Person': 'Avihay Eldad', 'Handle': '@AvihayEldad'}
- {'Person': 'Tommy Warren'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/XBootMgr.yml)
