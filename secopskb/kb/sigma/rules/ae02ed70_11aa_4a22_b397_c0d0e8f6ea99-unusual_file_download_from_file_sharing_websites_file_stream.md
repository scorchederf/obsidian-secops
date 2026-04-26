---
sigma_id: "ae02ed70-11aa-4a22-b397-c0d0e8f6ea99"
title: "Unusual File Download From File Sharing Websites - File Stream"
framework: "sigma"
generated: "true"
source_path: "rules/windows/create_stream_hash/create_stream_hash_file_sharing_domains_download_unusual_extension.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/create_stream_hash/create_stream_hash_file_sharing_domains_download_unusual_extension.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "windows / create_stream_hash"
aliases:
  - "ae02ed70-11aa-4a22-b397-c0d0e8f6ea99"
  - "Unusual File Download From File Sharing Websites - File Stream"
attack_technique_ids:
  - "T1564.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Unusual File Download From File Sharing Websites - File Stream

Detects the download of suspicious file type from a well-known file and paste sharing domain

## Metadata

- Rule ID: ae02ed70-11aa-4a22-b397-c0d0e8f6ea99
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems)
- Date: 2022-08-24
- Modified: 2025-12-10
- Source Path: rules/windows/create_stream_hash/create_stream_hash_file_sharing_domains_download_unusual_extension.yml

## Logsource

- category: create_stream_hash
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1564-hide_artifacts|T1564.004]]

### Software Tags

- S0139

## Detection

```yaml
selection_domain:
  Contents|contains:
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
selection_extension:
  TargetFilename|contains:
  - .bat:Zone
  - .cmd:Zone
  - .ps1:Zone
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://www.ultimatewindowssecurity.com/securitylog/encyclopedia/event.aspx?eventid=90015
- https://www.cisa.gov/uscert/ncas/alerts/aa22-321a
- https://www.microsoft.com/en-us/security/blog/2024/01/17/new-ttps-observed-in-mint-sandstorm-campaign-targeting-high-profile-individuals-at-universities-and-research-orgs/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/create_stream_hash/create_stream_hash_file_sharing_domains_download_unusual_extension.yml)
