---
sigma_id: "0afbd410-de03-4078-8491-f132303cb67d"
title: "Renamed NetSupport RAT Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_renamed_netsupport_rat.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_renamed_netsupport_rat.yml"
build_date: "2026-04-27 19:13:55"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the execution of a renamed "client32.exe" (NetSupport RAT) via Imphash, Product and OriginalFileName strings

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
