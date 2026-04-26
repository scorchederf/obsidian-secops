---
sigma_id: "7b14c76a-c602-4ae6-9717-eff868153fc0"
title: "HackTool - NoFilter Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_hktl_nofilter.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_hktl_nofilter.yml"
build_date: "2026-04-26 14:14:26"
status: "test"
level: "high"
logsource: "windows / security"
aliases:
  - "7b14c76a-c602-4ae6-9717-eff868153fc0"
  - "HackTool - NoFilter Execution"
attack_technique_ids:
  - "T1134"
  - "T1134.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# HackTool - NoFilter Execution

Detects execution of NoFilter, a tool for abusing the Windows Filtering Platform for privilege escalation via hardcoded policy name indicators

## Metadata

- Rule ID: 7b14c76a-c602-4ae6-9717-eff868153fc0
- Status: test
- Level: high
- Author: Stamatis Chatzimangou (st0pp3r)
- Date: 2024-01-05
- Source Path: rules/windows/builtin/security/win_security_hktl_nofilter.yml

## Logsource

- definition: Requirements: Audit Filtering Platform Policy Change needs to be enabled
- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1134-access_token_manipulation|T1134]]
- [[kb/attack/techniques/T1134-access_token_manipulation|T1134.001]]

## Detection

```yaml
selection_5447:
  EventID: 5447
  FilterName|contains: RonPolicy
selection_5449:
  EventID: 5449
  ProviderContextName|contains: RonPolicy
condition: 1 of selection_*
```

## False Positives

- Unknown

## References

- https://github.com/deepinstinct/NoFilter/blob/121d215ab130c5e8e3ad45a7e7fcd56f4de97b4d/NoFilter/Consts.cpp
- https://github.com/deepinstinct/NoFilter
- https://www.deepinstinct.com/blog/nofilter-abusing-windows-filtering-platform-for-privilege-escalation
- https://x.com/_st0pp3r_/status/1742203752361128162?s=20

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_hktl_nofilter.yml)
