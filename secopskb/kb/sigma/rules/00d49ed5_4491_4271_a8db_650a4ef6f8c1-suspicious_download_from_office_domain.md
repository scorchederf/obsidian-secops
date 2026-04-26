---
sigma_id: "00d49ed5-4491-4271-a8db-650a4ef6f8c1"
title: "Suspicious Download from Office Domain"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_download_office_domain.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_download_office_domain.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "00d49ed5-4491-4271-a8db-650a4ef6f8c1"
  - "Suspicious Download from Office Domain"
attack_technique_ids:
  - "T1105"
  - "T1608"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Download from Office Domain

Detects suspicious ways to download files from Microsoft domains that are used to store attachments in Emails or OneNote documents

## Metadata

- Rule ID: 00d49ed5-4491-4271-a8db-650a4ef6f8c1
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems), Nasreddine Bencherchali (Nextron Systems)
- Date: 2021-12-27
- Modified: 2022-08-02
- Source Path: rules/windows/process_creation/proc_creation_win_susp_download_office_domain.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]
- [[kb/attack/techniques/T1608-stage_capabilities|T1608]]

## Detection

```yaml
selection_download:
- Image|endswith:
  - \curl.exe
  - \wget.exe
- CommandLine|contains:
  - Invoke-WebRequest
  - 'iwr '
  - 'curl '
  - 'wget '
  - Start-BitsTransfer
  - .DownloadFile(
  - .DownloadString(
selection_domains:
  CommandLine|contains:
  - https://attachment.outlook.live.net/owa/
  - https://onenoteonlinesync.onenote.com/onenoteonlinesync/
condition: all of selection_*
```

## False Positives

- Scripts or tools that download attachments from these domains (OneNote, Outlook 365)

## References

- https://twitter.com/an0n_r0/status/1474698356635193346?s=12
- https://twitter.com/mrd0x/status/1475085452784844803?s=12

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_download_office_domain.yml)
