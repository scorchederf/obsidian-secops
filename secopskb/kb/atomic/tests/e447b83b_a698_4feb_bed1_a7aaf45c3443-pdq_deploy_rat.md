---
atomic_guid: "e447b83b-a698-4feb-bed1-a7aaf45c3443"
title: "PDQ Deploy RAT"
framework: "atomic"
generated: "true"
attack_technique_id: "T1072"
attack_technique_name: "Software Deployment Tools"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1072/T1072.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "e447b83b-a698-4feb-bed1-a7aaf45c3443"
  - "PDQ Deploy RAT"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# PDQ Deploy RAT

An adversary may use PDQ Deploy Software to deploy the Remote Adminstartion Tool, this will start the PDQ console.

## Metadata

- Atomic GUID: e447b83b-a698-4feb-bed1-a7aaf45c3443
- Technique: T1072: Software Deployment Tools
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Dependency Executor: powershell
- Source Path: atomics/T1072/T1072.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1072-software_deployment_tools|T1072]]

## Input Arguments

### PDQ_Deploy_exe

- description: The PDQDeployConsole.exe executable from PDQDeploysetup.exe
- type: path
- default: Admin Arsenal/PDQ Deploy/PDQDeployConsole.exe

### PDQ_Deploy_installer

- description: PDQ Deploy Install
- type: path
- default: PDQDeploysetup.exe

## Dependencies

PDQ Deploy will be installed at specified location (#{PDQ_Deploy_exe})

### Prerequisite Check

```powershell
if (Test-Path "${env:ProgramFiles(x86)}/#{PDQ_Deploy_exe}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
Write-Host Downloading PDQ Deploy installer
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
Invoke-WebRequest "https://download.pdq.com/release/19/Deploy_19.3.350.0.exe" -OutFile "PathToAtomicsFolder\..\ExternalPayloads\#{PDQ_Deploy_installer}"
Write-Host Install PDQ Deploy
Start-Process "PathToAtomicsFolder\..\ExternalPayloads\#{PDQ_Deploy_installer}" -Wait -ArgumentList "/s"
```

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
"%PROGRAMFILES(x86)%/#{PDQ_Deploy_exe}"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1072/T1072.yaml)
