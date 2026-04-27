---
title: "Shell32.dll"
framework: "lolbas"
generated: "true"
source_path: "yml/OSLibraries/Shell32.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSLibraries/Shell32.yml"
build_date: "2026-04-27 18:39:01"
category: "OSLibraries"
aliases:
  - "Shell32.dll"
functions:
  - "Execute"
attack_technique_ids:
  - "T1218.011"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Shell32.dll

Windows Shell Common Dll

## Metadata

- Category: OSLibraries
- Created: 2018-05-25
- Author: LOLBAS Team
- Source Path: yml/OSLibraries/Shell32.yml

## Paths

- `c:\windows\system32\shell32.dll`
- `c:\windows\syswow64\shell32.dll`

## Commands

### 1. Execute

Launch a DLL payload by calling the Control_RunDLL function.

```cmd
rundll32.exe shell32.dll,Control_RunDLL {PATH_ABSOLUTE:.dll}
```

- Use Case: Load a DLL payload.
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.011]]

### 2. Execute

Launch an executable by calling the ShellExec_RunDLL function.

```cmd
rundll32.exe shell32.dll,ShellExec_RunDLL {PATH:.exe}
```

- Use Case: Run an executable payload.
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.011]]

### 3. Execute

Launch command line by calling the ShellExec_RunDLL function.

```cmd
rundll32 SHELL32.DLL,ShellExec_RunDLL {PATH:.exe} {CMD:args}
```

- Use Case: Run an executable payload.
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.011]]

### 4. Execute

Load a DLL/CPL by calling undocumented Control_RunDLLNoFallback function.

```cmd
rundll32.exe shell32.dll,#44 {PATH:.dll}
```

- Use Case: Load a DLL/CPL payload.
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.011]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_rundll32_susp_activity.yml
- Splunk: https://github.com/splunk/security_content/blob/a1afa0fa605639cbef7d528dec46ce7c8112194a/detections/endpoint/rundll32_control_rundll_hunt.yml

## Resources

- {'Link': 'https://twitter.com/Hexacorn/status/885258886428725250'}
- {'Link': 'https://twitter.com/pabraeken/status/991768766898941953'}
- {'Link': 'https://twitter.com/mattifestation/status/776574940128485376'}
- {'Link': 'https://twitter.com/KyleHanslovan/status/905189665120149506'}
- {'Link': 'https://windows10dll.nirsoft.net/shell32_dll.html'}
- {'Link': 'https://www.hexacorn.com/blog/2025/05/18/shell32-dll-44-lolbin/'}

## Acknowledgements

- {'Person': 'Adam (Control_RunDLL, Control_RunDLLNoFallback)', 'Handle': '@hexacorn'}
- {'Person': 'Pierre-Alexandre Braeken (ShellExec_RunDLL)', 'Handle': '@pabraeken'}
- {'Person': 'Matt Graeber (ShellExec_RunDLL)', 'Handle': '@mattifestation'}
- {'Person': 'Kyle Hanslovan (ShellExec_RunDLL)', 'Handle': '@KyleHanslovan'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSLibraries/Shell32.yml)
