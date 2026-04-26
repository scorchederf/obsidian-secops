---
sigma_id: "1d61f71d-59d2-479e-9562-4ff5f4ead16b"
title: "Suspicious Service Installation"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/system/service_control_manager/win_system_service_install_susp.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/service_control_manager/win_system_service_install_susp.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "high"
logsource: "windows / system"
aliases:
  - "1d61f71d-59d2-479e-9562-4ff5f4ead16b"
  - "Suspicious Service Installation"
attack_technique_ids:
  - "T1543.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Service Installation

Detects suspicious service installation commands

## Metadata

- Rule ID: 1d61f71d-59d2-479e-9562-4ff5f4ead16b
- Status: test
- Level: high
- Author: pH-T (Nextron Systems), Florian Roth (Nextron Systems)
- Date: 2022-03-18
- Modified: 2023-12-04
- Source Path: rules/windows/builtin/system/service_control_manager/win_system_service_install_susp.yml

## Logsource

- product: windows
- service: system

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1543-create_or_modify_system_process|T1543.003]]

## Detection

```yaml
selection:
  Provider_Name: Service Control Manager
  EventID: 7045
  ImagePath|contains:
  - ' -nop '
  - ' -sta '
  - ' -w hidden '
  - :\Temp\
  - .downloadfile(
  - .downloadstring(
  - \ADMIN$\
  - \Perflogs\
  - '&&'
condition: selection
```

## False Positives

- Unknown

## References

- Internal Research

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/service_control_manager/win_system_service_install_susp.yml)
