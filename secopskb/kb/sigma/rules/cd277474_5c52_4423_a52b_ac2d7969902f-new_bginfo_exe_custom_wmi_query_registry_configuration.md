---
sigma_id: "cd277474-5c52-4423-a52b-ac2d7969902f"
title: "New BgInfo.EXE Custom WMI Query Registry Configuration"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_bginfo_custom_wmi_query.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_bginfo_custom_wmi_query.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "medium"
logsource: "windows / registry_set"
aliases:
  - "cd277474-5c52-4423-a52b-ac2d7969902f"
  - "New BgInfo.EXE Custom WMI Query Registry Configuration"
attack_technique_ids:
  - "T1112"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# New BgInfo.EXE Custom WMI Query Registry Configuration

Detects setting of a new registry value related to BgInfo configuration, which can be abused to execute custom WMI query via "BgInfo.exe"

## Metadata

- Rule ID: cd277474-5c52-4423-a52b-ac2d7969902f
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-08-16
- Source Path: rules/windows/registry/registry_set/registry_set_bginfo_custom_wmi_query.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1112-modify_registry|T1112]]

## Detection

```yaml
selection:
  TargetObject|contains: \Software\Winternals\BGInfo\UserFields\
  Details|startswith: '6'
condition: selection
```

## False Positives

- Legitimate WMI query

## References

- Internal Research

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_bginfo_custom_wmi_query.yml)
