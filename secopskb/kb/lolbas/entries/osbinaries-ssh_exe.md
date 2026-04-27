---
title: "ssh.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Ssh.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Ssh.yml"
build_date: "2026-04-27 19:14:21"
category: "OSBinaries"
aliases:
  - "ssh.exe"
functions:
  - "Execute"
attack_technique_ids:
  - "T1202"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Ssh.exe is the OpenSSH compatible client can be used to connect to Windows 10 (build 1809 and later) and Windows Server 2019 devices.

## Paths

- `c:\windows\system32\OpenSSH\ssh.exe`

## Commands

### 1. Execute

Executes specified command on host machine. The prompt for password can be eliminated by adding the host's public key in the user's authorized_keys file. Adversaries can do the same for execution on remote machines.

```cmd
ssh localhost "{CMD}"
```

- Use Case: Execute specified command, can be used for defense evasion.
- Privileges: User
- Operating System: Windows 10 1809, Windows Server 2019
- ATT&CK: [[kb/attack/techniques/T1202-indirect_command_execution|T1202: Indirect Command Execution]]

### 2. Execute

Executes specified command from ssh.exe

```cmd
ssh -o ProxyCommand="{CMD}" .
```

- Use Case: Performs execution of specified file, can be used as a defensive evasion.
- Privileges: User
- Operating System: Windows 10
- ATT&CK: [[kb/attack/techniques/T1202-indirect_command_execution|T1202: Indirect Command Execution]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_lolbin_ssh.yml
- IOC: Event ID 4624 with process name C:\Windows\System32\OpenSSH\sshd.exe.
- IOC: command line arguments specifying execution.

## Resources

- {'Link': 'https://gtfobins.github.io/gtfobins/ssh/'}

## Acknowledgements

- {'Person': 'Akshat Pradhan'}
- {'Person': 'Felix Boulet'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Ssh.yml)
