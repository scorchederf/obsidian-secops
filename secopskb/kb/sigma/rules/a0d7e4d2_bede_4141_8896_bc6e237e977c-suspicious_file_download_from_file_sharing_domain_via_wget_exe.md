---
sigma_id: "a0d7e4d2-bede-4141-8896-bc6e237e977c"
title: "Suspicious File Download From File Sharing Domain Via Wget.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_wget_download_susp_file_sharing_domains.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wget_download_susp_file_sharing_domains.yml"
build_date: "2026-04-26 17:03:22"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "a0d7e4d2-bede-4141-8896-bc6e237e977c"
  - "Suspicious File Download From File Sharing Domain Via Wget.EXE"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Suspicious File Download From File Sharing Domain Via Wget.EXE

Detects potentially suspicious file downloads from file sharing domains using wget.exe

## Metadata

- Rule ID: a0d7e4d2-bede-4141-8896-bc6e237e977c
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-05-05
- Modified: 2025-12-10
- Source Path: rules/windows/process_creation/proc_creation_win_wget_download_susp_file_sharing_domains.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection_img:
- Image|endswith: \wget.exe
- OriginalFileName: wget.exe
selection_websites:
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
  - pixeldrain.com
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
selection_http:
  CommandLine|contains: http
selection_flag:
- CommandLine|re: \s-O\s
- CommandLine|contains: --output-document
selection_ext:
  CommandLine|endswith:
  - .ps1
  - .ps1'
  - .ps1"
  - .dat
  - .dat'
  - .dat"
  - .msi
  - .msi'
  - .msi"
  - .bat
  - .bat'
  - .bat"
  - .exe
  - .exe'
  - .exe"
  - .vbs
  - .vbs'
  - .vbs"
  - .vbe
  - .vbe'
  - .vbe"
  - .hta
  - .hta'
  - .hta"
  - .dll
  - .dll'
  - .dll"
  - .psm1
  - .psm1'
  - .psm1"
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://labs.withsecure.com/publications/fin7-target-veeam-servers
- https://github.com/WithSecureLabs/iocs/blob/344203de742bb7e68bd56618f66d34be95a9f9fc/FIN7VEEAM/iocs.csv
- https://www.microsoft.com/en-us/security/blog/2024/01/17/new-ttps-observed-in-mint-sandstorm-campaign-targeting-high-profile-individuals-at-universities-and-research-orgs/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wget_download_susp_file_sharing_domains.yml)
