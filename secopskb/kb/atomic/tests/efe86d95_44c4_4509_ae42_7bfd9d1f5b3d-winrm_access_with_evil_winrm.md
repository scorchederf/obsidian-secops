---
atomic_guid: "efe86d95-44c4-4509-ae42-7bfd9d1f5b3d"
title: "WinRM Access with Evil-WinRM"
framework: "atomic"
generated: "true"
attack_technique_id: "T1021.006"
attack_technique_name: "Remote Services: Windows Remote Management"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1021.006/T1021.006.yaml"
build_date: "2026-04-27 19:12:25"
executor: "powershell"
aliases:
  - "efe86d95-44c4-4509-ae42-7bfd9d1f5b3d"
  - "WinRM Access with Evil-WinRM"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

An adversary may attempt to use Evil-WinRM with a valid account to interact with remote systems that have WinRM enabled

## ATT&CK Mapping

- [[kb/attack/techniques/T1021-remote_services#^t1021006-windows-remote-management|T1021.006: Windows Remote Management]]

## Input Arguments

### destination_address

- description: Remote Host IP or Hostname
- type: string
- default: Target

### password

- description: Password
- type: string
- default: P@ssw0rd1

### user_name

- description: Username
- type: string
- default: Domain\Administrator

## Dependencies

Computer must have Ruby Installed

### Prerequisite Check

```powershell
try {if (ruby -v) {exit 0} else {exit 1}} catch {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
Invoke-WebRequest  -OutFile "PathToAtomicsFolder\..\ExternalPayloads\rubyinstaller-2.7.1-1-x64.exe" https://github.com/oneclick/rubyinstaller2/releases/download/RubyInstaller-2.7.1-1/rubyinstaller-2.7.1-1-x64.exe
$file1= "PathToAtomicsFolder\..\ExternalPayloads\rubyinstaller-2.7.1-1-x64.exe"
Start-Process $file1 /S;
```

Computer must have Evil-WinRM installed

### Prerequisite Check

```powershell
try {if (evil-winrm -h) {exit 0} else {exit 1}} catch {exit 1}
```

### Get Prerequisite

```powershell
gem install evil-winrm
```

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
evil-winrm -i #{destination_address} -u #{user_name} -p #{password}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1021.006/T1021.006.yaml)
