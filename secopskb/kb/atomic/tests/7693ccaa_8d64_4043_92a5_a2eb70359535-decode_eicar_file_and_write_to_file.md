---
atomic_guid: "7693ccaa-8d64-4043-92a5-a2eb70359535"
title: "Decode Eicar File and Write to File"
framework: "atomic"
generated: "true"
attack_technique_id: "T1027.013"
attack_technique_name: "Obfuscated Files or Information: Encrypted/Encoded File"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1027.013/T1027.013.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "7693ccaa-8d64-4043-92a5-a2eb70359535"
  - "Decode Eicar File and Write to File"
platforms:
  - "windows"
  - "macos"
  - "linux"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Decode Eicar File and Write to File

Decode the eicar value, and write it to file, for AV/EDR to try to catch.

## Metadata

- Atomic GUID: 7693ccaa-8d64-4043-92a5-a2eb70359535
- Technique: T1027.013: Obfuscated Files or Information: Encrypted/Encoded File
- Platforms: windows, macos, linux
- Executor: powershell
- Elevation Required: False
- Source Path: atomics/T1027.013/T1027.013.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1027-obfuscated_files_or_information|T1027.013]]

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
$encodedString = "WDVPIVAlQEFQWzRcUFpYNTQoUF4pN0NDKTd9JEVJQ0FSLVNUQU5EQVJELUFOVElWSVJVUy1URVNULUZJTEUhJEgrSCo="
$bytes = [System.Convert]::FromBase64String($encodedString)
$decodedString = [System.Text.Encoding]::UTF8.GetString($bytes)
#write the decoded eicar string to file
$decodedString | Out-File $env:temp\T1027.013_decodedEicar.txt
```

### Cleanup

```powershell
Remove-Item $env:temp\T1027.013_decodedEicar.txt -Force -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1027.013/T1027.013.yaml)
