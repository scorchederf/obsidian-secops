---
sigma_id: "0afbd410-de03-4078-8491-f132303cb67d"
title: "Renamed NetSupport RAT Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_renamed_netsupport_rat.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_renamed_netsupport_rat.yml"
build_date: "2026-04-26 17:03:22"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "0afbd410-de03-4078-8491-f132303cb67d"
  - "Renamed NetSupport RAT Execution"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Renamed NetSupport RAT Execution

Detects the execution of a renamed "client32.exe" (NetSupport RAT) via Imphash, Product and OriginalFileName strings

## Metadata

- Rule ID: 0afbd410-de03-4078-8491-f132303cb67d
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-09-19
- Modified: 2024-11-23
- Source Path: rules/windows/process_creation/proc_creation_win_renamed_netsupport_rat.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection:
- Product|contains: NetSupport Remote Control
- OriginalFileName|contains: client32.exe
- Hashes|contains: IMPHASH=A9D50692E95B79723F3E76FCF70D023E
filter:
  Image|endswith: \client32.exe
condition: selection and not filter
```

## False Positives

- Unknown

## References

- https://redcanary.com/blog/misbehaving-rats/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_renamed_netsupport_rat.yml)
