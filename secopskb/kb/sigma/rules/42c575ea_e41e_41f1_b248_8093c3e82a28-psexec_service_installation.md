---
sigma_id: "42c575ea-e41e-41f1-b248-8093c3e82a28"
title: "PsExec Service Installation"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/system/service_control_manager/win_system_service_install_sysinternals_psexec.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/service_control_manager/win_system_service_install_sysinternals_psexec.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "medium"
logsource: "windows / system"
aliases:
  - "42c575ea-e41e-41f1-b248-8093c3e82a28"
  - "PsExec Service Installation"
attack_technique_ids:
  - "T1569.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# PsExec Service Installation

Detects PsExec service installation and execution events

## Metadata

- Rule ID: 42c575ea-e41e-41f1-b248-8093c3e82a28
- Status: test
- Level: medium
- Author: Thomas Patzke
- Date: 2017-06-12
- Modified: 2023-08-04
- Source Path: rules/windows/builtin/system/service_control_manager/win_system_service_install_sysinternals_psexec.yml

## Logsource

- product: windows
- service: system

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1569-system_services|T1569.002]]

### Software Tags

- S0029

## Detection

```yaml
selection_eid:
  Provider_Name: Service Control Manager
  EventID: 7045
selection_service:
- ServiceName: PSEXESVC
- ImagePath|endswith: \PSEXESVC.exe
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://www.jpcert.or.jp/english/pub/sr/ir_research.html
- https://jpcertcc.github.io/ToolAnalysisResultSheet

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/service_control_manager/win_system_service_install_sysinternals_psexec.yml)
