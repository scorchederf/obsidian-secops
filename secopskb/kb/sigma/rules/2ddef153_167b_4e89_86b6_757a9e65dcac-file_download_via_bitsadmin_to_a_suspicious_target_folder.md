---
sigma_id: "2ddef153-167b-4e89-86b6-757a9e65dcac"
title: "File Download Via Bitsadmin To A Suspicious Target Folder"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_bitsadmin_download_susp_targetfolder.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_bitsadmin_download_susp_targetfolder.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "2ddef153-167b-4e89-86b6-757a9e65dcac"
  - "File Download Via Bitsadmin To A Suspicious Target Folder"
attack_technique_ids:
  - "T1197"
  - "T1036.003"
  - "T1105"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# File Download Via Bitsadmin To A Suspicious Target Folder

Detects usage of bitsadmin downloading a file to a suspicious target folder

## Metadata

- Rule ID: 2ddef153-167b-4e89-86b6-757a9e65dcac
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems), Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-06-28
- Modified: 2025-12-10
- Source Path: rules/windows/process_creation/proc_creation_win_bitsadmin_download_susp_targetfolder.yml

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
selection_flags:
  CommandLine|contains:
  - ' /transfer '
  - ' /create '
  - ' /addfile '
selection_folder:
  CommandLine|contains:
  - :\Perflogs
  - :\ProgramData\
  - :\Temp\
  - :\Users\Public\
  - :\Windows\
  - \$Recycle.Bin\
  - \AppData\Local\
  - \AppData\Roaming\
  - \Contacts\
  - \Desktop\
  - \Favorites\
  - \Favourites\
  - \inetpub\wwwroot\
  - \Music\
  - \Pictures\
  - \Start Menu\Programs\Startup\
  - \Users\Default\
  - \Videos\
  - '%ProgramData%'
  - '%public%'
  - '%temp%'
  - '%tmp%'
condition: all of selection_*
```

## False Positives

- Unknown

## Simulation

### Windows - BITSAdmin BITS Download

- Atomic Test: [[kb/atomic/tests/a1921cd3_9a2d_47d5_a891_f1d0f2a7a31b-windows_bitsadmin_bits_download|a1921cd3-9a2d-47d5-a891-f1d0f2a7a31b]]
- atomic_guid: a1921cd3-9a2d-47d5-a891-f1d0f2a7a31b
- name: Windows - BITSAdmin BITS Download
- technique: T1105
- type: atomic-red-team

## References

- https://blog.netspi.com/15-ways-to-download-a-file/#bitsadmin
- https://isc.sans.edu/diary/22264
- https://lolbas-project.github.io/lolbas/Binaries/Bitsadmin/
- https://blog.talosintelligence.com/breaking-the-silence-recent-truebot-activity/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_bitsadmin_download_susp_targetfolder.yml)
