---
title: "coregen.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OtherMSBinaries/Coregen.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Coregen.yml"
build_date: "2026-04-27 19:14:21"
category: "OtherMSBinaries"
aliases:
  - "coregen.exe"
functions:
  - "Execute"
  - "AWL Bypass"
attack_technique_ids:
  - "T1055"
  - "T1218"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Binary coregen.exe (Microsoft CoreCLR Native Image Generator) loads exported function GetCLRRuntimeHost from coreclr.dll or from .DLL in arbitrary path. Coregen is located within "C:\Program Files (x86)\Microsoft Silverlight\5.1.50918.0\" or another version of Silverlight. Coregen is signed by Microsoft and bundled with Microsoft Silverlight.

## Paths

- `C:\Program Files\Microsoft Silverlight\5.1.50918.0\coregen.exe`
- `C:\Program Files (x86)\Microsoft Silverlight\5.1.50918.0\coregen.exe`

## Commands

### 1. Execute

Loads the target .DLL in arbitrary path specified with /L.

```cmd
coregen.exe /L {PATH_ABSOLUTE:.dll} dummy_assembly_name
```

- Use Case: Execute DLL code
- Privileges: User
- Operating System: Windows
- ATT&CK: [[kb/attack/techniques/T1055-process_injection|T1055: Process Injection]]

### 2. Execute

Loads the coreclr.dll in the corgen.exe directory (e.g. C:\Program Files\Microsoft Silverlight\5.1.50918.0).

```cmd
coregen.exe dummy_assembly_name
```

- Use Case: Execute DLL code
- Privileges: User
- Operating System: Windows
- ATT&CK: [[kb/attack/techniques/T1055-process_injection|T1055: Process Injection]]

### 3. AWL Bypass

Loads the target .DLL in arbitrary path specified with /L. Since binary is signed it can also be used to bypass application whitelisting solutions.

```cmd
coregen.exe /L {PATH_ABSOLUTE:.dll} dummy_assembly_name
```

- Use Case: Execute DLL code
- Privileges: User
- Operating System: Windows
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/b02e3b698afbaae143ac4fb36236eb0b41122ed7/rules/windows/image_load/image_load_side_load_coregen.yml
- IOC: coregen.exe loading .dll file not in "C:\Program Files (x86)\Microsoft Silverlight\5.1.50918.0\"
- IOC: coregen.exe loading .dll file not named coreclr.dll
- IOC: coregen.exe command line containing -L or -l
- IOC: coregen.exe command line containing unexpected/invald assembly name
- IOC: coregen.exe application crash by invalid assembly name

## Resources

- {'Link': 'https://www.youtube.com/watch?v=75XImxOOInU'}
- {'Link': 'https://www.fireeye.com/blog/threat-research/2019/10/staying-hidden-on-the-endpoint-evading-detection-with-shellcode.html'}

## Acknowledgements

- {'Person': 'Nicky Tyrer'}
- {'Person': 'Evan Pena'}
- {'Person': 'Casey Erikson'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Coregen.yml)
