---
sigma_id: "b9cbbc17-d00d-4e3d-a827-b06d03d2380d"
title: "Monitoring For Persistence Via BITS"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_bitsadmin_potential_persistence.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_bitsadmin_potential_persistence.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "b9cbbc17-d00d-4e3d-a827-b06d03d2380d"
  - "Monitoring For Persistence Via BITS"
attack_technique_ids:
  - "T1197"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Monitoring For Persistence Via BITS

BITS will allow you to schedule a command to execute after a successful download to notify you that the job is finished.
When the job runs on the system the command specified in the BITS job will be executed.
This can be abused by actors to create a backdoor within the system and for persistence.
It will be chained in a BITS job to schedule the download of malware/additional binaries and execute the program after being downloaded.

## Metadata

- Rule ID: b9cbbc17-d00d-4e3d-a827-b06d03d2380d
- Status: test
- Level: medium
- Author: Sreeman
- Date: 2020-10-29
- Modified: 2024-01-25
- Source Path: rules/windows/process_creation/proc_creation_win_bitsadmin_potential_persistence.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1197-bits_jobs|T1197]]

## Detection

```yaml
selection_img:
- Image|endswith: \bitsadmin.exe
- OriginalFileName: bitsadmin.exe
selection_cli_notify_1:
  CommandLine|contains: /SetNotifyCmdLine
selection_cli_notify_2:
  CommandLine|contains:
  - '%COMSPEC%'
  - cmd.exe
  - regsvr32.exe
selection_cli_add_1:
  CommandLine|contains: /Addfile
selection_cli_add_2:
  CommandLine|contains:
  - 'http:'
  - 'https:'
  - 'ftp:'
  - 'ftps:'
condition: selection_img and (all of selection_cli_notify_* or all of selection_cli_add_*)
```

## False Positives

- Unknown

## References

- https://www.fireeye.com/blog/threat-research/2020/10/kegtap-and-singlemalt-with-a-ransomware-chaser.html
- http://0xthem.blogspot.com/2014/03/t-emporal-persistence-with-and-schtasks.html
- https://isc.sans.edu/diary/Wipe+the+drive+Stealthy+Malware+Persistence+Mechanism+-+Part+1/15394

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_bitsadmin_potential_persistence.yml)
