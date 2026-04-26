---
sigma_id: "42333b2c-b425-441c-b70e-99404a17170f"
title: "HackTool - Sliver C2 Implant Activity Pattern"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_hktl_sliver_c2_execution_pattern.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_sliver_c2_execution_pattern.yml"
build_date: "2026-04-26 15:01:45"
status: "test"
level: "critical"
logsource: "windows / process_creation"
aliases:
  - "42333b2c-b425-441c-b70e-99404a17170f"
  - "HackTool - Sliver C2 Implant Activity Pattern"
attack_technique_ids:
  - "T1059"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# HackTool - Sliver C2 Implant Activity Pattern

Detects process activity patterns as seen being used by Sliver C2 framework implants

## Metadata

- Rule ID: 42333b2c-b425-441c-b70e-99404a17170f
- Status: test
- Level: critical
- Author: Nasreddine Bencherchali (Nextron Systems), Florian Roth (Nextron Systems)
- Date: 2022-08-25
- Modified: 2023-03-05
- Source Path: rules/windows/process_creation/proc_creation_win_hktl_sliver_c2_execution_pattern.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059]]

## Detection

```yaml
selection:
  CommandLine|contains: -NoExit -Command [Console]::OutputEncoding=[Text.UTF8Encoding]::UTF8
condition: selection
```

## False Positives

- Unlikely

## References

- https://github.com/BishopFox/sliver/blob/79f2d48fcdfc2bee4713b78d431ea4b27f733f30/implant/sliver/shell/shell_windows.go#L36
- https://www.microsoft.com/security/blog/2022/08/24/looking-for-the-sliver-lining-hunting-for-emerging-command-and-control-frameworks/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_hktl_sliver_c2_execution_pattern.yml)
