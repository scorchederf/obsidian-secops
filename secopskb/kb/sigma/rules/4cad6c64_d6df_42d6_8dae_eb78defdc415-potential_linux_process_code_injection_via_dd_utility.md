---
sigma_id: "4cad6c64-d6df-42d6-8dae-eb78defdc415"
title: "Potential Linux Process Code Injection Via DD Utility"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_dd_process_injection.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_dd_process_injection.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "linux / process_creation"
aliases:
  - "4cad6c64-d6df-42d6-8dae-eb78defdc415"
  - "Potential Linux Process Code Injection Via DD Utility"
attack_technique_ids:
  - "T1055.009"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Linux Process Code Injection Via DD Utility

Detects the injection of code by overwriting the memory map of a Linux process using the "dd" Linux command.

## Metadata

- Rule ID: 4cad6c64-d6df-42d6-8dae-eb78defdc415
- Status: test
- Level: medium
- Author: Joseph Kamau
- Date: 2023-12-01
- Source Path: rules/linux/process_creation/proc_creation_lnx_dd_process_injection.yml

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1055-process_injection|T1055.009]]

## Detection

```yaml
selection:
  Image|endswith: /dd
  CommandLine|contains|all:
  - of=
  - /proc/
  - /mem
condition: selection
```

## False Positives

- Unknown

## References

- https://www.aon.com/cyber-solutions/aon_cyber_labs/linux-based-inter-process-code-injection-without-ptrace2/
- https://github.com/AonCyberLabs/Cexigua/blob/34d338620afae4c6335ba8d8d499e1d7d3d5d7b5/overwrite.sh

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_dd_process_injection.yml)
