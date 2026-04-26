---
car_id: "CAR-2019-08-002"
title: "Active Directory Dumping via NTDSUtil"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2019-08-002/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2019-08-002.yaml"
build_date: "2026-04-26 13:49:48"
aliases:
  - "CAR-2019-08-002"
  - "Active Directory Dumping via NTDSUtil"
attack_technique_ids:
  - "T1003"
  - "T1003.003"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# CAR-2019-08-002: Active Directory Dumping via NTDSUtil

## Metadata

- CAR ID: CAR-2019-08-002
- Submission Date: 2019/08/13
- Information Domain: Host
- Analytic Type: TTP
- Platforms: Windows
- Data Subtypes: File
- Contributors: Tony Lambert/Red Canary

## Description

The NTDSUtil tool may be used to dump a Microsoft Active Directory database to disk for processing with a credential access tool such as Mimikatz. This is performed by launching `ntdsutil.exe` as a privileged user with command line arguments indicating that media should be created for offline Active Directory installation and specifying a folder path. This process will create a copy of the Active Directory database, `ntds.dit`, to the specified folder path.

This requires filesystem data to determine whether files have been created.

## ATT&CK Coverage

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003]] (coverage: Low; tactics: TA0006)
  - [[kb/attack/techniques/T1003-os_credential_dumping|T1003.003]]

## Implementations

### Pseudocode

This base pseudocode looks for file create events where a file with a name of ntds.dit is created by the ntdsutil process.

```pseudocode
files = search File:Create
ntds_dump = filter files where (
  file_name = "ntds.dit"  and
  image_path = "*ntdsutil.exe")
output ntds_dump
```

### Splunk

A Splunk/Sysmon version of the above pseudocode.

- Data Model: Sysmon native

```splunk
index=__your_sysmon_index__ EventCode=11 TargetFilename="*ntds.dit" Image="*ntdsutil.exe"
```

### EQL

An EQL version of the above pseudocode.

- Data Model: EQL native

```eql
file where file_name == "ntds.dit" and process_name == "ntdsutil.exe"
```

### LogPoint

LogPoint version of the above pseudocode.

- Data Model: LogPoint native

```logpoint
norm_id=WindowsSysmon event_id=11 file="*ntds.dit" source_image="*ntdsutil.exe"
```

## Data Model References

- file/create/file_name
- file/create/image_path

## Unit Tests

1. Open a Windows Command Prompt or PowerShell instance as Administrator
2. Execute `ntdsutil.exe “ac i ntds” “ifm” “create full c:\temp” q q`

## D3FEND Mappings

- [[kb/defend/techniques/D3-PSA-process_spawn_analysis|D3-PSA: Process Spawn Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2019-08-002/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2019-08-002.yaml)
