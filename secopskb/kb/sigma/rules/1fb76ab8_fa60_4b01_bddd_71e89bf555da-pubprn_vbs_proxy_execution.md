---
sigma_id: "1fb76ab8-fa60-4b01-bddd-71e89bf555da"
title: "Pubprn.vbs Proxy Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_lolbin_pubprn.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_pubprn.yml"
build_date: "2026-04-26 14:14:34"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "1fb76ab8-fa60-4b01-bddd-71e89bf555da"
  - "Pubprn.vbs Proxy Execution"
attack_technique_ids:
  - "T1216.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Pubprn.vbs Proxy Execution

Detects the use of the 'Pubprn.vbs' Microsoft signed script to execute commands.

## Metadata

- Rule ID: 1fb76ab8-fa60-4b01-bddd-71e89bf555da
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-05-28
- Source Path: rules/windows/process_creation/proc_creation_win_lolbin_pubprn.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1216-system_script_proxy_execution|T1216.001]]

## Detection

```yaml
selection:
  CommandLine|contains|all:
  - \pubprn.vbs
  - 'script:'
condition: selection
```

## False Positives

- Unknown

## References

- https://lolbas-project.github.io/lolbas/Scripts/Pubprn/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_pubprn.yml)
