---
title: "Sftp.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Sftp.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Sftp.yml"
build_date: "2026-04-27 18:39:01"
category: "OSBinaries"
aliases:
  - "Sftp.exe"
functions:
  - "Execute"
attack_technique_ids:
  - "T1202"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Sftp.exe

sftp.exe is a Windows command-line utility that uses the Secure File Transfer Protocol (SFTP) to securely transfer files between a local machine and a remote server.

## Metadata

- Category: OSBinaries
- Created: 2025-05-13
- Author: Swachchhanda Shrawan Poudel
- Source Path: yml/OSBinaries/Sftp.yml

## Paths

- `C:\Windows\System32\OpenSSH\sftp.exe`

## Commands

### 1. Execute

Spawns ssh.exe which in turn spawns the specified command line. See also this project's entry for ssh.exe.

```cmd
sftp -o ProxyCommand="{CMD}" .
```

- Use Case: Proxy execution of specified command, can be used as a defensive evasion.
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1202-indirect_command_execution|T1202]]

## Detections

- IOC: sftp.exe executions with ProxyCommand on the command line
- IOC: sftp.exe spawning ssh.exe with ProxyCommand on the command line
- Sigma: https://github.com/SigmaHQ/sigma/pull/5414/files

## Resources

- {'Link': 'https://news.sophos.com/en-us/2025/05/09/lumma-stealer-coming-and-going/'}

## Acknowledgements

- {'Person': 'Swachchhanda Shrawan Poudel', 'Handle': '@_swachchhanda_'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Sftp.yml)
