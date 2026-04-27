---
title: "Advpack.dll"
framework: "lolbas"
generated: "true"
source_path: "yml/OSLibraries/Advpack.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSLibraries/Advpack.yml"
build_date: "2026-04-27 18:39:01"
category: "OSLibraries"
aliases:
  - "Advpack.dll"
functions:
  - "AWL Bypass"
  - "Execute"
attack_technique_ids:
  - "T1218.011"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Advpack.dll

Utility for installing software and drivers with rundll32.exe

## Metadata

- Category: OSLibraries
- Created: 2018-05-25
- Author: LOLBAS Team
- Source Path: yml/OSLibraries/Advpack.yml

## Paths

- `c:\windows\system32\advpack.dll`
- `c:\windows\syswow64\advpack.dll`

## Commands

### 1. AWL Bypass

Execute the specified (local or remote) .wsh/.sct script with scrobj.dll in the .inf file by calling an information file directive (section name specified).

```cmd
rundll32.exe advpack.dll,LaunchINFSection {PATH:.inf},DefaultInstall_SingleUser,1,
```

- Use Case: Run local or remote script(let) code through INF file specification.
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.011]]

### 2. AWL Bypass

Execute the specified (local or remote) .wsh/.sct script with scrobj.dll in the .inf file by calling an information file directive (DefaultInstall section implied).

```cmd
rundll32.exe advpack.dll,LaunchINFSection {PATH:.inf},,1,
```

- Use Case: Run local or remote script(let) code through INF file specification.
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.011]]

### 3. Execute

Launch a DLL payload by calling the RegisterOCX function.

```cmd
rundll32.exe advpack.dll,RegisterOCX {PATH:.dll}
```

- Use Case: Load a DLL payload.
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.011]]

### 4. Execute

Launch an executable by calling the RegisterOCX function.

```cmd
rundll32.exe advpack.dll,RegisterOCX {PATH:.exe}
```

- Use Case: Run an executable payload.
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.011]]

### 5. Execute

Launch command line by calling the RegisterOCX function.

```cmd
rundll32 advpack.dll, RegisterOCX {CMD}
```

- Use Case: Run an executable payload.
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.011]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_rundll32_susp_activity.yml
- Splunk: https://github.com/splunk/security_content/blob/86a5b644a44240f01274c8b74d19a435c7dae66e/detections/endpoint/detect_rundll32_application_control_bypass___advpack.yml

## Resources

- {'Link': 'https://bohops.com/2018/02/26/leveraging-inf-sct-fetch-execute-techniques-for-bypass-evasion-persistence/'}
- {'Link': 'https://twitter.com/ItsReallyNick/status/967859147977850880'}
- {'Link': 'https://twitter.com/bohops/status/974497123101179904'}
- {'Link': 'https://twitter.com/moriarty_meng/status/977848311603380224'}

## Acknowledgements

- {'Person': 'Jimmy (LaunchINFSection)', 'Handle': '@bohops'}
- {'Person': 'Fabrizio (RegisterOCX - DLL)', 'Handle': '@0rbz_'}
- {'Person': 'Moriarty (RegisterOCX - CMD)', 'Handle': '@moriarty_meng'}
- {'Person': 'Nick Carr (Threat Intel)', 'Handle': '@ItsReallyNick'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSLibraries/Advpack.yml)
