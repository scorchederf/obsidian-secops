---
sigma_id: "64d51a51-32a6-49f0-9f3d-17e34d640272"
title: "Ngrok Usage with Remote Desktop Service"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/terminalservices/win_terminalservices_rdp_ngrok.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/terminalservices/win_terminalservices_rdp_ngrok.yml"
build_date: "2026-04-26 17:03:20"
status: "test"
level: "high"
logsource: "windows / terminalservices-localsessionmanager"
aliases:
  - "64d51a51-32a6-49f0-9f3d-17e34d640272"
  - "Ngrok Usage with Remote Desktop Service"
attack_technique_ids:
  - "T1090"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Ngrok Usage with Remote Desktop Service

Detects cases in which ngrok, a reverse proxy tool, forwards events to the local RDP port, which could be a sign of malicious behaviour

## Metadata

- Rule ID: 64d51a51-32a6-49f0-9f3d-17e34d640272
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2022-04-29
- Source Path: rules/windows/builtin/terminalservices/win_terminalservices_rdp_ngrok.yml

## Logsource

- product: windows
- service: terminalservices-localsessionmanager

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1090-proxy|T1090]]

## Detection

```yaml
selection:
  EventID: 21
  Address|contains: '16777216'
condition: selection
```

## False Positives

- Unknown

## References

- https://twitter.com/tekdefense/status/1519711183162556416?s=12&t=OTsHCBkQOTNs1k3USz65Zg
- https://ngrok.com/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/terminalservices/win_terminalservices_rdp_ngrok.yml)
