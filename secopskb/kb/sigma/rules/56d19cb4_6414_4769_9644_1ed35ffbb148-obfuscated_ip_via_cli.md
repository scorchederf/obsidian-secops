---
sigma_id: "56d19cb4-6414-4769-9644-1ed35ffbb148"
title: "Obfuscated IP Via CLI"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_obfuscated_ip_via_cli.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_obfuscated_ip_via_cli.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "56d19cb4-6414-4769-9644-1ed35ffbb148"
  - "Obfuscated IP Via CLI"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Obfuscated IP Via CLI

Detects usage of an encoded/obfuscated version of an IP address (hex, octal, etc.) via command line

## Metadata

- Rule ID: 56d19cb4-6414-4769-9644-1ed35ffbb148
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems), X__Junior (Nextron Systems)
- Date: 2022-08-03
- Modified: 2023-11-06
- Source Path: rules/windows/process_creation/proc_creation_win_susp_obfuscated_ip_via_cli.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection_img:
  Image|endswith:
  - \ping.exe
  - \arp.exe
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
condition: selection_img and 1 of selection_ip_* and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://h.43z.one/ipconverter/
- https://twitter.com/Yasser_Elsnbary/status/1553804135354564608

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_obfuscated_ip_via_cli.yml)
