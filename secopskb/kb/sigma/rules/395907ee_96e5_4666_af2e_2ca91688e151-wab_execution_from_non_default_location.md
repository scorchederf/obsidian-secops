---
sigma_id: "395907ee-96e5-4666-af2e-2ca91688e151"
title: "Wab Execution From Non Default Location"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_wab_execution_from_non_default_location.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wab_execution_from_non_default_location.yml"
build_date: "2026-04-26 17:03:24"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "395907ee-96e5-4666-af2e-2ca91688e151"
  - "Wab Execution From Non Default Location"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Wab Execution From Non Default Location

Detects execution of wab.exe (Windows Contacts) and Wabmig.exe (Microsoft Address Book Import Tool) from non default locations as seen with bumblebee activity

## Metadata

- Rule ID: 395907ee-96e5-4666-af2e-2ca91688e151
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-08-12
- Modified: 2022-09-27
- Source Path: rules/windows/process_creation/proc_creation_win_wab_execution_from_non_default_location.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection:
  Image|endswith:
  - \wab.exe
  - \wabmig.exe
filter:
  Image|startswith:
  - C:\Windows\WinSxS\
  - C:\Program Files\Windows Mail\
  - C:\Program Files (x86)\Windows Mail\
condition: selection and not filter
```

## False Positives

- Unknown

## References

- https://thedfirreport.com/2022/08/08/bumblebee-roasts-its-way-to-domain-admin/
- https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/bumblebee-loader-cybercrime
- https://thedfirreport.com/2022/09/26/bumblebee-round-two/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_wab_execution_from_non_default_location.yml)
