---
atomic_guid: "88b81702-a1c0-49a9-95b2-2dd53d755767"
title: "Create and start VirtualBox virtual machine"
framework: "atomic"
generated: "true"
attack_technique_id: "T1564.006"
attack_technique_name: "Run Virtual Instance"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1564.006/T1564.006.yaml"
build_date: "2026-04-26 17:02:13"
executor: "command_prompt"
aliases:
  - "88b81702-a1c0-49a9-95b2-2dd53d755767"
  - "Create and start VirtualBox virtual machine"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Create and start VirtualBox virtual machine

Create a simple VirtualBox VM and start up the machine
Cleanup command stops and deletes the newly created VM and associated files
https://www.virtualbox.org/manual/ch08.html#vboxmanage-startvm
https://news.sophos.com/en-us/2020/05/21/ragnar-locker-ransomware-deploys-virtual-machine-to-dodge-security/
https://attack.mitre.org/techniques/T1564/006/

## Metadata

- Atomic GUID: 88b81702-a1c0-49a9-95b2-2dd53d755767
- Technique: T1564.006: Run Virtual Instance
- Platforms: windows
- Executor: command_prompt
- Elevation Required: False
- Dependency Executor: powershell
- Source Path: atomics/T1564.006/T1564.006.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1564-hide_artifacts|T1564.006]]

## Input Arguments

### vboxmanage_exe

- description: Path to the executable for VBoxManage, the command-line interface to VirtualBox
- type: path
- default: C:\Program Files\Oracle\VirtualBox\VBoxManage.exe

### virtualbox_download

- description: URL for the current installer for the Windows version of VirtualBox, as of March 2022
- type: url
- default: https://download.virtualbox.org/virtualbox/6.1.32/VirtualBox-6.1.32-149290-Win.exe

### virtualbox_exe

- description: Path to the VirtualBox executable
- type: path
- default: C:\Program Files\Oracle\VirtualBox\VirtualBox.exe

### virtualbox_installer

- description: Executable for the Virtualbox installer
- type: string
- default: VirtualBox-6.1.32-149290-Win.exe

### vm_name

- description: Name of the new virtual machine
- type: string
- default: Atomic VM

## Dependencies

VirtualBox must exist on disk at specified locations (#{virtualbox_exe})

### Prerequisite Check

```powershell
if (Test-Path "#{virtualbox_exe}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
$wc = New-Object System.Net.WebClient
$wc.DownloadFile("#{virtualbox_download}","PathToAtomicsFolder\..\ExternalPayloads\#{virtualbox_installer}")
start-process -FilePath "PathToAtomicsFolder\..\ExternalPayloads\#{virtualbox_installer}" -ArgumentList "--silent" -Wait
```

VBoxManage must exist on disk at specified locations (#{vboxmanage_exe})

### Prerequisite Check

```powershell
if (Test-Path "#{vboxmanage_exe}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
$wc = New-Object System.Net.WebClient
$wc.DownloadFile("#{virtualbox_download}","PathToAtomicsFolder\..\ExternalPayloads\#{virtualbox_installer}")
start-process -FilePath "PathToAtomicsFolder\..\ExternalPayloads\#{virtualbox_installer}" -ArgumentList "--silent" -Wait
```

## Executor

- elevation_required: False
- name: command_prompt

### Command

```cmd
"#{vboxmanage_exe}" createvm --name "#{vm_name}" --register
"#{vboxmanage_exe}" modifyvm "#{vm_name}" --firmware efi
"#{vboxmanage_exe}" startvm "#{vm_name}"
```

### Cleanup

```cmd
"#{vboxmanage_exe}" controlvm "#{vm_name}" poweroff
"#{vboxmanage_exe}" unregistervm "#{vm_name}" --delete
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1564.006/T1564.006.yaml)
