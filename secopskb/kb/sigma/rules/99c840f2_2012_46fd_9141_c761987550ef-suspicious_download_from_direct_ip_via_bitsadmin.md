---
sigma_id: "99c840f2-2012-46fd-9141-c761987550ef"
title: "Suspicious Download From Direct IP Via Bitsadmin"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_bitsadmin_download_direct_ip.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_bitsadmin_download_direct_ip.yml"
build_date: "2026-04-26 17:03:22"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "99c840f2-2012-46fd-9141-c761987550ef"
  - "Suspicious Download From Direct IP Via Bitsadmin"
attack_technique_ids:
  - "T1197"
  - "T1036.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Suspicious Download From Direct IP Via Bitsadmin

Detects usage of bitsadmin downloading a file using an URL that contains an IP

## Metadata

- Rule ID: 99c840f2-2012-46fd-9141-c761987550ef
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2022-06-28
- Modified: 2023-02-15
- Source Path: rules/windows/process_creation/proc_creation_win_bitsadmin_download_direct_ip.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1197-bits_jobs|T1197]]
- [[kb/attack/techniques/T1036-masquerading|T1036.003]]

### Software Tags

- S0190

## Detection

```yaml
selection_img:
- Image|endswith: \bitsadmin.exe
- OriginalFileName: bitsadmin.exe
selection_flags:
  CommandLine|contains:
  - ' /transfer '
  - ' /create '
  - ' /addfile '
selection_extension:
  CommandLine|contains:
  - ://1
  - ://2
  - ://3
  - ://4
  - ://5
  - ://6
  - ://7
  - ://8
  - ://9
filter_seven_zip:
  CommandLine|contains: ://7-
condition: all of selection_* and not 1 of filter_*
```

## False Positives

- Unknown

## References

- https://blog.netspi.com/15-ways-to-download-a-file/#bitsadmin
- https://isc.sans.edu/diary/22264
- https://lolbas-project.github.io/lolbas/Binaries/Bitsadmin/
- https://blog.talosintelligence.com/breaking-the-silence-recent-truebot-activity/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_bitsadmin_download_direct_ip.yml)
