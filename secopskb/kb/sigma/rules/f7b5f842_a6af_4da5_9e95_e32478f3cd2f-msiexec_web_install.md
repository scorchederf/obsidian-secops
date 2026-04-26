---
sigma_id: "f7b5f842-a6af-4da5-9e95-e32478f3cd2f"
title: "MsiExec Web Install"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_msiexec_web_install.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_msiexec_web_install.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "f7b5f842-a6af-4da5-9e95-e32478f3cd2f"
  - "MsiExec Web Install"
attack_technique_ids:
  - "T1218.007"
  - "T1105"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# MsiExec Web Install

Detects suspicious msiexec process starts with web addresses as parameter

## Metadata

- Rule ID: f7b5f842-a6af-4da5-9e95-e32478f3cd2f
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems)
- Date: 2018-02-09
- Modified: 2022-01-07
- Source Path: rules/windows/process_creation/proc_creation_win_msiexec_web_install.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.007]]
- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

## Detection

```yaml
selection:
  CommandLine|contains|all:
  - ' msiexec'
  - ://
condition: selection
```

## False Positives

- False positives depend on scripts and administrative tools used in the monitored environment

## References

- https://blog.trendmicro.com/trendlabs-security-intelligence/attack-using-windows-installer-msiexec-exe-leads-lokibot/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_msiexec_web_install.yml)
