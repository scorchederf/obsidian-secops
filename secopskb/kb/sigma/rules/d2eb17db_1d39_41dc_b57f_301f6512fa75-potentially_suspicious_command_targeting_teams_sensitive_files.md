---
sigma_id: "d2eb17db-1d39-41dc-b57f-301f6512fa75"
title: "Potentially Suspicious Command Targeting Teams Sensitive Files"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_teams_suspicious_command_line_cred_access.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_teams_suspicious_command_line_cred_access.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "d2eb17db-1d39-41dc-b57f-301f6512fa75"
  - "Potentially Suspicious Command Targeting Teams Sensitive Files"
attack_technique_ids:
  - "T1528"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potentially Suspicious Command Targeting Teams Sensitive Files

Detects a commandline containing references to the Microsoft Teams database or cookies files from a process other than Teams.
The database might contain authentication tokens and other sensitive information about the logged in accounts.

## Metadata

- Rule ID: d2eb17db-1d39-41dc-b57f-301f6512fa75
- Status: test
- Level: medium
- Author: @SerkinValery
- Date: 2022-09-16
- Modified: 2023-12-18
- Source Path: rules/windows/process_creation/proc_creation_win_teams_suspicious_command_line_cred_access.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1528-steal_application_access_token|T1528]]

## Detection

```yaml
selection:
  CommandLine|contains:
  - \Microsoft\Teams\Cookies
  - \Microsoft\Teams\Local Storage\leveldb
filter_main_legit_locations:
  Image|endswith: \Microsoft\Teams\current\Teams.exe
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://www.bleepingcomputer.com/news/security/microsoft-teams-stores-auth-tokens-as-cleartext-in-windows-linux-macs/
- https://www.vectra.ai/blogpost/undermining-microsoft-teams-security-by-mining-tokens

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_teams_suspicious_command_line_cred_access.yml)
