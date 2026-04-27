---
title: "Csc.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Csc.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Csc.yml"
build_date: "2026-04-27 19:14:21"
category: "OSBinaries"
aliases:
  - "Csc.exe"
functions:
  - "Compile"
attack_technique_ids:
  - "T1127"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Binary file used by .NET Framework to compile C# code

## Paths

- `C:\Windows\Microsoft.NET\Framework\v4.0.30319\Csc.exe`
- `C:\Windows\Microsoft.NET\Framework64\v4.0.30319\Csc.exe`
- `C:\Windows\Microsoft.NET\Framework\v3.5\csc.exe`
- `C:\Windows\Microsoft.NET\Framework64\v3.5\csc.exe`
- `C:\Windows\Microsoft.NET\Framework\v2.0.50727\csc.exe`
- `C:\Windows\Microsoft.NET\Framework64\v2.0.50727\csc.exe`

## Commands

### 1. Compile

Use csc.exe to compile C# code, targeting the .NET Framework, stored in the specified .cs file and output the compiled version to the specified .exe path.

```cmd
csc.exe -out:{PATH:.exe} {PATH:.cs}
```

- Use Case: Compile attacker code on system. Bypass defensive counter measures.
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1127-trusted_developer_utilities_proxy_execution|T1127: Trusted Developer Utilities Proxy Execution]]

### 2. Compile

Use csc.exe to compile C# code, targeting the .NET Framework, stored in the specified .cs file and output the compiled version to a DLL file with the same name.

```cmd
csc -target:library {PATH:.cs}
```

- Use Case: Compile attacker code on system. Bypass defensive counter measures.
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1127-trusted_developer_utilities_proxy_execution|T1127: Trusted Developer Utilities Proxy Execution]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_csc_susp_parent.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_csc_susp_folder.yml
- Elastic: https://github.com/elastic/detection-rules/blob/61afb1c1c0c3f50637b1bb194f3e6fb09f476e50/rules/windows/defense_evasion_dotnet_compiler_parent_process.toml
- Elastic: https://github.com/elastic/detection-rules/blob/82ec6ac1eeb62a1383792719a1943b551264ed16/rules/windows/defense_evasion_execution_msbuild_started_unusal_process.toml
- IOC: Csc.exe should normally not run as System account unless it is used for development.

## Resources

- {'Link': 'https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/compiler-options/'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Csc.yml)
