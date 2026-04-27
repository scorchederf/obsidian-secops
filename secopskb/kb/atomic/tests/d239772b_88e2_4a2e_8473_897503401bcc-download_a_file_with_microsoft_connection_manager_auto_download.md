---
atomic_guid: "d239772b-88e2-4a2e-8473-897503401bcc"
title: "Download a file with Microsoft Connection Manager Auto-Download"
framework: "atomic"
generated: "true"
attack_technique_id: "T1105"
attack_technique_name: "Ingress Tool Transfer"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1105/T1105.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "d239772b-88e2-4a2e-8473-897503401bcc"
  - "Download a file with Microsoft Connection Manager Auto-Download"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Download a file with Microsoft Connection Manager Auto-Download

Uses the cmdl32 to download arbitrary file from the internet. The cmdl32 package is allowed to install the profile used to launch the VPN connection. However, the config is modified to download the arbitary file. 
The issue of cmdl32.exe detecting and deleting the payload by identifying it as not a VPN Servers profile is avoided by setting a temporary TMP folder and denying the delete permission to all files for the user.
Upon successful execution the test will open calculator and Notepad executable for 10 seconds.
reference:
https://twitter.com/ElliotKillick/status/1455897435063074824
https://github.com/LOLBAS-Project/LOLBAS/pull/151
https://lolbas-project.github.io/lolbas/Binaries/Cmdl32/
https://strontic.github.io/xcyclopedia/library/cmdl32.exe-FA1D5B8802FFF4A85B6F52A52C871BBB.html

## Metadata

- Atomic GUID: d239772b-88e2-4a2e-8473-897503401bcc
- Technique: T1105: Ingress Tool Transfer
- Platforms: windows
- Executor: command_prompt
- Dependency Executor: powershell
- Source Path: atomics/T1105/T1105.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

## Input Arguments

### Path_to_file

- description: Path to the Batch script
- type: path
- default: PathToAtomicsFolder\T1105\src\T1105.bat

## Dependencies

#{Path_to_file} must exist on system.

### Prerequisite Check

```powershell
if (Test-Path "#{Path_to_file}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory (split-path "#{Path_to_file}") -ErrorAction ignore | Out-Null
Invoke-WebRequest "https://github.com/redcanaryco/atomic-red-team/raw/master/atomics/T1105/src/T1105.bat" -OutFile "#{Path_to_file}"
```

## Executor

- name: command_prompt

### Command

```cmd
"#{Path_to_file}" 1>NUL
```

### Cleanup

```cmd
del /f/s/q %temp%\T1105 >nul 2>&1
rmdir /s/q %temp%\T1105 >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1105/T1105.yaml)
