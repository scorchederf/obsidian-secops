---
sigma_id: "3b2c1059-ae5f-40b6-b5d4-6106d3ac20fe"
title: "Hidden Flag Set On File/Directory Via Chflags - MacOS"
framework: "sigma"
generated: "true"
source_path: "rules/macos/process_creation/proc_creation_macos_chflags_hidden_flag.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_chflags_hidden_flag.yml"
build_date: "2026-04-26 14:14:27"
status: "test"
level: "medium"
logsource: "macos / process_creation"
aliases:
  - "3b2c1059-ae5f-40b6-b5d4-6106d3ac20fe"
  - "Hidden Flag Set On File/Directory Via Chflags - MacOS"
attack_technique_ids:
  - "T1218"
  - "T1564.004"
  - "T1552.001"
  - "T1105"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Hidden Flag Set On File/Directory Via Chflags - MacOS

Detects the execution of the "chflags" utility with the "hidden" flag, in order to hide files on MacOS.
When a file or directory has this hidden flag set, it becomes invisible to the default file listing commands and in graphical file browsers.

## Metadata

- Rule ID: 3b2c1059-ae5f-40b6-b5d4-6106d3ac20fe
- Status: test
- Level: medium
- Author: Omar Khaled (@beacon_exe)
- Date: 2024-08-21
- Source Path: rules/macos/process_creation/proc_creation_macos_chflags_hidden_flag.yml

## Logsource

- category: process_creation
- product: macos

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]
- [[kb/attack/techniques/T1564-hide_artifacts|T1564.004]]
- [[kb/attack/techniques/T1552-unsecured_credentials|T1552.001]]
- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]

## Detection

```yaml
selection:
  Image|endswith: /chflags
  CommandLine|contains: 'hidden '
condition: selection
```

## False Positives

- Legitimate usage of chflags by administrators and users.

## References

- https://www.sentinelone.com/labs/apt32-multi-stage-macos-trojan-innovates-on-crimeware-scripting-technique/
- https://www.welivesecurity.com/2019/04/09/oceanlotus-macos-malware-update/
- https://www.paloaltonetworks.com/content/dam/pan/en_US/assets/pdf/reports/Unit_42/unit42-wirelurker.pdf
- https://ss64.com/mac/chflags.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_chflags_hidden_flag.yml)
