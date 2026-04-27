---
sigma_id: "4c0aaedc-154c-4427-ada0-d80ef9c9deb6"
title: "Process Access via TrolleyExpress Exclusion"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_citrix_trolleyexpress_procdump.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_citrix_trolleyexpress_procdump.yml"
build_date: "2026-04-26 17:03:21"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "4c0aaedc-154c-4427-ada0-d80ef9c9deb6"
  - "Process Access via TrolleyExpress Exclusion"
attack_technique_ids:
  - "T1218.011"
  - "T1003.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Process Access via TrolleyExpress Exclusion

Detects a possible process memory dump that uses the white-listed Citrix TrolleyExpress.exe filename as a way to dump the lsass process memory

## Metadata

- Rule ID: 4c0aaedc-154c-4427-ada0-d80ef9c9deb6
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2022-02-10
- Modified: 2022-05-13
- Source Path: rules/windows/process_creation/proc_creation_win_citrix_trolleyexpress_procdump.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.011]]
- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.001]]

## Detection

```yaml
selection:
  CommandLine|contains:
  - \TrolleyExpress 7
  - \TrolleyExpress 8
  - \TrolleyExpress 9
  - \TrolleyExpress.exe 7
  - \TrolleyExpress.exe 8
  - \TrolleyExpress.exe 9
  - '\TrolleyExpress.exe -ma '
renamed:
  Image|endswith: \TrolleyExpress.exe
filter_renamed:
  OriginalFileName|contains: CtxInstall
filter_empty:
  OriginalFileName: null
condition: selection or ( renamed and not 1 of filter* )
```

## False Positives

- Unknown

## References

- https://twitter.com/_xpn_/status/1491557187168178176
- https://www.youtube.com/watch?v=Ie831jF0bb0

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_citrix_trolleyexpress_procdump.yml)
