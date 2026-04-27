---
title: "vbc.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Vbc.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Vbc.yml"
build_date: "2026-04-27 19:14:21"
category: "OSBinaries"
aliases:
  - "vbc.exe"
functions:
  - "Compile"
attack_technique_ids:
  - "T1127"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Binary file used for compile vbs code

## Paths

- `C:\Windows\Microsoft.NET\Framework\v4.0.30319\vbc.exe`
- `C:\Windows\Microsoft.NET\Framework\v3.5\vbc.exe`
- `C:\Windows\Microsoft.NET\Framework\v2.0.50727\vbc.exe`
- `C:\Windows\Microsoft.NET\Framework64\v4.0.30319\vbc.exe`
- `C:\Windows\Microsoft.NET\Framework64\v3.5\vbc.exe`
- `C:\Windows\Microsoft.NET\Framework64\v2.0.50727\vbc.exe`

## Commands

### 1. Compile

Binary file used by .NET to compile Visual Basic code to an executable.

```cmd
vbc.exe /target:exe {PATH_ABSOLUTE:.vb}
```

- Use Case: Compile attacker code on system. Bypass defensive counter measures.
- Privileges: User
- Operating System: Windows 7, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1127-trusted_developer_utilities_proxy_execution|T1127: Trusted Developer Utilities Proxy Execution]]

### 2. Compile

Binary file used by .NET to compile Visual Basic code to an executable.

```cmd
vbc -reference:Microsoft.VisualBasic.dll {PATH_ABSOLUTE:.vb}
```

- Use Case: Compile attacker code on system. Bypass defensive counter measures.
- Privileges: User
- Operating System: Windows 7, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1127-trusted_developer_utilities_proxy_execution|T1127: Trusted Developer Utilities Proxy Execution]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_visual_basic_compiler.yml
- Elastic: https://github.com/elastic/detection-rules/blob/61afb1c1c0c3f50637b1bb194f3e6fb09f476e50/rules/windows/defense_evasion_dotnet_compiler_parent_process.toml

## Acknowledgements

- {'Person': 'Lior Adar'}
- {'Person': 'Hai Vaknin(Lux)'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Vbc.yml)
