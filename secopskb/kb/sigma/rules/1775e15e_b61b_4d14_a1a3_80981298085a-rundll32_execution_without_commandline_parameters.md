---
sigma_id: "1775e15e-b61b-4d14-a1a3-80981298085a"
title: "Rundll32 Execution Without CommandLine Parameters"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_rundll32_no_params.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_rundll32_no_params.yml"
build_date: "2026-04-26 17:03:22"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "1775e15e-b61b-4d14-a1a3-80981298085a"
  - "Rundll32 Execution Without CommandLine Parameters"
attack_technique_ids:
  - "T1202"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Rundll32 Execution Without CommandLine Parameters

Detects suspicious start of rundll32.exe without any parameters as found in CobaltStrike beacon activity

## Metadata

- Rule ID: 1775e15e-b61b-4d14-a1a3-80981298085a
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2021-05-27
- Modified: 2023-08-31
- Source Path: rules/windows/process_creation/proc_creation_win_rundll32_no_params.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1202-indirect_command_execution|T1202]]

## Detection

```yaml
selection:
  CommandLine|endswith:
  - \rundll32.exe
  - \rundll32.exe"
  - \rundll32
filter:
  ParentImage|contains:
  - \AppData\Local\
  - \Microsoft\Edge\
condition: selection and not filter
```

## False Positives

- Possible but rare

## References

- https://www.cobaltstrike.com/help-opsec
- https://twitter.com/ber_m1ng/status/1397948048135778309

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_rundll32_no_params.yml)
