---
sigma_id: "d635249d-86b5-4dad-a8c7-d7272b788586"
title: "BITS Transfer Job Download From File Sharing Domains"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/bits_client/win_bits_client_new_transfer_via_file_sharing_domains.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/bits_client/win_bits_client_new_transfer_via_file_sharing_domains.yml"
build_date: "2026-04-26 15:01:43"
status: "test"
level: "high"
logsource: "windows / bits-client"
aliases:
  - "d635249d-86b5-4dad-a8c7-d7272b788586"
  - "BITS Transfer Job Download From File Sharing Domains"
attack_technique_ids:
  - "T1197"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# BITS Transfer Job Download From File Sharing Domains

Detects BITS transfer job downloading files from a file sharing domain.

## Metadata

- Rule ID: d635249d-86b5-4dad-a8c7-d7272b788586
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2022-06-28
- Modified: 2025-12-10
- Source Path: rules/windows/builtin/bits_client/win_bits_client_new_transfer_via_file_sharing_domains.yml

## Logsource

- product: windows
- service: bits-client

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1197-bits_jobs|T1197]]

## Detection

```yaml
selection:
  EventID: 16403
  RemoteName|contains:
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
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1197/T1197.md
- https://twitter.com/malmoeb/status/1535142803075960832
- https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/ransomware-hive-conti-avoslocker
- https://www.microsoft.com/en-us/security/blog/2024/01/17/new-ttps-observed-in-mint-sandstorm-campaign-targeting-high-profile-individuals-at-universities-and-research-orgs/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/bits_client/win_bits_client_new_transfer_via_file_sharing_domains.yml)
