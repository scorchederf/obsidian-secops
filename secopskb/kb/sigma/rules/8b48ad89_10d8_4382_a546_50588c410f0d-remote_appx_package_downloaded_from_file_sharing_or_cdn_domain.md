---
sigma_id: "8b48ad89-10d8-4382-a546-50588c410f0d"
title: "Remote AppX Package Downloaded from File Sharing or CDN Domain"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/appxdeployment_server/win_appxdeployment_server_appx_downloaded_from_file_sharing_domains.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/appxdeployment_server/win_appxdeployment_server_appx_downloaded_from_file_sharing_domains.yml"
build_date: "2026-04-26 17:03:21"
status: "test"
level: "high"
logsource: "windows / appxdeployment-server"
aliases:
  - "8b48ad89-10d8-4382-a546-50588c410f0d"
  - "Remote AppX Package Downloaded from File Sharing or CDN Domain"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Remote AppX Package Downloaded from File Sharing or CDN Domain

Detects an appx package that was added to the pipeline of the "to be processed" packages which was downloaded from a file sharing or CDN domain.

## Metadata

- Rule ID: 8b48ad89-10d8-4382-a546-50588c410f0d
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-01-11
- Modified: 2025-12-10
- Source Path: rules/windows/builtin/appxdeployment_server/win_appxdeployment_server_appx_downloaded_from_file_sharing_domains.yml

## Logsource

- product: windows
- service: appxdeployment-server

## Detection

```yaml
selection:
  EventID: 854
  Path|contains:
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
condition: selection
```

## False Positives

- Unlikely, unless the organization uses file sharing or CDN services to distribute internal applications.

## References

- https://www.sentinelone.com/labs/inside-malicious-windows-apps-for-malware-deployment/
- https://learn.microsoft.com/en-us/windows/win32/appxpkg/troubleshooting
- https://news.sophos.com/en-us/2021/11/11/bazarloader-call-me-back-attack-abuses-windows-10-apps-mechanism/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/appxdeployment_server/win_appxdeployment_server_appx_downloaded_from_file_sharing_domains.yml)
