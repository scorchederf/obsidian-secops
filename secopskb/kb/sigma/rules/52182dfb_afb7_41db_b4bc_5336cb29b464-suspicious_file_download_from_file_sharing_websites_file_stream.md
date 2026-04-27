---
sigma_id: "52182dfb-afb7-41db-b4bc-5336cb29b464"
title: "Suspicious File Download From File Sharing Websites -  File Stream"
framework: "sigma"
generated: "true"
source_path: "rules/windows/create_stream_hash/create_stream_hash_file_sharing_domains_download_susp_extension.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/create_stream_hash/create_stream_hash_file_sharing_domains_download_susp_extension.yml"
build_date: "2026-04-27 19:13:56"
status: "test"
level: "high"
logsource: "windows / create_stream_hash"
aliases:
  - "52182dfb-afb7-41db-b4bc-5336cb29b464"
  - "Suspicious File Download From File Sharing Websites -  File Stream"
attack_technique_ids:
  - "T1564.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the download of suspicious file type from a well-known file and paste sharing domain

## Logsource

- category: create_stream_hash
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1564-hide_artifacts#^t1564004-ntfs-file-attributes|T1564.004: NTFS File Attributes]]

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
  - .cpl:Zone
  - .dll:Zone
  - .exe:Zone
  - .hta:Zone
  - .lnk:Zone
  - .one:Zone
  - .vbe:Zone
  - .vbs:Zone
  - .xll:Zone
condition: all of selection_*
```

## False Positives

- Some false positives might occur with binaries download via Github

## References

- https://www.ultimatewindowssecurity.com/securitylog/encyclopedia/event.aspx?eventid=90015
- https://www.cisa.gov/uscert/ncas/alerts/aa22-321a
- https://fabian-voith.de/2020/06/25/sysmon-v11-1-reads-alternate-data-streams/
- https://www.microsoft.com/en-us/security/blog/2024/01/17/new-ttps-observed-in-mint-sandstorm-campaign-targeting-high-profile-individuals-at-universities-and-research-orgs/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/create_stream_hash/create_stream_hash_file_sharing_domains_download_susp_extension.yml)
