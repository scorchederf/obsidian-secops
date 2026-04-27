---
title: "Syssetup.dll"
framework: "lolbas"
generated: "true"
source_path: "yml/OSLibraries/Syssetup.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSLibraries/Syssetup.yml"
build_date: "2026-04-27 18:39:01"
category: "OSLibraries"
aliases:
  - "Syssetup.dll"
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

# Syssetup.dll

Windows NT System Setup

## Metadata

- Category: OSLibraries
- Created: 2018-05-25
- Author: LOLBAS Team
- Source Path: yml/OSLibraries/Syssetup.yml

## Paths

- `c:\windows\system32\syssetup.dll`
- `c:\windows\syswow64\syssetup.dll`

## Commands

### 1. AWL Bypass

Execute the specified (local or remote) .wsh/.sct script with scrobj.dll in the .inf file by calling an information file directive (section name specified).

```cmd
rundll32 syssetup.dll,SetupInfObjectInstallAction DefaultInstall 128 {PATH_ABSOLUTE:.inf}
```

- Use Case: Run local or remote script(let) code through INF file specification (Note May pop an error window).
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.011]]

### 2. Execute

Launch an executable file via the SetupInfObjectInstallAction function and .inf file section directive.

```cmd
rundll32 syssetup.dll,SetupInfObjectInstallAction DefaultInstall 128 {PATH_ABSOLUTE:.inf}
```

- Use Case: Load an executable payload.
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.011]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_rundll32_susp_activity.yml
- Splunk: https://github.com/splunk/security_content/blob/86a5b644a44240f01274c8b74d19a435c7dae66e/detections/endpoint/detect_rundll32_application_control_bypass___syssetup.yml

## Resources

- {'Link': 'https://twitter.com/pabraeken/status/994392481927258113'}
- {'Link': 'https://twitter.com/harr0ey/status/975350238184697857'}
- {'Link': 'https://twitter.com/bohops/status/975549525938135040'}
- {'Link': 'https://windows10dll.nirsoft.net/syssetup_dll.html'}

## Acknowledgements

- {'Person': 'Pierre-Alexandre Braeken (Execute)', 'Handle': '@pabraeken'}
- {'Person': 'Matt harr0ey (Execute)', 'Handle': '@harr0ey'}
- {'Person': 'Jimmy (Scriptlet)', 'Handle': '@bohops'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSLibraries/Syssetup.yml)
