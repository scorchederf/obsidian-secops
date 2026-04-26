---
sigma_id: "98054878-5eab-434c-85d4-72d4e5a3361b"
title: "HackTool - EDRSilencer Execution - Filter Added"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_hktl_edr_silencer.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_hktl_edr_silencer.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "high"
logsource: "windows / security"
aliases:
  - "98054878-5eab-434c-85d4-72d4e5a3361b"
  - "HackTool - EDRSilencer Execution - Filter Added"
attack_technique_ids:
  - "T1562"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# HackTool - EDRSilencer Execution - Filter Added

Detects execution of EDRSilencer, a tool that abuses the Windows Filtering Platform (WFP) to block the outbound traffic of running EDR agents based on specific hardcoded filter names.

## Metadata

- Rule ID: 98054878-5eab-434c-85d4-72d4e5a3361b
- Status: test
- Level: high
- Author: Thodoris Polyzos (@SmoothDeploy)
- Date: 2024-01-29
- Modified: 2024-01-30
- Source Path: rules/windows/builtin/security/win_security_hktl_edr_silencer.yml

## Logsource

- definition: Requirements: Audit Filtering Platform Policy Change needs to be enabled
- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562]]

## Detection

```yaml
selection:
  EventID:
  - 5441
  - 5447
  FilterName|contains: Custom Outbound Filter
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/netero1010/EDRSilencer

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_hktl_edr_silencer.yml)
