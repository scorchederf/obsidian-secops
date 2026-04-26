---
sigma_id: "7b434893-c57d-4f41-908d-6a17bf1ae98f"
title: "Network Connection Initiated From Process Located In Potentially Suspicious Or Uncommon Location"
framework: "sigma"
generated: "true"
source_path: "rules/windows/network_connection/net_connection_win_susp_initiated_uncommon_or_suspicious_locations.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_susp_initiated_uncommon_or_suspicious_locations.yml"
build_date: "2026-04-26 15:01:47"
status: "test"
level: "high"
logsource: "windows / network_connection"
aliases:
  - "7b434893-c57d-4f41-908d-6a17bf1ae98f"
  - "Network Connection Initiated From Process Located In Potentially Suspicious Or Uncommon Location"
attack_technique_ids:
  - "T1105"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Network Connection Initiated From Process Located In Potentially Suspicious Or Uncommon Location

Detects a network connection initiated by programs or processes running from suspicious or uncommon files system locations.

## Metadata

- Rule ID: 7b434893-c57d-4f41-908d-6a17bf1ae98f
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems), Nasreddine Bencherchali (Nextron Systems)
- Date: 2017-03-19
- Modified: 2025-12-10
- Source Path: rules/windows/network_connection/net_connection_win_susp_initiated_uncommon_or_suspicious_locations.yml

## Logsource

- category: network_connection
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

## Detection

```yaml
selection:
  Initiated: 'true'
  Image|contains:
  - :\$Recycle.bin
  - :\Perflogs\
  - :\Temp\
  - :\Users\Default\
  - :\Users\Public\
  - :\Windows\Fonts\
  - :\Windows\IME\
  - :\Windows\System32\Tasks\
  - :\Windows\Tasks\
  - \config\systemprofile\
  - \Contacts\
  - \Favorites\
  - \Favourites\
  - \Music\
  - \Pictures\
  - \Videos\
  - \Windows\addins\
filter_main_domains:
  DestinationHostname|endswith:
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
  - mega.co.nz
  - mega.nz
  - onrender.com
  - pages.dev
  - paste.ee
  - pastebin.com
  - pastebin.pl
  - pastetext.net
  - portmap.io
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
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://docs.google.com/spreadsheets/d/17pSTDNpa0sf6pHeRhusvWG6rThciE8CsXTSlDUAZDyo

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_susp_initiated_uncommon_or_suspicious_locations.yml)
