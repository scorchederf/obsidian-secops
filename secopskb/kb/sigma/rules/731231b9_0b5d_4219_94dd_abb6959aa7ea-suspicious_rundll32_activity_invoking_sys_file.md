---
sigma_id: "731231b9-0b5d-4219-94dd-abb6959aa7ea"
title: "Suspicious Rundll32 Activity Invoking Sys File"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_rundll32_sys.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_rundll32_sys.yml"
build_date: "2026-04-26 15:01:52"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "731231b9-0b5d-4219-94dd-abb6959aa7ea"
  - "Suspicious Rundll32 Activity Invoking Sys File"
attack_technique_ids:
  - "T1218.011"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Suspicious Rundll32 Activity Invoking Sys File

Detects suspicious process related to rundll32 based on command line that includes a *.sys file as seen being used by UNC2452

## Metadata

- Rule ID: 731231b9-0b5d-4219-94dd-abb6959aa7ea
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2021-03-05
- Modified: 2022-10-09
- Source Path: rules/windows/process_creation/proc_creation_win_rundll32_sys.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.011]]

## Detection

```yaml
selection1:
  CommandLine|contains: rundll32.exe
selection2:
  CommandLine|contains:
  - .sys,
  - '.sys '
condition: all of selection*
```

## False Positives

- Unknown

## References

- https://www.microsoft.com/security/blog/2021/03/04/goldmax-goldfinder-sibot-analyzing-nobelium-malware/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_rundll32_sys.yml)
