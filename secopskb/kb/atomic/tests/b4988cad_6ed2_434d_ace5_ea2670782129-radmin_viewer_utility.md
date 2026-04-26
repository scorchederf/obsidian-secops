---
atomic_guid: "b4988cad-6ed2-434d-ace5-ea2670782129"
title: "Radmin Viewer Utility"
framework: "atomic"
generated: "true"
attack_technique_id: "T1072"
attack_technique_name: "Software Deployment Tools"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1072/T1072.yaml"
build_date: "2026-04-26 14:38:39"
executor: "command_prompt"
aliases:
  - "b4988cad-6ed2-434d-ace5-ea2670782129"
  - "Radmin Viewer Utility"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Radmin Viewer Utility

An adversary may use Radmin Viewer Utility to remotely control Windows device, this will start the radmin console.

## Metadata

- Atomic GUID: b4988cad-6ed2-434d-ace5-ea2670782129
- Technique: T1072: Software Deployment Tools
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Dependency Executor: powershell
- Source Path: atomics/T1072/T1072.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1072-software_deployment_tools|T1072]]

## Input Arguments

### radmin_exe

- description: The radmin.exe executable from RadminViewer.msi
- type: path
- default: Radmin Viewer 3/Radmin.exe

### radmin_installer

- description: Radmin Viewer installer
- type: path
- default: RadminViewer.msi

## Dependencies

Radmin Viewer Utility must be installed at specified location (#{radmin_exe})

### Prerequisite Check

```text
if (Test-Path "${env:ProgramFiles(x86)}/#{radmin_exe}") {exit 0} else {exit 1}
```

### Get Prerequisite

```text
Write-Host Downloading radmin installer
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
Invoke-WebRequest "https://www.radmin.com/download/Radmin_Viewer_3.5.2.1_EN.msi" -OutFile "PathToAtomicsFolder\..\ExternalPayloads\#{radmin_installer}"
Write-Host Install Radmin
Start-Process msiexec  -Wait -ArgumentList /i , "PathToAtomicsFolder\..\ExternalPayloads\#{radmin_installer}", /qn
```

## Executor

- elevation_required: True
- name: command_prompt

### Command

```commandprompt
"%PROGRAMFILES(x86)%/#{radmin_exe}"
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1072/T1072.yaml)
