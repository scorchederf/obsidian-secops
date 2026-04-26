---
sigma_id: "53330955-dc52-487f-a3a2-da24dcff99b5"
title: "New BgInfo.EXE Custom DB Path Registry Configuration"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_bginfo_custom_db.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_bginfo_custom_db.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "medium"
logsource: "windows / registry_set"
aliases:
  - "53330955-dc52-487f-a3a2-da24dcff99b5"
  - "New BgInfo.EXE Custom DB Path Registry Configuration"
attack_technique_ids:
  - "T1112"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# New BgInfo.EXE Custom DB Path Registry Configuration

Detects setting of a new registry database value related to BgInfo configuration. Attackers can for example set this value to save the results of the commands executed by BgInfo in order to exfiltrate information.

## Metadata

- Rule ID: 53330955-dc52-487f-a3a2-da24dcff99b5
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-08-16
- Source Path: rules/windows/registry/registry_set/registry_set_bginfo_custom_db.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1112-modify_registry|T1112]]

## Detection

```yaml
selection:
  TargetObject|endswith: \Software\Winternals\BGInfo\Database
condition: selection
```

## False Positives

- Legitimate use of external DB to save the results

## References

- Internal Research

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_bginfo_custom_db.yml)
