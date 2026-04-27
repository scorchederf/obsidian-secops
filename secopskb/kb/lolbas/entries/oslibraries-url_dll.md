---
title: "Url.dll"
framework: "lolbas"
generated: "true"
source_path: "yml/OSLibraries/Url.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSLibraries/Url.yml"
build_date: "2026-04-27 18:39:01"
category: "OSLibraries"
aliases:
  - "Url.dll"
functions:
  - "Execute"
attack_technique_ids:
  - "T1218.011"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Url.dll

Internet Shortcut Shell Extension DLL.

## Metadata

- Category: OSLibraries
- Created: 2018-05-25
- Author: LOLBAS Team
- Source Path: yml/OSLibraries/Url.yml

## Paths

- `c:\windows\system32\url.dll`
- `c:\windows\syswow64\url.dll`

## Commands

### 1. Execute

Launch a HTML application payload by calling OpenURL.

```cmd
rundll32.exe url.dll,OpenURL {PATH_ABSOLUTE:.hta}
```

- Use Case: Invoke an HTML Application via mshta.exe (Default Handler).
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.011]]

### 2. Execute

Launch an executable payload via proxy through a .url (information) file by calling OpenURL.

```cmd
rundll32.exe url.dll,OpenURL {PATH_ABSOLUTE:.url}
```

- Use Case: Load an executable payload by calling a .url file.
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.011]]

### 3. Execute

Launch an executable by calling OpenURL.

```cmd
rundll32.exe url.dll,OpenURL file://^C^:^/^W^i^n^d^o^w^s^/^s^y^s^t^e^m^3^2^/^c^a^l^c^.^e^x^e
```

- Use Case: Load an executable payload by specifying the file protocol handler (obfuscated).
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.011]]

### 4. Execute

Launch an executable by calling FileProtocolHandler.

```cmd
rundll32.exe url.dll,FileProtocolHandler {PATH_ABSOLUTE:.exe}
```

- Use Case: Launch an executable.
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.011]]

### 5. Execute

Launch an executable by calling FileProtocolHandler.

```cmd
rundll32.exe url.dll,FileProtocolHandler file://^C^:^/^W^i^n^d^o^w^s^/^s^y^s^t^e^m^3^2^/^c^a^l^c^.^e^x^e
```

- Use Case: Load an executable payload by specifying the file protocol handler (obfuscated).
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.011]]

### 6. Execute

Launch a HTML application payload by calling FileProtocolHandler.

```cmd
rundll32.exe url.dll,FileProtocolHandler file:///C:/test/test.hta
```

- Use Case: Invoke an HTML Application via mshta.exe (Default Handler).
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.011]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_rundll32_susp_activity.yml

## Resources

- {'Link': 'https://bohops.com/2018/03/17/abusing-exported-functions-and-exposed-dcom-interfaces-for-pass-thru-command-execution-and-lateral-movement/'}
- {'Link': 'https://twitter.com/DissectMalware/status/995348436353470465'}
- {'Link': 'https://twitter.com/bohops/status/974043815655956481'}
- {'Link': 'https://twitter.com/yeyint_mth/status/997355558070927360'}
- {'Link': 'https://twitter.com/Hexacorn/status/974063407321223168'}
- {'Link': 'https://windows10dll.nirsoft.net/url_dll.html'}

## Acknowledgements

- {'Person': 'Adam (OpenURL)', 'Handle': '@hexacorn'}
- {'Person': 'Jimmy (OpenURL)', 'Handle': '@bohops'}
- {'Person': 'Malwrologist (FileProtocolHandler - HTA)', 'Handle': '@DissectMalware'}
- {'Person': 'r0lan (Obfuscation)', 'Handle': '@r0lan'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSLibraries/Url.yml)
