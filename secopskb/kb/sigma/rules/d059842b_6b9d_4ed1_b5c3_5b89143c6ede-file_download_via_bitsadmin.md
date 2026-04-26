---
sigma_id: "d059842b-6b9d-4ed1-b5c3-5b89143c6ede"
title: "File Download Via Bitsadmin"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_bitsadmin_download.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_bitsadmin_download.yml"
build_date: "2026-04-26 14:14:25"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "d059842b-6b9d-4ed1-b5c3-5b89143c6ede"
  - "File Download Via Bitsadmin"
attack_technique_ids:
  - "T1197"
  - "T1036.003"
  - "T1105"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# File Download Via Bitsadmin

Detects usage of bitsadmin downloading a file

## Metadata

- Rule ID: d059842b-6b9d-4ed1-b5c3-5b89143c6ede
- Status: test
- Level: medium
- Author: Michael Haag, FPT.EagleEye
- Date: 2017-03-09
- Modified: 2023-02-15
- Source Path: rules/windows/process_creation/proc_creation_win_bitsadmin_download.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1197-bits_jobs|T1197]]
- [[kb/attack/techniques/T1036-masquerading|T1036.003]]
- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

### Software Tags

- S0190

## Detection

```yaml
selection_img:
- Image|endswith: \bitsadmin.exe
- OriginalFileName: bitsadmin.exe
selection_cmd:
  CommandLine|contains: ' /transfer '
selection_cli_1:
  CommandLine|contains:
  - ' /create '
  - ' /addfile '
selection_cli_2:
  CommandLine|contains: http
condition: selection_img and (selection_cmd or all of selection_cli_*)
```

## False Positives

- Some legitimate apps use this, but limited.

## Simulation

### Windows - BITSAdmin BITS Download

- atomic_guid: a1921cd3-9a2d-47d5-a891-f1d0f2a7a31b
- name: Windows - BITSAdmin BITS Download
- technique: T1105
- type: atomic-red-team

## References

- https://blog.netspi.com/15-ways-to-download-a-file/#bitsadmin
- https://isc.sans.edu/diary/22264
- https://lolbas-project.github.io/lolbas/Binaries/Bitsadmin/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_bitsadmin_download.yml)
