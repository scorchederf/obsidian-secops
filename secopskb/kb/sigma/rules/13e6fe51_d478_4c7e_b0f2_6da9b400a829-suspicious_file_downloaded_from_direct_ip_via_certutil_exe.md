---
sigma_id: "13e6fe51-d478-4c7e-b0f2-6da9b400a829"
title: "Suspicious File Downloaded From Direct IP Via Certutil.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_certutil_download_direct_ip.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_certutil_download_direct_ip.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "13e6fe51-d478-4c7e-b0f2-6da9b400a829"
  - "Suspicious File Downloaded From Direct IP Via Certutil.EXE"
attack_technique_ids:
  - "T1027"
  - "T1105"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious File Downloaded From Direct IP Via Certutil.EXE

Detects the execution of certutil with certain flags that allow the utility to download files from direct IPs.

## Metadata

- Rule ID: 13e6fe51-d478-4c7e-b0f2-6da9b400a829
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-02-15
- Modified: 2025-12-01
- Source Path: rules/windows/process_creation/proc_creation_win_certutil_download_direct_ip.yml

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
  - ://1
  - ://2
  - ://3
  - ://4
  - ://5
  - ://6
  - ://7
  - ://8
  - ://9
filter_main_seven_zip:
  CommandLine|contains: ://7-
condition: all of selection_* and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/certutil
- https://forensicitguy.github.io/agenttesla-vba-certutil-download/
- https://news.sophos.com/en-us/2021/04/13/compromised-exchange-server-hosting-cryptojacker-targeting-other-exchange-servers/
- https://twitter.com/egre55/status/1087685529016193025
- https://lolbas-project.github.io/lolbas/Binaries/Certutil/
- https://twitter.com/_JohnHammond/status/1708910264261980634
- https://www.hexacorn.com/blog/2020/08/23/certutil-one-more-gui-lolbin

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_certutil_download_direct_ip.yml)
