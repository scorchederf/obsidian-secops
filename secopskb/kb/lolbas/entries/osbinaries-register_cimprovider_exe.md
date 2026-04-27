---
title: "Register-cimprovider.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Register-cimprovider.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Register-cimprovider.yml"
build_date: "2026-04-27 18:39:01"
category: "OSBinaries"
aliases:
  - "Register-cimprovider.exe"
functions:
  - "Execute"
attack_technique_ids:
  - "T1218"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Register-cimprovider.exe

Used to register new wmi providers

## Metadata

- Category: OSBinaries
- Created: 2018-05-25
- Author: Oddvar Moe
- Source Path: yml/OSBinaries/Register-cimprovider.yml

## Paths

- `C:\Windows\System32\Register-cimprovider.exe`
- `C:\Windows\SysWOW64\Register-cimprovider.exe`

## Commands

### 1. Execute

Load the target .DLL.

```cmd
Register-cimprovider -path {PATH_ABSOLUTE:.dll}
```

- Use Case: Execute code within dll file
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/35a7244c62820fbc5a832e50b1e224ac3a1935da/rules/windows/process_creation/proc_creation_win_susp_register_cimprovider.yml
- IOC: Register-cimprovider.exe execution and cmdline DLL load may be supsicious

## Resources

- {'Link': 'https://twitter.com/PhilipTsukerman/status/992021361106268161'}

## Acknowledgements

- {'Person': 'Philip Tsukerman', 'Handle': '@PhilipTsukerman'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Register-cimprovider.yml)
