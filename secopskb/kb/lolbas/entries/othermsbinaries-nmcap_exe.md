---
title: "Nmcap.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OtherMSBinaries/Nmcap.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Nmcap.yml"
build_date: "2026-04-27 19:14:21"
category: "OtherMSBinaries"
aliases:
  - "Nmcap.exe"
functions:
  - "Reconnaissance"
attack_technique_ids:
  - "T1040"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Command-line packet capture utility from Microsoft Network Monitor 3.x.

## Paths

- `C:\Program Files\Microsoft Network Monitor 3\nmcap.exe`
- `C:\Program Files (x86)\Microsoft Network Monitor 3\nmcap.exe`

## Commands

### 1. Reconnaissance

Start capture on all network adapters and save to specified .cap (circular) file.
Optionally, one can add:
- `/TerminateWhen /TimeAfter 30 seconds` to auto-terminate after a relative times (e.g. 30 seconds);
- `/TerminateWhen /Time 04:52:00 AM 9/17/2025` to auto-terminate after a specific date/time;
- `/TerminateWhen /KeyPress x` to terminate when a specific key is pressed.

```cmd
nmcap.exe /network * /capture /file {PATH_ABSOLUTE:.cap}
```

- Use Case: Capture network traffic on windows to collect sensitive data.
- Privileges: Administrator
- Operating System: Windows
- ATT&CK: [[kb/attack/techniques/T1040-network_sniffing|T1040: Network Sniffing]]

## Resources

- {'Link': 'https://learn.microsoft.com/en-us/troubleshoot/windows-server/networking/network-monitor-3'}

## Acknowledgements

- {'Person': 'Avihay Eldad', 'Handle': '@AvihayEldad'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Nmcap.yml)
