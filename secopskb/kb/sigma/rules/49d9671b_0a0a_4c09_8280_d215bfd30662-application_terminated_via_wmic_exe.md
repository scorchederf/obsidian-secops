---
sigma_id: "49d9671b-0a0a-4c09-8280-d215bfd30662"
title: "Application Terminated Via Wmic.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_wmic_terminate_application.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wmic_terminate_application.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "49d9671b-0a0a-4c09-8280-d215bfd30662"
  - "Application Terminated Via Wmic.EXE"
attack_technique_ids:
  - "T1047"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Application Terminated Via Wmic.EXE

Detects calls to the "terminate" function via wmic in order to kill an application

## Metadata

- Rule ID: 49d9671b-0a0a-4c09-8280-d215bfd30662
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-09-11
- Source Path: rules/windows/process_creation/proc_creation_win_wmic_terminate_application.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1047-windows_management_instrumentation|T1047]]

## Detection

```yaml
selection_img:
- Image|endswith: \WMIC.exe
- OriginalFileName: wmic.exe
selection_cli:
  CommandLine|contains|all:
  - call
  - terminate
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://cyble.com/blog/lockfile-ransomware-using-proxyshell-attack-to-deploy-ransomware/
- https://www.bitdefender.com/files/News/CaseStudies/study/377/Bitdefender-Whitepaper-WMI-creat4871-en-EN-GenericUse.pdf

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wmic_terminate_application.yml)
