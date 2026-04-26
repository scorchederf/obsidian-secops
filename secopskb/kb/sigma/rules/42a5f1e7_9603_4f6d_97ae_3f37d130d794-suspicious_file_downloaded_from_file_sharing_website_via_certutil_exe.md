---
sigma_id: "42a5f1e7-9603-4f6d-97ae-3f37d130d794"
title: "Suspicious File Downloaded From File-Sharing Website Via Certutil.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_certutil_download_file_sharing_domains.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_certutil_download_file_sharing_domains.yml"
build_date: "2026-04-26 17:03:22"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "42a5f1e7-9603-4f6d-97ae-3f37d130d794"
  - "Suspicious File Downloaded From File-Sharing Website Via Certutil.EXE"
attack_technique_ids:
  - "T1027"
  - "T1105"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Suspicious File Downloaded From File-Sharing Website Via Certutil.EXE

Detects the execution of certutil with certain flags that allow the utility to download files from file-sharing websites.

## Metadata

- Rule ID: 42a5f1e7-9603-4f6d-97ae-3f37d130d794
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-02-15
- Modified: 2025-12-10
- Source Path: rules/windows/process_creation/proc_creation_win_certutil_download_file_sharing_domains.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1027-obfuscated_files_or_information|T1027]]
- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

## Detection

```yaml
selection_img:
- Image|endswith: \certutil.exe
- OriginalFileName: CertUtil.exe
selection_flags:
  CommandLine|contains:
  - 'urlcache '
  - 'verifyctl '
  - 'URL '
selection_http:
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

- Unknown

## References

- https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/certutil
- https://forensicitguy.github.io/agenttesla-vba-certutil-download/
- https://news.sophos.com/en-us/2021/04/13/compromised-exchange-server-hosting-cryptojacker-targeting-other-exchange-servers/
- https://twitter.com/egre55/status/1087685529016193025
- https://lolbas-project.github.io/lolbas/Binaries/Certutil/
- https://www.microsoft.com/en-us/security/blog/2024/01/17/new-ttps-observed-in-mint-sandstorm-campaign-targeting-high-profile-individuals-at-universities-and-research-orgs/
- https://www.hexacorn.com/blog/2020/08/23/certutil-one-more-gui-lolbin

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_certutil_download_file_sharing_domains.yml)
