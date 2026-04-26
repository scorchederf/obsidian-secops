---
atomic_guid: "6ed67921-1774-44ba-bac6-adb51ed60660"
title: "Copy a sensitive File over Administrative share with copy"
framework: "atomic"
generated: "true"
attack_technique_id: "T1039"
attack_technique_name: "Data from Network Shared Drive"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1039/T1039.yaml"
build_date: "2026-04-26 14:38:39"
executor: "command_prompt"
aliases:
  - "6ed67921-1774-44ba-bac6-adb51ed60660"
  - "Copy a sensitive File over Administrative share with copy"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Copy a sensitive File over Administrative share with copy

Copy from sensitive File from the c$ of another LAN computer with copy cmd
https://twitter.com/SBousseaden/status/1211636381086339073

## Metadata

- Atomic GUID: 6ed67921-1774-44ba-bac6-adb51ed60660
- Technique: T1039: Data from Network Shared Drive
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Dependency Executor: powershell
- Source Path: atomics/T1039/T1039.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1039-data_from_network_shared_drive|T1039]]

## Input Arguments

### local_file

- description: Local name
- type: string
- default: Easter_egg.password

### remote

- description: Remote server name
- type: string
- default: 127.0.0.1

### share_file

- description: Remote Path to the file
- type: path
- default: Windows\temp\Easter_Bunny.password

## Dependencies

Administrative share must exist on #{remote}

### Prerequisite Check

```text
if (Test-Path "\\#{remote}\C$") {exit 0} else {exit 1}
```

### Get Prerequisite

```text
Write-Host 'Please Enable "C$" share on #{remote}'
```

"\\#{remote}\C$\#{share_file}" must exist on #{remote}

### Prerequisite Check

```text
if (Test-Path "\\#{remote}\C$\#{share_file}") {exit 0} else {exit 1}
```

### Get Prerequisite

```text
Out-File -FilePath "\\#{remote}\C$\#{share_file}"
```

## Executor

- elevation_required: True
- name: command_prompt

### Command

```commandprompt
copy \\#{remote}\C$\#{share_file} %TEMP%\#{local_file}
```

### Cleanup

```commandprompt
del \\#{remote}\C$\#{share_file}
del %TEMP%\#{local_file}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1039/T1039.yaml)
