---
sigma_id: "d7654f02-e04b-4934-9838-65c46f187ebc"
title: "PUA- IOX Tunneling Tool Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_pua_iox.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pua_iox.yml"
build_date: "2026-04-26 17:03:20"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "d7654f02-e04b-4934-9838-65c46f187ebc"
  - "PUA- IOX Tunneling Tool Execution"
attack_technique_ids:
  - "T1090"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# PUA- IOX Tunneling Tool Execution

Detects the use of IOX - a tool for port forwarding and intranet proxy purposes

## Metadata

- Rule ID: d7654f02-e04b-4934-9838-65c46f187ebc
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2022-10-08
- Modified: 2024-11-23
- Source Path: rules/windows/process_creation/proc_creation_win_pua_iox.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1090-proxy|T1090]]

## Detection

```yaml
selection:
  Image|endswith: \iox.exe
selection_commandline:
  CommandLine|contains:
  - '.exe fwd -l '
  - '.exe fwd -r '
  - '.exe proxy -l '
  - '.exe proxy -r '
selection_hashes:
  Hashes|contains:
  - MD5=9DB2D314DD3F704A02051EF5EA210993
  - SHA1=039130337E28A6623ECF9A0A3DA7D92C5964D8DD
  - SHA256=C6CF82919B809967D9D90EA73772A8AA1C1EB3BC59252D977500F64F1A0D6731
condition: 1 of selection*
```

## False Positives

- Legitimate use

## References

- https://github.com/EddieIvan01/iox

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pua_iox.yml)
