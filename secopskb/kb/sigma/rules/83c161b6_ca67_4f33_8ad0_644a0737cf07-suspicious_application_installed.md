---
sigma_id: "83c161b6-ca67-4f33-8ad0-644a0737cf07"
title: "Suspicious Application Installed"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/shell_core/win_shell_core_susp_packages_installed.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/shell_core/win_shell_core_susp_packages_installed.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "medium"
logsource: "windows / shell-core"
aliases:
  - "83c161b6-ca67-4f33-8ad0-644a0737cf07"
  - "Suspicious Application Installed"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Application Installed

Detects suspicious application installed by looking at the added shortcut to the app resolver cache

## Metadata

- Rule ID: 83c161b6-ca67-4f33-8ad0-644a0737cf07
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-08-14
- Source Path: rules/windows/builtin/shell_core/win_shell_core_susp_packages_installed.yml

## Logsource

- product: windows
- service: shell-core

## Detection

```yaml
selection_name:
  EventID: 28115
  Name|contains:
  - Zenmap
  - AnyDesk
  - wireshark
  - openvpn
selection_packageid:
  EventID: 28115
  AppID|contains:
  - zenmap.exe
  - prokzult ad
  - wireshark
  - openvpn
condition: 1 of selection_*
```

## False Positives

- Packages or applications being legitimately used by users or administrators

## References

- https://nasbench.medium.com/finding-forensic-goodness-in-obscure-windows-event-logs-60e978ea45a3

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/shell_core/win_shell_core_susp_packages_installed.yml)
