---
title: "Tar.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Tar.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Tar.yml"
build_date: "2026-04-27 18:39:01"
category: "OSBinaries"
aliases:
  - "Tar.exe"
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

# Tar.exe

Used by Windows to extract and create archives.

## Metadata

- Category: OSBinaries
- Created: 2023-01-30
- Author: Brian Lucero
- Source Path: yml/OSBinaries/Tar.yml

## Paths

- `C:\Windows\System32\tar.exe`
- `C:\Windows\SysWOW64\tar.exe`

## Commands

### 1. ADS

Compress one or more files to an alternate data stream (ADS).

```cmd
tar -cf {PATH}:ads {PATH_ABSOLUTE:folder}
```

- Use Case: Can be used to evade defensive countermeasures, or to hide as part of a persistence mechanism
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1564-hide_artifacts|T1564.004]]

### 2. ADS

Decompress a compressed file from an alternate data stream (ADS).

```cmd
tar -xf {PATH}:ads
```

- Use Case: Can be used to evade defensive countermeasures, or to hide as part of a persistence mechanism
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1564-hide_artifacts|T1564.004]]

### 3. Copy

Extracts archive.tar from the remote (internal) host to the current host.

```cmd
tar -xf {PATH_SMB:.tar}
```

- Use Case: Copy files
- Privileges: User
- Operating System: Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/e1a713d264ac072bb76b5c4e5f41315a015d3f41/rules/windows/process_creation/proc_creation_win_tar_compression.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/e1a713d264ac072bb76b5c4e5f41315a015d3f41/rules/windows/process_creation/proc_creation_win_tar_extraction.yml
- IOC: tar.exe extracting files from a remote host within the environment
- IOC: Abnormal processes spawning tar.exe
- IOC: tar.exe interacting with alternate data streams (ADS)

## Resources

- {'Link': 'https://twitter.com/Cyber_Sorcery/status/1619819249886969856'}

## Acknowledgements

- {'Person': 'Brian Lucero', 'Handle': '@Cyber_Sorcery'}
- {'Person': 'Avester Fahimipour'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Tar.yml)
