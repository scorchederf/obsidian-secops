---
sigma_id: "3b4e950b-a3ea-44d3-877e-432071990709"
title: "Notepad Password Files Discovery"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_notepad_local_passwd_discovery.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_notepad_local_passwd_discovery.yml"
build_date: "2026-04-26 14:14:30"
status: "experimental"
level: "low"
logsource: "windows / process_creation"
aliases:
  - "3b4e950b-a3ea-44d3-877e-432071990709"
  - "Notepad Password Files Discovery"
attack_technique_ids:
  - "T1083"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Notepad Password Files Discovery

Detects the execution of Notepad to open a file that has the string "password" which may indicate unauthorized access to credentials or suspicious activity.

## Metadata

- Rule ID: 3b4e950b-a3ea-44d3-877e-432071990709
- Status: experimental
- Level: low
- Author: The DFIR Report
- Date: 2025-02-21
- Source Path: rules/windows/process_creation/proc_creation_win_notepad_local_passwd_discovery.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1083-file_and_directory_discovery|T1083]]

## Detection

```yaml
selection:
  ParentImage|endswith: \explorer.exe
  Image|endswith: \notepad.exe
  CommandLine|endswith:
  - password*.txt
  - password*.csv
  - password*.doc
  - password*.xls
condition: selection
```

## False Positives

- Legitimate use of opening files from remote hosts by administrators or users. However, storing passwords in text readable format could potentially be a violation of the organization's policy. Any match should be investigated further.

## References

- https://thedfirreport.com/2025/02/24/confluence-exploit-leads-to-lockbit-ransomware/
- https://intel.thedfirreport.com/eventReports/view/57

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_notepad_local_passwd_discovery.yml)
