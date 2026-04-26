---
sigma_id: "e9f8f8cc-07cc-4e81-b724-f387db9175e4"
title: "Potentially Suspicious Execution Of Regasm/Regsvcs With Uncommon Extension"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_regasm_regsvcs_uncommon_extension_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_regasm_regsvcs_uncommon_extension_execution.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "e9f8f8cc-07cc-4e81-b724-f387db9175e4"
  - "Potentially Suspicious Execution Of Regasm/Regsvcs With Uncommon Extension"
attack_technique_ids:
  - "T1218.009"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potentially Suspicious Execution Of Regasm/Regsvcs With Uncommon Extension

Detects potentially suspicious execution of the Regasm/Regsvcs utilities with an uncommon extension.

## Metadata

- Rule ID: e9f8f8cc-07cc-4e81-b724-f387db9175e4
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-02-13
- Source Path: rules/windows/process_creation/proc_creation_win_regasm_regsvcs_uncommon_extension_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218.009]]

## Detection

```yaml
selection_img:
- Image|endswith:
  - \Regsvcs.exe
  - \Regasm.exe
- OriginalFileName:
  - RegSvcs.exe
  - RegAsm.exe
selection_extension:
  CommandLine|contains:
  - .dat
  - .gif
  - .jpeg
  - .jpg
  - .png
  - .txt
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://www.fortiguard.com/threat-signal-report/4718?s=09
- https://lolbas-project.github.io/lolbas/Binaries/Regasm/
- https://lolbas-project.github.io/lolbas/Binaries/Regsvcs/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_regasm_regsvcs_uncommon_extension_execution.yml)
