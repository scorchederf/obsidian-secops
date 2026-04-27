---
title: "Wlrmdr.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Wlrmdr.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Wlrmdr.yml"
build_date: "2026-04-27 18:39:01"
category: "OSBinaries"
aliases:
  - "Wlrmdr.exe"
functions:
  - "Execute"
attack_technique_ids:
  - "T1202"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Wlrmdr.exe

Windows Logon Reminder executable

## Metadata

- Category: OSBinaries
- Created: 2022-02-16
- Author: Moshe Kaplan
- Source Path: yml/OSBinaries/Wlrmdr.yml

## Paths

- `c:\windows\system32\wlrmdr.exe`

## Commands

### 1. Execute

Execute executable with wlrmdr.exe as parent process

```cmd
wlrmdr.exe -s 3600 -f 0 -t _ -m _ -a 11 -u {PATH:.exe}
```

- Use Case: Use wlrmdr as a proxy binary to evade defensive countermeasures
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1202-indirect_command_execution|T1202]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_lolbin_wlrmdr.yml
- IOC: wlrmdr.exe spawning any new processes

## Resources

- {'Link': 'https://twitter.com/0gtweet/status/1493963591745220608'}
- {'Link': 'https://twitter.com/Oddvarmoe/status/927437787242090496'}
- {'Link': 'https://twitter.com/falsneg/status/1461625526640992260'}
- {'Link': 'https://docs.microsoft.com/en-us/windows/win32/api/shellapi/ns-shellapi-notifyicondataw'}

## Acknowledgements

- {'Person': 'Grzegorz Tworek', 'Handle': '@0gtweet'}
- {'Person': 'Oddvar Moe', 'Handle': '@Oddvarmoe'}
- {'Person': 'Freddy', 'Handle': '@falsneg'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Wlrmdr.yml)
