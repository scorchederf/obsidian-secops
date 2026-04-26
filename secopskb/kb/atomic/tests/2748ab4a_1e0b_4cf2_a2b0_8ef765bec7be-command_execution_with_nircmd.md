---
atomic_guid: "2748ab4a-1e0b-4cf2-a2b0-8ef765bec7be"
title: "Command Execution with NirCmd"
framework: "atomic"
generated: "true"
attack_technique_id: "T1564"
attack_technique_name: "Hide Artifacts"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1564/T1564.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "2748ab4a-1e0b-4cf2-a2b0-8ef765bec7be"
  - "Command Execution with NirCmd"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Command Execution with NirCmd

NirCmd is used by threat actors to execute commands, which can include recon and privilege escalation via running commands via the SYSTEM account
See https://www.kroll.com/en/insights/publications/cyber/black-basta-technical-analysis

## Metadata

- Atomic GUID: 2748ab4a-1e0b-4cf2-a2b0-8ef765bec7be
- Technique: T1564: Hide Artifacts
- Platforms: windows
- Executor: powershell
- Elevation Required: False
- Dependency Executor: powershell
- Source Path: atomics/T1564/T1564.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1564-hide_artifacts|T1564]]

## Input Arguments

### cleanup_command_to_execute

- description: Cleanup command to undo the arbitrary command ran by nircmd
- type: Path
- default: win child class "Shell_TrayWnd" show class "TrayClockWClass"

### command_to_execute

- description: Command for nircmd to execute
- type: Path
- default: win child class "Shell_TrayWnd" hide class "TrayClockWClass"

### nircmd_location

- description: Location of nircmd executable
- type: Path
- default: PathToAtomicsFolder\..\ExternalPayloads\nircmd.exe

## Dependencies

The Nircmd executable must exist at (#{nircmd_location})

### Prerequisite Check

```powershell
if (Test-Path "#{nircmd_location}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
invoke-webrequest "https://www.nirsoft.net/utils/nircmd-x64.zip" -outfile "PathToAtomicsFolder\..\ExternalPayloads\nircmd.zip" 
expand-archive -path "PathToAtomicsFolder\..\ExternalPayloads\nircmd.zip" -destinationpath "PathToAtomicsFolder\..\ExternalPayloads\"
```

## Executor

- elevation_required: False
- name: powershell

### Command

```powershell
cmd /c "#{nircmd_location}" #{command_to_execute}
```

### Cleanup

```powershell
cmd /c "#{nircmd_location}" #{cleanup_command_to_execute} -erroraction silentlycontinue | out-null
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1564/T1564.yaml)
