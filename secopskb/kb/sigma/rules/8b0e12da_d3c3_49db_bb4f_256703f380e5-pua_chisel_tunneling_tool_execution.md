---
sigma_id: "8b0e12da-d3c3-49db-bb4f-256703f380e5"
title: "PUA - Chisel Tunneling Tool Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_pua_chisel.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pua_chisel.yml"
build_date: "2026-04-26 17:03:20"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "8b0e12da-d3c3-49db-bb4f-256703f380e5"
  - "PUA - Chisel Tunneling Tool Execution"
attack_technique_ids:
  - "T1090.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# PUA - Chisel Tunneling Tool Execution

Detects usage of the Chisel tunneling tool via the commandline arguments

## Metadata

- Rule ID: 8b0e12da-d3c3-49db-bb4f-256703f380e5
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2022-09-13
- Modified: 2023-02-13
- Source Path: rules/windows/process_creation/proc_creation_win_pua_chisel.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1090-proxy|T1090.001]]

## Detection

```yaml
selection_img:
  Image|endswith: \chisel.exe
selection_param1:
  CommandLine|contains:
  - 'exe client '
  - 'exe server '
selection_param2:
  CommandLine|contains:
  - -socks5
  - -reverse
  - ' r:'
  - ':127.0.0.1:'
  - '-tls-skip-verify '
  - :socks
condition: selection_img or all of selection_param*
```

## False Positives

- Some false positives may occur with other tools with similar commandlines

## References

- https://github.com/jpillora/chisel/
- https://arcticwolf.com/resources/blog/lorenz-ransomware-chiseling-in/
- https://blog.sekoia.io/lucky-mouse-incident-response-to-detection-engineering/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pua_chisel.yml)
