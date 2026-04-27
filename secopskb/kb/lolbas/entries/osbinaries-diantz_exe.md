---
title: "Diantz.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Diantz.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Diantz.yml"
build_date: "2026-04-27 18:39:01"
category: "OSBinaries"
aliases:
  - "Diantz.exe"
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

# Diantz.exe

Binary that package existing files into a cabinet (.cab) file

## Metadata

- Category: OSBinaries
- Created: 2020-08-08
- Author: Tamir Yehuda
- Source Path: yml/OSBinaries/Diantz.yml

## Paths

- `c:\windows\system32\diantz.exe`
- `c:\windows\syswow64\diantz.exe`

## Commands

### 1. ADS

Compress a file (first argument) into a CAB file stored in the Alternate Data Stream (ADS) of the target file.

```cmd
diantz.exe {PATH_ABSOLUTE:.exe} {PATH_ABSOLUTE}:targetFile.cab
```

- Use Case: Hide data compressed into an Alternate Data Stream.
- Privileges: User
- Operating System: Windows XP, Windows vista, Windows 7, Windows 8, Windows 8.1.
- ATT&CK: [[kb/attack/techniques/T1564-hide_artifacts|T1564.004]]

### 2. Download

Download and compress a remote file and store it in a CAB file on local machine.

```cmd
diantz.exe {PATH_SMB:.exe} {PATH_ABSOLUTE:.cab}
```

- Use Case: Download and compress into a cab file.
- Privileges: User
- Operating System: Windows Server 2012, Windows Server 2012R2, Windows Server 2016, Windows Server 2019
- ATT&CK: [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

### 3. Execute

Execute diantz directives as defined in the specified Diamond Definition File (.ddf); see resources for the format specification.

```cmd
diantz /f {PATH:.ddf}
```

- Use Case: Bypass command-line based detections
- Privileges: User
- Operating System: Windows Server 2012, Windows Server 2012R2, Windows Server 2016, Windows Server 2019
- ATT&CK: [[kb/attack/techniques/T1036-masquerading|T1036]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_lolbin_diantz_ads.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_lolbin_diantz_remote_cab.yml
- IOC: diantz storing data into alternate data streams.
- IOC: diantz getting a file from a remote machine or the internet.

## Resources

- {'Link': 'https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/diantz'}
- {'Link': 'https://ss64.com/nt/makecab-directives.html'}

## Acknowledgements

- {'Person': 'Tamir Yehuda', 'Handle': '@tim8288'}
- {'Person': 'Hai Vaknin', 'Handle': '@vakninhai'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Diantz.yml)
