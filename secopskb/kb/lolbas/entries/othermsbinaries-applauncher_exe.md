---
title: "AppLauncher.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OtherMSBinaries/AppLauncher.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/AppLauncher.yml"
build_date: "2026-04-27 19:14:21"
category: "OtherMSBinaries"
aliases:
  - "AppLauncher.exe"
functions:
  - "Execute"
attack_technique_ids:
  - "T1127"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

User Experience Virtualization tool that launches applications under monitoring to capture and synchronize user settings.

## Paths

- `C:\Program Files\Windows Kits\10\Microsoft User Experience Virtualization\Management\AppLauncher.exe`
- `C:\Program Files (x86)\Windows Kits\10\Microsoft User Experience Virtualization\Management\AppLauncher.exe`

## Commands

### 1. Execute

Launches an executable via User Experience Virtualization tool.

```cmd
AppLauncher.exe {PATH_ABSOLUTE:.exe}
```

- Use Case: Executes an executable under a trusted, Microsoft signed binary.
- Privileges: User
- Operating System: Windows
- ATT&CK: [[kb/attack/techniques/T1127-trusted_developer_utilities_proxy_execution|T1127: Trusted Developer Utilities Proxy Execution]]

## Resources

- {'Link': 'https://learn.microsoft.com/en-us/microsoft-desktop-optimization-pack/ue-v/uev-getting-started'}

## Acknowledgements

- {'Person': 'Avihay Eldad', 'Handle': '@AvihayEldad'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/AppLauncher.yml)
