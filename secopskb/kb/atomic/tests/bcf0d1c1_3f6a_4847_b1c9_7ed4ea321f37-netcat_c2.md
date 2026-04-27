---
atomic_guid: "bcf0d1c1-3f6a-4847-b1c9-7ed4ea321f37"
title: "Netcat C2"
framework: "atomic"
generated: "true"
attack_technique_id: "T1095"
attack_technique_name: "Non-Application Layer Protocol"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1095/T1095.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "bcf0d1c1-3f6a-4847-b1c9-7ed4ea321f37"
  - "Netcat C2"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Netcat C2

Start C2 Session Using Ncat
To start the listener on a Linux device, type the following: 
nc -l -p <port>

## Metadata

- Atomic GUID: bcf0d1c1-3f6a-4847-b1c9-7ed4ea321f37
- Technique: T1095: Non-Application Layer Protocol
- Platforms: windows
- Executor: powershell
- Dependency Executor: powershell
- Source Path: atomics/T1095/T1095.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1095-non-application_layer_protocol|T1095]]

## Input Arguments

### ncat_exe

- description: The location of ncat.exe
- type: path
- default: PathToAtomicsFolder\..\ExternalPayloads\T1095\nmap-7.80\ncat.exe

### ncat_path

- description: The folder path of ncat.exe
- type: path
- default: PathToAtomicsFolder\..\ExternalPayloads\T1095

### server_ip

- description: The IP address or domain name of the listening server
- type: string
- default: 127.0.0.1

### server_port

- description: The port for the C2 connection
- type: integer
- default: 80

## Dependencies

ncat.exe must be available at specified location (#{ncat_exe})

### Prerequisite Check

```powershell
if( Test-Path "#{ncat_exe}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
New-Item -ItemType Directory -Force -Path "#{ncat_path}" | Out-Null
$parentpath = Split-Path (Split-Path "#{ncat_exe}"); $zippath = "$parentpath\nmap.zip"
Invoke-WebRequest  "https://nmap.org/dist/nmap-7.80-win32.zip" -OutFile "$zippath"
  Expand-Archive $zippath $parentpath -Force
  $unzipPath = Join-Path $parentPath "nmap-7.80"
if( $null -eq (Get-ItemProperty HKLM:\Software\Microsoft\Windows\CurrentVersion\Uninstall\* | ?{$_.DisplayName -like "Microsoft Visual C++*"}) ) {
  Start-Process (Join-Path $unzipPath "vcredist_x86.exe")
}
```

## Executor

- name: powershell

### Command

```powershell
cmd /c "#{ncat_exe}" #{server_ip} #{server_port}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1095/T1095.yaml)
