---
sigma_id: "2316929c-01aa-438c-970f-099145ab1ee6"
title: "JAMF MDM Potential Suspicious Child Process"
framework: "sigma"
generated: "true"
source_path: "rules/macos/process_creation/proc_creation_macos_jamf_susp_child.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_jamf_susp_child.yml"
build_date: "2026-04-26 14:14:28"
status: "test"
level: "medium"
logsource: "macos / process_creation"
aliases:
  - "2316929c-01aa-438c-970f-099145ab1ee6"
  - "JAMF MDM Potential Suspicious Child Process"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# JAMF MDM Potential Suspicious Child Process

Detects potential suspicious child processes of "jamf". Could be a sign of potential abuse of Jamf as a C2 server as seen by Typhon MythicAgent.

## Metadata

- Rule ID: 2316929c-01aa-438c-970f-099145ab1ee6
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-08-22
- Source Path: rules/macos/process_creation/proc_creation_macos_jamf_susp_child.yml

## Logsource

- category: process_creation
- product: macos

## Detection

```yaml
selection:
  ParentImage|endswith: /jamf
  Image|endswith:
  - /bash
  - /sh
condition: selection
```

## False Positives

- Legitimate execution of custom scripts or commands by Jamf administrators. Apply additional filters accordingly

## References

- https://github.com/MythicAgents/typhon/
- https://www.zoocoup.org/casper/jamf_cheatsheet.pdf
- https://docs.jamf.com/10.30.0/jamf-pro/administrator-guide/Components_Installed_on_Managed_Computers.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_jamf_susp_child.yml)
