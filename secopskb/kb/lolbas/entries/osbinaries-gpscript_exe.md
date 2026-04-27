---
title: "Gpscript.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Gpscript.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Gpscript.yml"
build_date: "2026-04-27 18:39:01"
category: "OSBinaries"
aliases:
  - "Gpscript.exe"
functions:
  - "Execute"
attack_technique_ids:
  - "T1218"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Gpscript.exe

Used by group policy to process scripts

## Metadata

- Category: OSBinaries
- Created: 2018-05-25
- Author: Oddvar Moe
- Source Path: yml/OSBinaries/Gpscript.yml

## Paths

- `C:\Windows\System32\gpscript.exe`
- `C:\Windows\SysWOW64\gpscript.exe`

## Commands

### 1. Execute

Executes logon scripts configured in Group Policy.

```cmd
Gpscript /logon
```

- Use Case: Add local group policy logon script to execute file and hide from defensive counter measures
- Privileges: Administrator
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

### 2. Execute

Executes startup scripts configured in Group Policy

```cmd
Gpscript /startup
```

- Use Case: Add local group policy logon script to execute file and hide from defensive counter measures
- Privileges: Administrator
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_lolbin_gpscript.yml
- IOC: Scripts added in local group policy
- IOC: Execution of Gpscript.exe after logon

## Resources

- {'Link': 'https://oddvar.moe/2018/04/27/gpscript-exe-another-lolbin-to-the-list/'}

## Acknowledgements

- {'Person': 'Oddvar Moe', 'Handle': '@oddvarmoe'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Gpscript.yml)
