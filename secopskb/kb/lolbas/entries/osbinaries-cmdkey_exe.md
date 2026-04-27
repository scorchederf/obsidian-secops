---
title: "Cmdkey.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Cmdkey.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Cmdkey.yml"
build_date: "2026-04-27 18:39:01"
category: "OSBinaries"
aliases:
  - "Cmdkey.exe"
functions:
  - "Credentials"
attack_technique_ids:
  - "T1078"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Cmdkey.exe

creates, lists, and deletes stored user names and passwords or credentials.

## Metadata

- Category: OSBinaries
- Created: 2018-05-25
- Author: Oddvar Moe
- Source Path: yml/OSBinaries/Cmdkey.yml

## Paths

- `C:\Windows\System32\cmdkey.exe`
- `C:\Windows\SysWOW64\cmdkey.exe`

## Commands

### 1. Credentials

List cached credentials

```cmd
cmdkey /list
```

- Use Case: Get credential information from host
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1078-valid_accounts|T1078]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_cmdkey_recon.yml

## Resources

- {'Link': 'https://web.archive.org/web/20230202122017/https://www.peew.pw/blog/2017/11/26/exploring-cmdkey-an-edge-case-for-privilege-escalation'}
- {'Link': 'https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/cmdkey'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Cmdkey.yml)
