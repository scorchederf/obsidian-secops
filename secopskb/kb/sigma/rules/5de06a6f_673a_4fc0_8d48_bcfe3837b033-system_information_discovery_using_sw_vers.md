---
sigma_id: "5de06a6f-673a-4fc0-8d48-bcfe3837b033"
title: "System Information Discovery Using sw_vers"
framework: "sigma"
generated: "true"
source_path: "rules/macos/process_creation/proc_creation_macos_swvers_discovery.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_swvers_discovery.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "medium"
logsource: "macos / process_creation"
aliases:
  - "5de06a6f-673a-4fc0-8d48-bcfe3837b033"
  - "System Information Discovery Using sw_vers"
attack_technique_ids:
  - "T1082"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# System Information Discovery Using sw_vers

Detects the use of "sw_vers" for system information discovery

## Metadata

- Rule ID: 5de06a6f-673a-4fc0-8d48-bcfe3837b033
- Status: test
- Level: medium
- Author: Joseliyo Sanchez, @Joseliyo_Jstnk
- Date: 2023-12-20
- Source Path: rules/macos/process_creation/proc_creation_macos_swvers_discovery.yml

## Logsource

- category: process_creation
- product: macos

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1082-system_information_discovery|T1082]]

## Detection

```yaml
selection_image:
  Image|endswith: /sw_vers
selection_options:
  CommandLine|contains:
  - -buildVersion
  - -productName
  - -productVersion
condition: all of selection_*
```

## False Positives

- Legitimate administrative activities

## References

- https://www.virustotal.com/gui/file/d3fa64f63563fe958b75238742d1e473800cb5f49f5cb79d38d4aa3c93709026/behavior
- https://www.virustotal.com/gui/file/03b71eaceadea05bc0eea5cddecaa05f245126d6b16cfcd0f3ba0442ac58dab3/behavior
- https://ss64.com/osx/sw_vers.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_swvers_discovery.yml)
