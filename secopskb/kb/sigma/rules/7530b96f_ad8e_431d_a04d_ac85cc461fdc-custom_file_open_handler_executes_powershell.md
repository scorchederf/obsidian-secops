---
sigma_id: "7530b96f-ad8e-431d-a04d-ac85cc461fdc"
title: "Custom File Open Handler Executes PowerShell"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_custom_file_open_handler_powershell_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_custom_file_open_handler_powershell_execution.yml"
build_date: "2026-04-27 19:13:51"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "7530b96f-ad8e-431d-a04d-ac85cc461fdc"
  - "Custom File Open Handler Executes PowerShell"
attack_technique_ids:
  - "T1202"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the abuse of custom file open handler, executing powershell

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1202-indirect_command_execution|T1202: Indirect Command Execution]]

## Detection

```yaml
selection:
  TargetObject|contains: shell\open\command\
  Details|contains|all:
  - powershell
  - -command
condition: selection
```

## False Positives

- Unknown

## References

- https://news.sophos.com/en-us/2022/02/01/solarmarker-campaign-used-novel-registry-changes-to-establish-persistence/?cmp=30728

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_custom_file_open_handler_powershell_execution.yml)
