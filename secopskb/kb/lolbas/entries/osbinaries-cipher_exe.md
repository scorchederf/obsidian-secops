---
title: "Cipher.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Cipher.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Cipher.yml"
build_date: "2026-04-27 18:39:01"
category: "OSBinaries"
aliases:
  - "Cipher.exe"
functions:
  - "Tamper"
attack_technique_ids:
  - "T1485"
  - "T1562"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Cipher.exe

File Encryption Utility

## Metadata

- Category: OSBinaries
- Created: 2024-11-22
- Author: Adetutu Ogunsowo
- Source Path: yml/OSBinaries/Cipher.yml

## Paths

- `c:\windows\system32\cipher.exe`
- `c:\windows\syswow64\cipher.exe`

## Commands

### 1. Tamper

Zero out a file

```cmd
cipher /w:{PATH_ABSOLUTE:folder}
```

- Use Case: Can be used to forensically erase a file.
- Privileges: User
- Operating System: Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1485-data_destruction|T1485]]

### 2. Tamper

Encrypt a file

```cmd
cipher.exe /e {PATH_ABSOLUTE}
```

- Use Case: Can be used to impair defences by e.g. encrypting a critical EDR solution file.
- Privileges: Admin
- Operating System: Windows 10
- ATT&CK: [[kb/attack/techniques/T1562-impair_defenses|T1562]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/c7998c92b3c5f23ea67045bee8ee364d2ed1a775/rules/windows/process_creation/proc_creation_win_cipher_overwrite_deleted_data.yml
- IOC: cipher.exe process with /w on the command line

## Resources

- {'Link': 'https://www.volexity.com/blog/2024/11/22/the-nearest-neighbor-attack-how-a-russian-apt-weaponized-nearby-wi-fi-networks-for-covert-access/'}

## Acknowledgements

- {'Person': 'Ade Ogunsowo', 'Handle': '@i_am_tutu'}
- {'Person': 'Alexander Sennhauser', 'Handle': '@conitrade'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Cipher.yml)
