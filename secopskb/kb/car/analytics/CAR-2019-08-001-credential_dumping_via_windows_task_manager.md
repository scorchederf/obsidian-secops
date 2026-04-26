---
car_id: "CAR-2019-08-001"
title: "Credential Dumping via Windows Task Manager"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2019-08-001/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2019-08-001.yaml"
build_date: "2026-04-26 13:49:48"
aliases:
  - "CAR-2019-08-001"
  - "Credential Dumping via Windows Task Manager"
attack_technique_ids:
  - "T1003"
  - "T1003.001"
platforms:
  - "Windows"
implementation_types:
  - "Pseudocode"
  - "Splunk"
  - "EQL"
  - "LogPoint"
tags:
  - "car"
  - "analytic"
  - "detection"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[workspaces/index|Notes]]

# CAR-2019-08-001: Credential Dumping via Windows Task Manager

## Metadata

- CAR ID: CAR-2019-08-001
- Submission Date: 2019/08/05
- Information Domain: Host
- Analytic Type: TTP
- Platforms: Windows
- Data Subtypes: File
- Contributors: Tony Lambert/Red Canary

## Description

The Windows Task Manager may be used to dump the memory space of `lsass.exe` to disk for processing with a credential access tool such as Mimikatz. This is performed by launching Task Manager as a privileged user, selecting `lsass.exe`, and clicking "Create dump file". This saves a dump file to disk with a deterministic name that includes the name of the process being dumped.

This requires filesystem data to determine whether files have been created.

## ATT&CK Coverage

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003]] (coverage: Low; tactics: TA0006)
  - [[kb/attack/techniques/T1003-os_credential_dumping|T1003.001]]

## Implementations

### Pseudocode

This base pseudocode looks for file create events where a file with a name similar to lsass.dmp is created by the Windows task manager process.

```pseudocode
files = search File:Create
lsass_dump = filter files where (
  file_name = "lsass*.dmp"  and
  image_path = "C:\Windows\*\taskmgr.exe")
output lsass_dump
```

### Splunk

A Splunk/Sysmon version of the above pseudocode.

- Data Model: Sysmon native

```splunk
index=__your_sysmon_index__ EventCode=11 TargetFilename="*lsass*.dmp" Image="C:\\Windows\\*\\taskmgr.exe"
```

### EQL

An EQL version of the above pseudocode.

- Data Model: EQL native

```eql
file where file_name == "lsass*.dmp" and process_name == "taskmgr.exe"
```

### LogPoint

LogPoint version of the above pseudocode.

- Data Model: LogPoint native

```logpoint
norm_id=WindowsSysmon event_id=11 file="*lsass*.dmp" source_image="C:\Windows\*\taskmgr.exe"
```

## Data Model References

- file/create/file_name
- file/create/image_path

## Unit Tests

1. Open Windows Task Manager as Administrator
2. Select lsass.exe
3. Right-click on lsass.exe and select "Create dump file".

## D3FEND Mappings

- [[kb/defend/techniques/D3-FCA-file_creation_analysis|D3-FCA: File Creation Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2019-08-001/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2019-08-001.yaml)
