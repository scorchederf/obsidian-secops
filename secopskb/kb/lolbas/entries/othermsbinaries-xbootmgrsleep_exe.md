---
title: "XBootMgrSleep.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OtherMSBinaries/XBootMgrSleep.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/XBootMgrSleep.yml"
build_date: "2026-04-27 19:14:21"
category: "OtherMSBinaries"
aliases:
  - "XBootMgrSleep.exe"
functions:
  - "Execute"
attack_technique_ids:
  - "T1202"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Windows Performance Toolkit binary used for tracing and analyzing system performance during sleep and resume transitions.

## Paths

- `C:\Program Files\Windows Kits\10\Windows Performance Toolkit\xbootmgrsleep.exe`
- `C:\Program Files (x86)\Windows Kits\10\Windows Performance Toolkit\xbootmgrsleep.exe`

## Commands

### 1. Execute

Execute executable via XBootMgrSleep, with a 1 second (=1000 milliseconds) delay. Alternatively, it is also possible to replace the delay with any string for immediate execution.

```cmd
xbootmgrsleep.exe 1000 {PATH:.exe}
```

- Use Case: Performs execution of specified executable, can be used as a defense evasion
- Privileges: User
- Operating System: Windows
- ATT&CK: [[kb/attack/techniques/T1202-indirect_command_execution|T1202: Indirect Command Execution]]

## Resources

- {'Link': 'https://learn.microsoft.com/en-us/previous-versions/windows/desktop/xperf/reference'}

## Acknowledgements

- {'Person': 'Avihay Eldad', 'Handle': '@AvihayEldad'}
- {'Person': 'Yuval Saban', 'Handle': '@yuvalsaban3'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/XBootMgrSleep.yml)
