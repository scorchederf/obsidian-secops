---
sigma_id: "7280c9f3-a5af-45d0-916a-bc01cb4151c9"
title: "Suspicious MSExchangeMailboxReplication ASPX Write"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_susp_exchange_aspx_write.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_susp_exchange_aspx_write.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "high"
logsource: "windows / file_event"
aliases:
  - "7280c9f3-a5af-45d0-916a-bc01cb4151c9"
  - "Suspicious MSExchangeMailboxReplication ASPX Write"
attack_technique_ids:
  - "T1190"
  - "T1505.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious MSExchangeMailboxReplication ASPX Write

Detects suspicious activity in which the MSExchangeMailboxReplication process writes .asp and .apsx files to disk, which could be a sign of ProxyShell exploitation

## Metadata

- Rule ID: 7280c9f3-a5af-45d0-916a-bc01cb4151c9
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2022-02-25
- Source Path: rules/windows/file/file_event/file_event_win_susp_exchange_aspx_write.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1190-exploit_public-facing_application|T1190]]
- [[kb/attack/techniques/T1505-server_software_component|T1505.003]]

## Detection

```yaml
selection:
  Image|endswith: \MSExchangeMailboxReplication.exe
  TargetFilename|endswith:
  - .aspx
  - .asp
condition: selection
```

## False Positives

- Unknown

## References

- https://redcanary.com/blog/blackbyte-ransomware/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_susp_exchange_aspx_write.yml)
