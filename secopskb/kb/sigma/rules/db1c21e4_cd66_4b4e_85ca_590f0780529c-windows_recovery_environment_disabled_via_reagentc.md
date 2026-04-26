---
sigma_id: "db1c21e4-cd66-4b4e-85ca-590f0780529c"
title: "Windows Recovery Environment Disabled Via Reagentc"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_reagentc_disable_windows_recovery_environment.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_reagentc_disable_windows_recovery_environment.yml"
build_date: "2026-04-26 14:14:40"
status: "experimental"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "db1c21e4-cd66-4b4e-85ca-590f0780529c"
  - "Windows Recovery Environment Disabled Via Reagentc"
attack_technique_ids:
  - "T1490"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Windows Recovery Environment Disabled Via Reagentc

Detects attempts to disable windows recovery environment using Reagentc.
ReAgentc.exe is a command-line tool in Windows used to manage the Windows Recovery Environment (WinRE).
It allows users to enable, disable, and configure WinRE, which is used for troubleshooting and repairing common boot issues.

## Metadata

- Rule ID: db1c21e4-cd66-4b4e-85ca-590f0780529c
- Status: experimental
- Level: medium
- Author: Daniel Koifman (KoifSec), Michael Vilshin
- Date: 2025-07-31
- Source Path: rules/windows/process_creation/proc_creation_win_reagentc_disable_windows_recovery_environment.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1490-inhibit_system_recovery|T1490]]

## Detection

```yaml
selection_img:
- Image|endswith: \reagentc.exe
- OriginalFileName: reagentc.exe
selection_cli:
  CommandLine|contains|windash: /disable
condition: all of selection_*
```

## False Positives

- Legitimate administrative activity

## References

- https://www.elastic.co/security-labs/maas-appeal-an-infostealer-rises-from-the-ashes
- https://learn.microsoft.com/en-us/windows-hardware/manufacture/desktop/reagentc-command-line-options?view=windows-11

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_reagentc_disable_windows_recovery_environment.yml)
