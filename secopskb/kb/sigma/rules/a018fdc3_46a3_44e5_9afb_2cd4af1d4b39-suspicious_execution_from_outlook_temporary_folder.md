---
sigma_id: "a018fdc3-46a3-44e5-9afb-2cd4af1d4b39"
title: "Suspicious Execution From Outlook Temporary Folder"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_office_outlook_execution_from_temp.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_office_outlook_execution_from_temp.yml"
build_date: "2026-04-27 19:13:56"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "a018fdc3-46a3-44e5-9afb-2cd4af1d4b39"
  - "Suspicious Execution From Outlook Temporary Folder"
attack_technique_ids:
  - "T1566.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects a suspicious program execution in Outlook temp folder

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1566-phishing#^t1566001-spearphishing-attachment|T1566.001: Spearphishing Attachment]]

## Detection

```yaml
selection:
  Image|contains: \Temporary Internet Files\Content.Outlook\
condition: selection
```

## False Positives

- Unknown

## References

- Internal Research

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_office_outlook_execution_from_temp.yml)
