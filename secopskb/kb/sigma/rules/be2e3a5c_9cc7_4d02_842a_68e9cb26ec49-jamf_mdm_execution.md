---
sigma_id: "be2e3a5c-9cc7-4d02-842a-68e9cb26ec49"
title: "JAMF MDM Execution"
framework: "sigma"
generated: "true"
source_path: "rules/macos/process_creation/proc_creation_macos_jamf_usage.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_jamf_usage.yml"
build_date: "2026-04-26 14:14:28"
status: "test"
level: "low"
logsource: "macos / process_creation"
aliases:
  - "be2e3a5c-9cc7-4d02-842a-68e9cb26ec49"
  - "JAMF MDM Execution"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# JAMF MDM Execution

Detects execution of the "jamf" binary to create user accounts and run commands. For example, the binary can be abused by attackers on the system in order to bypass security controls or remove application control polices.

## Metadata

- Rule ID: be2e3a5c-9cc7-4d02-842a-68e9cb26ec49
- Status: test
- Level: low
- Author: Jay Pandit
- Date: 2023-08-22
- Source Path: rules/macos/process_creation/proc_creation_macos_jamf_usage.yml

## Logsource

- category: process_creation
- product: macos

## Detection

```yaml
selection:
  Image|endswith: /jamf
  CommandLine|contains:
  - createAccount
  - manage
  - removeFramework
  - removeMdmProfile
  - resetPassword
  - setComputerName
condition: selection
```

## False Positives

- Legitimate use of the JAMF CLI tool by IT support and administrators

## References

- https://github.com/MythicAgents/typhon/
- https://www.zoocoup.org/casper/jamf_cheatsheet.pdf
- https://docs.jamf.com/10.30.0/jamf-pro/administrator-guide/Components_Installed_on_Managed_Computers.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/macos/process_creation/proc_creation_macos_jamf_usage.yml)
