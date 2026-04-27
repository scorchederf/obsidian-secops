---
sigma_id: "b98d0db6-511d-45de-ad02-e82a98729620"
title: "Remotely Hosted HTA File Executed Via Mshta.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_mshta_http.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_mshta_http.yml"
build_date: "2026-04-27 19:13:55"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "b98d0db6-511d-45de-ad02-e82a98729620"
  - "Remotely Hosted HTA File Executed Via Mshta.EXE"
attack_technique_ids:
  - "T1218.005"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects execution of the "mshta" utility with an argument containing the "http" keyword, which could indicate that an attacker is executing a remotely hosted malicious hta file

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution#^t1218005-mshta|T1218.005: Mshta]]

## Detection

```yaml
selection_img:
- Image|endswith: \mshta.exe
- OriginalFileName: MSHTA.EXE
selection_cli:
  CommandLine|contains:
  - http://
  - https://
  - ftp://
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://www.trendmicro.com/en_us/research/22/e/avoslocker-ransomware-variant-abuses-driver-file-to-disable-anti-Virus-scans-log4shell.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_mshta_http.yml)
