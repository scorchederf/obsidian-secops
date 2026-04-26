---
atomic_guid: "6cd715aa-20ac-4be1-a8f1-dda7bae160bd"
title: "Enable Local and Remote Symbolic Links via Powershell"
framework: "atomic"
generated: "true"
attack_technique_id: "T1222"
attack_technique_name: "File and Directory Permissions Modification"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1222/T1222.yaml"
build_date: "2026-04-26 14:38:40"
executor: "powershell"
aliases:
  - "6cd715aa-20ac-4be1-a8f1-dda7bae160bd"
  - "Enable Local and Remote Symbolic Links via Powershell"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Enable Local and Remote Symbolic Links via Powershell

Use Powershell to enable both ‘remote to local’ and ‘remote to remote’ symbolic links. This allows access to files from local shortcuts with local or remote paths.
[reference](https://symantec-enterprise-blogs.security.com/threat-intelligence/noberus-blackcat-alphv-rust-ransomware/)

## Metadata

- Atomic GUID: 6cd715aa-20ac-4be1-a8f1-dda7bae160bd
- Technique: T1222: File and Directory Permissions Modification
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1222/T1222.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1222-file_and_directory_permissions_modification|T1222]]

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
New-ItemProperty -Path HKLM:\Software\Policies\Microsoft\Windows\Filesystems\NTFS -Name SymlinkRemoteToLocalEvaluation -PropertyType DWORD -Value 1 -Force -ErrorAction Ignore
New-ItemProperty -Path HKLM:\Software\Policies\Microsoft\Windows\Filesystems\NTFS -Name SymlinkRemoteToRemoteEvaluation -PropertyType DWORD -Value 1 -Force -ErrorAction Ignore
```

### Cleanup

```powershell
New-ItemProperty -Path HKLM:\Software\Policies\Microsoft\Windows\Filesystems\NTFS -Name SymlinkRemoteToLocalEvaluation -PropertyType DWORD -Value 0 -Force -ErrorAction Ignore
New-ItemProperty -Path HKLM:\Software\Policies\Microsoft\Windows\Filesystems\NTFS -Name SymlinkRemoteToRemoteEvaluation -PropertyType DWORD -Value 0 -Force -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1222/T1222.yaml)
