---
sigma_id: "b236190c-1c61-41e9-84b3-3fe03f6d76b0"
title: "Potential Regsvr32 Commandline Flag Anomaly"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_regsvr32_flags_anomaly.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_regsvr32_flags_anomaly.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "b236190c-1c61-41e9-84b3-3fe03f6d76b0"
  - "Potential Regsvr32 Commandline Flag Anomaly"
attack_technique_ids:
  - "T1218.010"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Regsvr32 Commandline Flag Anomaly

Detects a potential command line flag anomaly related to "regsvr32" in which the "/i" flag is used without the "/n" which should be uncommon.

## Metadata

- Rule ID: b236190c-1c61-41e9-84b3-3fe03f6d76b0
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems)
- Date: 2019-07-13
- Modified: 2024-03-13
- Source Path: rules/windows/process_creation/proc_creation_win_regsvr32_flags_anomaly.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.010]]

## Detection

```yaml
selection:
  Image|endswith: \regsvr32.exe
  CommandLine|contains|windash: ' -i:'
filter_main_flag:
  CommandLine|contains|windash: ' -n '
condition: selection and not 1 of filter_main_*
```

## False Positives

- Administrator typo might cause some false positives

## References

- https://twitter.com/sbousseaden/status/1282441816986484737?s=12

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_regsvr32_flags_anomaly.yml)
