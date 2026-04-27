---
title: "vstest.console.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OtherMSBinaries/vstest.console.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/vstest.console.yml"
build_date: "2026-04-27 19:14:21"
category: "OtherMSBinaries"
aliases:
  - "vstest.console.exe"
functions:
  - "AWL Bypass"
attack_technique_ids:
  - "T1127"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

VSTest.Console.exe is the command-line tool to run tests

## Paths

- `C:\Program Files\Microsoft Visual Studio\2022\Community\Common7\IDE\CommonExtensions\Microsoft\TestWindow\vstest.console.exe`
- `C:\Program Files (x86)\Microsoft Visual Studio\2022\TestAgent\Common7\IDE\CommonExtensions\Microsoft\TestWindow\vstest.console.exe`

## Commands

### 1. AWL Bypass

VSTest functionality may allow an adversary to executes their malware by wrapping it as a test method then build it to a .exe or .dll file to be later run by vstest.console.exe. This may both allow AWL bypass or defense bypass in general

```cmd
vstest.console.exe {PATH:.dll}
```

- Use Case: Proxy Execution and AWL bypass, Adversaries may run malicious code embedded inside the test methods of crafted dll/exe
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1127-trusted_developer_utilities_proxy_execution|T1127: Trusted Developer Utilities Proxy Execution]]

## Detections

- IOC: vstest.console.exe spawning unexpected processes

## Resources

- {'Link': 'https://learn.microsoft.com/en-us/visualstudio/test/vstest-console-options?view=vs-2022'}

## Acknowledgements

- {'Person': 'Onat Uzunyayla'}
- {'Person': 'Ayberk Halac'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/vstest.console.yml)
