---
sigma_id: "8518ed3d-f7c9-4601-a26c-f361a4256a0c"
title: "Suspicious Download From File-Sharing Website Via Bitsadmin"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_bitsadmin_download_file_sharing_domains.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_bitsadmin_download_file_sharing_domains.yml"
build_date: "2026-04-26 17:03:22"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "8518ed3d-f7c9-4601-a26c-f361a4256a0c"
  - "Suspicious Download From File-Sharing Website Via Bitsadmin"
attack_technique_ids:
  - "T1197"
  - "T1036.003"
  - "T1105"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Suspicious Download From File-Sharing Website Via Bitsadmin

Detects usage of bitsadmin downloading a file from a suspicious domain

## Metadata

- Rule ID: 8518ed3d-f7c9-4601-a26c-f361a4256a0c
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2022-06-28
- Modified: 2025-12-10
- Source Path: rules/windows/process_creation/proc_creation_win_bitsadmin_download_file_sharing_domains.yml

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
selection_domain:
  CommandLine|contains:
  - .githubusercontent.com
  - anonfiles.com
  - cdn.discordapp.com
  - ddns.net
  - dl.dropboxusercontent.com
  - ghostbin.co
  - github.com
  - glitch.me
  - gofile.io
  - hastebin.com
  - mediafire.com
  - mega.nz
  - onrender.com
  - pages.dev
  - paste.ee
  - pastebin.com
  - pastebin.pl
  - pastetext.net
  - privatlab.com
  - privatlab.net
  - send.exploit.in
  - sendspace.com
  - storage.googleapis.com
  - storjshare.io
  - supabase.co
  - temp.sh
  - transfer.sh
  - trycloudflare.com
  - ufile.io
  - w3spaces.com
  - workers.dev
condition: all of selection_*
```

## False Positives

- Some legitimate apps use this, but limited.

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
- https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/ransomware-hive-conti-avoslocker
- https://www.cisa.gov/uscert/ncas/alerts/aa22-321a
- https://www.microsoft.com/en-us/security/blog/2024/01/17/new-ttps-observed-in-mint-sandstorm-campaign-targeting-high-profile-individuals-at-universities-and-research-orgs/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_bitsadmin_download_file_sharing_domains.yml)
