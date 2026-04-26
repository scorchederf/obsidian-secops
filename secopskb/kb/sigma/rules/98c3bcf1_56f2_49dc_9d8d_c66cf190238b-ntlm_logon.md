---
sigma_id: "98c3bcf1-56f2-49dc-9d8d-c66cf190238b"
title: "NTLM Logon"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/ntlm/win_susp_ntlm_auth.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/ntlm/win_susp_ntlm_auth.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "low"
logsource: "windows / ntlm"
aliases:
  - "98c3bcf1-56f2-49dc-9d8d-c66cf190238b"
  - "NTLM Logon"
attack_technique_ids:
  - "T1550.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# NTLM Logon

Detects logons using NTLM, which could be caused by a legacy source or attackers

## Metadata

- Rule ID: 98c3bcf1-56f2-49dc-9d8d-c66cf190238b
- Status: test
- Level: low
- Author: Florian Roth (Nextron Systems)
- Date: 2018-06-08
- Modified: 2024-07-22
- Source Path: rules/windows/builtin/ntlm/win_susp_ntlm_auth.yml

## Logsource

- definition: Requires events from Microsoft-Windows-NTLM/Operational
- product: windows
- service: ntlm

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1550-use_alternate_authentication_material|T1550.002]]

## Detection

```yaml
selection:
  EventID: 8002
condition: selection
```

## False Positives

- Legacy hosts

## References

- https://twitter.com/JohnLaTwC/status/1004895028995477505

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/ntlm/win_susp_ntlm_auth.yml)
