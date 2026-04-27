---
sigma_id: "cc268ac1-42d9-40fd-9ed3-8c4e1a5b87e6"
title: "Devtoolslauncher.exe Executes Specified Binary"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_lolbin_devtoolslauncher.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_devtoolslauncher.yml"
build_date: "2026-04-27 19:13:51"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "cc268ac1-42d9-40fd-9ed3-8c4e1a5b87e6"
  - "Devtoolslauncher.exe Executes Specified Binary"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

The Devtoolslauncher.exe executes other binary

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218: System Binary Proxy Execution]]

## Detection

```yaml
selection:
  Image|endswith: \devtoolslauncher.exe
  CommandLine|contains: LaunchForDeploy
condition: selection
```

## False Positives

- Legitimate use of devtoolslauncher.exe by legitimate user

## References

- https://lolbas-project.github.io/lolbas/OtherMSBinaries/Devtoolslauncher/
- https://twitter.com/_felamos/status/1179811992841797632

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_devtoolslauncher.yml)
