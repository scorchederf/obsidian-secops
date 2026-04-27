---
title: "Makecab.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Makecab.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Makecab.yml"
build_date: "2026-04-27 18:39:01"
category: "OSBinaries"
aliases:
  - "Makecab.exe"
functions:
  - "ADS"
  - "Download"
  - "Execute"
attack_technique_ids:
  - "T1564.004"
  - "T1105"
  - "T1036"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Makecab.exe

Binary to package existing files into a cabinet (.cab) file

## Metadata

- Category: OSBinaries
- Created: 2018-05-25
- Author: Oddvar Moe
- Source Path: yml/OSBinaries/Makecab.yml

## Paths

- `C:\Windows\System32\makecab.exe`
- `C:\Windows\SysWOW64\makecab.exe`

## Commands

### 1. ADS

Compresses the target file into a CAB file stored in the Alternate Data Stream (ADS) of the target file.

```cmd
makecab {PATH_ABSOLUTE:.exe} {PATH_ABSOLUTE}:autoruns.cab
```

- Use Case: Hide data compressed into an alternate data stream
- Privileges: User
- Operating System: Windows XP, Windows Vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1564-hide_artifacts|T1564.004]]

### 2. ADS

Compresses the target file into a CAB file stored in the Alternate Data Stream (ADS) of the target file.

```cmd
makecab {PATH_SMB:.exe} {PATH_ABSOLUTE}:file.cab
```

- Use Case: Hide data compressed into an alternate data stream
- Privileges: User
- Operating System: Windows XP, Windows Vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1564-hide_artifacts|T1564.004]]

### 3. Download

Download and compresses the target file and stores it in the target file.

```cmd
makecab {PATH_SMB:.exe} {PATH_ABSOLUTE:.cab}
```

- Use Case: Download file and compress into a cab file
- Privileges: User
- Operating System: Windows XP, Windows Vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

### 4. Execute

Execute makecab commands as defined in the specified Diamond Definition File (.ddf); see resources for the format specification.

```cmd
makecab /F {PATH:.ddf}
```

- Use Case: Bypass command-line based detections
- Privileges: User
- Operating System: Windows XP, Windows Vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1036-masquerading|T1036]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_susp_alternate_data_streams.yml
- Elastic: https://github.com/elastic/detection-rules/blob/12577f7380f324fcee06dab3218582f4a11833e7/rules/windows/defense_evasion_misc_lolbin_connecting_to_the_internet.toml
- IOC: Makecab retrieving files from Internet
- IOC: Makecab storing data into alternate data streams

## Resources

- {'Link': 'https://gist.github.com/api0cradle/cdd2d0d0ec9abb686f0e89306e277b8f'}
- {'Link': 'https://ss64.com/nt/makecab-directives.html'}
- {'Link': 'https://www.pearsonhighered.com/assets/samplechapter/0/7/8/9/0789728583.pdf'}
- {'Link': 'https://learn.microsoft.com/en-us/previous-versions/bb417343(v=msdn.10)#makecab-application'}

## Acknowledgements

- {'Person': 'Oddvar Moe', 'Handle': '@oddvarmoe'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Makecab.yml)
