---
title: "Aspnet_Compiler.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Aspnet_Compiler.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Aspnet_Compiler.yml"
build_date: "2026-04-27 18:39:01"
category: "OSBinaries"
aliases:
  - "Aspnet_Compiler.exe"
functions:
  - "AWL Bypass"
attack_technique_ids:
  - "T1127"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Aspnet_Compiler.exe

ASP.NET Compilation Tool

## Metadata

- Category: OSBinaries
- Created: 2021-09-26
- Author: Jimmy (@bohops)
- Source Path: yml/OSBinaries/Aspnet_Compiler.yml

## Paths

- `c:\Windows\Microsoft.NET\Framework\v4.0.30319\aspnet_compiler.exe`
- `c:\Windows\Microsoft.NET\Framework64\v4.0.30319\aspnet_compiler.exe`

## Commands

### 1. AWL Bypass

Execute C# code with the Build Provider and proper folder structure in place.

```cmd
C:\Windows\Microsoft.NET\Framework64\v4.0.30319\aspnet_compiler.exe -v none -p C:\users\cpl.internal\desktop\asptest\ -f C:\users\cpl.internal\desktop\asptest\none -u
```

- Use Case: Execute proxied payload with Microsoft signed binary to bypass application control solutions
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1127-trusted_developer_utilities_proxy_execution|T1127]]

## Detections

- BlockRule: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_lolbin_aspnet_compiler.yml

## Resources

- {'Link': 'https://ijustwannared.team/2020/08/01/the-curious-case-of-aspnet_compiler-exe/'}
- {'Link': 'https://docs.microsoft.com/en-us/dotnet/api/system.web.compilation.buildprovider.generatecode?view=netframework-4.8'}

## Acknowledgements

- {'Person': 'cpl', 'Handle': '@cpl3h'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Aspnet_Compiler.yml)
