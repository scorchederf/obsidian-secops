---
sigma_id: "f38a82d2-fba3-4781-b549-525efbec8506"
title: "PUA - 3Proxy Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_pua_3proxy_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pua_3proxy_execution.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "f38a82d2-fba3-4781-b549-525efbec8506"
  - "PUA - 3Proxy Execution"
attack_technique_ids:
  - "T1572"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# PUA - 3Proxy Execution

Detects the use of 3proxy, a tiny free proxy server

## Metadata

- Rule ID: f38a82d2-fba3-4781-b549-525efbec8506
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2022-09-13
- Modified: 2023-02-21
- Source Path: rules/windows/process_creation/proc_creation_win_pua_3proxy_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1572-protocol_tunneling|T1572]]

## Detection

```yaml
selection_img:
  Image|endswith: \3proxy.exe
selection_pe:
  Description: 3proxy - tiny proxy server
selection_params:
  CommandLine|contains: .exe -i127.0.0.1 -p
condition: 1 of selection_*
```

## False Positives

- Administrative activity

## References

- https://github.com/3proxy/3proxy
- https://blog.talosintelligence.com/2022/09/lazarus-three-rats.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pua_3proxy_execution.yml)
