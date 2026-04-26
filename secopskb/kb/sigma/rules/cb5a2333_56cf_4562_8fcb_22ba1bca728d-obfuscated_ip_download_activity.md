---
sigma_id: "cb5a2333-56cf-4562-8fcb-22ba1bca728d"
title: "Obfuscated IP Download Activity"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_obfuscated_ip_download.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_obfuscated_ip_download.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "cb5a2333-56cf-4562-8fcb-22ba1bca728d"
  - "Obfuscated IP Download Activity"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Obfuscated IP Download Activity

Detects use of an encoded/obfuscated version of an IP address (hex, octal...) in an URL combined with a download command

## Metadata

- Rule ID: cb5a2333-56cf-4562-8fcb-22ba1bca728d
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems), X__Junior (Nextron Systems)
- Date: 2022-08-03
- Modified: 2025-07-18
- Source Path: rules/windows/process_creation/proc_creation_win_susp_obfuscated_ip_download.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection_command:
  CommandLine|contains:
  - Invoke-WebRequest
  - 'iwr '
  - Invoke-RestMethod
  - 'irm '
  - 'wget '
  - 'curl '
  - DownloadFile
  - DownloadString
selection_ip_1:
  CommandLine|contains:
  - ' 0x'
  - //0x
  - .0x
  - .00x
selection_ip_2:
  CommandLine|contains|all:
  - http://%
  - '%2e'
selection_ip_3:
- CommandLine|re: https?://[0-9]{1,3}\.[0-9]{1,3}\.0[0-9]{3,4}
- CommandLine|re: https?://[0-9]{1,3}\.0[0-9]{3,7}
- CommandLine|re: https?://0[0-9]{3,11}
- CommandLine|re: https?://(0[0-9]{1,11}\.){3}0[0-9]{1,11}
- CommandLine|re: https?://0[0-9]{1,11}
- CommandLine|re: ' [0-7]{7,13}'
filter_main_valid_ip:
  CommandLine|re: https?://((25[0-5]|(2[0-4]|1\d|[1-9])?\d)(\.|\b)){4}
condition: selection_command and 1 of selection_ip_* and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://h.43z.one/ipconverter/
- https://twitter.com/Yasser_Elsnbary/status/1553804135354564608
- https://twitter.com/fr0s7_/status/1712780207105404948

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_obfuscated_ip_download.yml)
