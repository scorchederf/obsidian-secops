---
title: "cmdl32.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Cmdl32.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Cmdl32.yml"
build_date: "2026-04-27 18:39:01"
category: "OSBinaries"
aliases:
  - "cmdl32.exe"
functions:
  - "Download"
attack_technique_ids:
  - "T1105"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# cmdl32.exe

Microsoft Connection Manager Auto-Download

## Metadata

- Category: OSBinaries
- Created: 2021-08-26
- Author: Elliot Killick
- Source Path: yml/OSBinaries/Cmdl32.yml

## Paths

- `C:\Windows\System32\cmdl32.exe`
- `C:\Windows\SysWOW64\cmdl32.exe`

## Commands

### 1. Download

Download a file from the web address specified in the configuration file. The downloaded file will be in %TMP% under the name VPNXXXX.tmp where "X" denotes a random number or letter.

```cmd
cmdl32 /vpn /lan %cd%\config
```

- Use Case: Download file from Internet
- Privileges: User
- Operating System: Windows Vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_lolbin_cmdl32.yml
- IOC: Reports of downloading from suspicious URLs in %TMP%\config.log
- IOC: Useragent Microsoft(R) Connection Manager Vpn File Update

## Resources

- {'Link': 'https://github.com/LOLBAS-Project/LOLBAS/pull/151'}
- {'Link': 'https://twitter.com/ElliotKillick/status/1455897435063074824'}
- {'Link': 'https://elliotonsecurity.com/living-off-the-land-reverse-engineering-methodology-plus-tips-and-tricks-cmdl32-case-study/'}

## Acknowledgements

- {'Person': 'Elliot Killick', 'Handle': '@elliotkillick'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Cmdl32.yml)
