---
sigma_id: "e31033fc-33f0-4020-9a16-faf9b31cbf08"
title: "PUA - Netcat Suspicious Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_pua_netcat.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pua_netcat.yml"
build_date: "2026-04-26 15:01:47"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "e31033fc-33f0-4020-9a16-faf9b31cbf08"
  - "PUA - Netcat Suspicious Execution"
attack_technique_ids:
  - "T1095"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# PUA - Netcat Suspicious Execution

Detects execution of Netcat. Adversaries may use a non-application layer protocol for communication between host and C2 server or among infected hosts within a network

## Metadata

- Rule ID: e31033fc-33f0-4020-9a16-faf9b31cbf08
- Status: test
- Level: high
- Author: frack113, Florian Roth (Nextron Systems)
- Date: 2021-07-21
- Modified: 2023-02-08
- Source Path: rules/windows/process_creation/proc_creation_win_pua_netcat.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1095-non-application_layer_protocol|T1095]]

## Detection

```yaml
selection_img:
  Image|endswith:
  - \nc.exe
  - \ncat.exe
  - \netcat.exe
selection_cmdline:
  CommandLine|contains:
  - ' -lvp '
  - ' -lvnp'
  - ' -l -v -p '
  - ' -lv -p '
  - ' -l --proxy-type http '
  - ' -vnl --exec '
  - ' -vnl -e '
  - ' --lua-exec '
  - ' --sh-exec '
condition: 1 of selection_*
```

## False Positives

- Legitimate ncat use

## References

- https://nmap.org/ncat/
- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1095/T1095.md
- https://www.revshells.com/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pua_netcat.yml)
