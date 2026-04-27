---
title: "Extrac32.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Extrac32.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Extrac32.yml"
build_date: "2026-04-27 19:14:21"
category: "OSBinaries"
aliases:
  - "Extrac32.exe"
functions:
  - "ADS"
  - "Download"
  - "Copy"
attack_technique_ids:
  - "T1564.004"
  - "T1105"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Extract to ADS, copy or overwrite a file with Extrac32.exe

## Paths

- `C:\Windows\System32\extrac32.exe`
- `C:\Windows\SysWOW64\extrac32.exe`

## Commands

### 1. ADS

Extracts the source CAB file into an Alternate Data Stream (ADS) of the target file.

```cmd
extrac32 {PATH_ABSOLUTE:.cab} {PATH_ABSOLUTE}:file.exe
```

- Use Case: Extract data from cab file and hide it in an alternate data stream.
- Privileges: User
- Operating System: Windows XP, Windows Vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1564-hide_artifacts#^t1564004-ntfs-file-attributes|T1564.004: NTFS File Attributes]]

### 2. ADS

Extracts the source CAB file on an unc path into an Alternate Data Stream (ADS) of the target file.

```cmd
extrac32 {PATH_ABSOLUTE:.cab} {PATH_ABSOLUTE}:file.exe
```

- Use Case: Extract data from cab file and hide it in an alternate data stream.
- Privileges: User
- Operating System: Windows XP, Windows Vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1564-hide_artifacts#^t1564004-ntfs-file-attributes|T1564.004: NTFS File Attributes]]

### 3. Download

Copy the source file to the destination file and overwrite it.

```cmd
extrac32 /Y /C {PATH_SMB} {PATH_ABSOLUTE}
```

- Use Case: Download file from UNC/WEBDav
- Privileges: User
- Operating System: Windows XP, Windows Vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]]

### 4. Copy

Command for copying file from one folder to another

```cmd
extrac32.exe /C {PATH_ABSOLUTE:.source.exe} {PATH_ABSOLUTE:.dest.exe}
```

- Use Case: Copy file
- Privileges: User
- Operating System: Windows XP, Windows Vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]]

## Detections

- Elastic: https://github.com/elastic/detection-rules/blob/12577f7380f324fcee06dab3218582f4a11833e7/rules/windows/defense_evasion_misc_lolbin_connecting_to_the_internet.toml
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_lolbin_extrac32.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/c04bef2fbbe8beff6c7620d5d7ea6872dbe7acba/rules/windows/process_creation/proc_creation_win_lolbin_extrac32_ads.yml

## Resources

- {'Link': 'https://oddvar.moe/2018/04/11/putting-data-in-alternate-data-streams-and-how-to-execute-it-part-2/'}
- {'Link': 'https://gist.github.com/api0cradle/cdd2d0d0ec9abb686f0e89306e277b8f'}
- {'Link': 'https://twitter.com/egre55/status/985994639202283520'}

## Acknowledgements

- {'Person': 'egre55', 'Handle': '@egre55'}
- {'Person': 'Oddvar Moe', 'Handle': '@oddvarmoe'}
- {'Person': 'Hai Vaknin(Lux', 'Handle': '@VakninHai'}
- {'Person': 'Tamir Yehuda', 'Handle': '@tim8288'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Extrac32.yml)
