---
title: "Pktmon.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Pktmon.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Pktmon.yml"
build_date: "2026-04-27 19:14:21"
category: "OSBinaries"
aliases:
  - "Pktmon.exe"
functions:
  - "Reconnaissance"
attack_technique_ids:
  - "T1040"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Capture Network Packets on the windows 10 with October 2018 Update or later.

## Paths

- `c:\windows\system32\pktmon.exe`
- `c:\windows\syswow64\pktmon.exe`

## Commands

### 1. Reconnaissance

Will start a packet capture and store log file as PktMon.etl. Use pktmon.exe stop

```cmd
pktmon.exe start --etw
```

- Use Case: use this a built in network sniffer on windows 10 to capture senstive traffic
- Privileges: Administrator
- Operating System: Windows 10 1809 and later, Windows 11
- ATT&CK: [[kb/attack/techniques/T1040-network_sniffing|T1040: Network Sniffing]]

### 2. Reconnaissance

Select Desired ports for packet capture

```cmd
pktmon.exe filter add -p 445
```

- Use Case: Look for interesting traffic such as telent or FTP
- Privileges: Administrator
- Operating System: Windows 10 1809 and later, Windows 11
- ATT&CK: [[kb/attack/techniques/T1040-network_sniffing|T1040: Network Sniffing]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_lolbin_pktmon.yml
- IOC: .etl files found on system

## Resources

- {'Link': 'https://binar-x79.com/windows-10-secret-sniffer/'}

## Acknowledgements

- {'Person': 'Derek Johnson'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Pktmon.yml)
