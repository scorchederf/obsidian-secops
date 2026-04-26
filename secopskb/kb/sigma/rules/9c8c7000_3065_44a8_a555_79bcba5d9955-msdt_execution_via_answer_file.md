---
sigma_id: "9c8c7000-3065-44a8-a555-79bcba5d9955"
title: "MSDT Execution Via Answer File"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_msdt_answer_file_exec.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_msdt_answer_file_exec.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "9c8c7000-3065-44a8-a555-79bcba5d9955"
  - "MSDT Execution Via Answer File"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# MSDT Execution Via Answer File

Detects execution of "msdt.exe" using an answer file which is simulating the legitimate way of calling msdt via "pcwrun.exe" (For example from the compatibility tab).

## Metadata

- Rule ID: 9c8c7000-3065-44a8-a555-79bcba5d9955
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-06-13
- Modified: 2025-10-29
- Source Path: rules/windows/process_creation/proc_creation_win_msdt_answer_file_exec.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection:
  Image|endswith: \msdt.exe
  CommandLine|contains: \WINDOWS\diagnostics\index\PCWDiagnostic.xml
  CommandLine|contains|windash: ' -af '
filter_main_pcwrun:
  ParentImage|endswith: \pcwrun.exe
condition: selection and not 1 of filter_main_*
```

## False Positives

- Possible undocumented parents of "msdt" other than "pcwrun".

## References

- https://lolbas-project.github.io/lolbas/Binaries/Msdt/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_msdt_answer_file_exec.yml)
