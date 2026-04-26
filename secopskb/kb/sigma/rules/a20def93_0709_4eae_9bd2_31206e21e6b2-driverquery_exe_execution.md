---
sigma_id: "a20def93-0709-4eae-9bd2-31206e21e6b2"
title: "DriverQuery.EXE Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_driverquery_usage.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_driverquery_usage.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "a20def93-0709-4eae-9bd2-31206e21e6b2"
  - "DriverQuery.EXE Execution"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# DriverQuery.EXE Execution

Detect usage of the "driverquery" utility. Which can be used to perform reconnaissance on installed drivers

## Metadata

- Rule ID: a20def93-0709-4eae-9bd2-31206e21e6b2
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-01-19
- Modified: 2023-09-29
- Source Path: rules/windows/process_creation/proc_creation_win_driverquery_usage.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection:
- Image|endswith: driverquery.exe
- OriginalFileName: drvqry.exe
filter_main_other:
- ParentImage|endswith:
  - \cscript.exe
  - \mshta.exe
  - \regsvr32.exe
  - \rundll32.exe
  - \wscript.exe
- ParentImage|contains:
  - \AppData\Local\
  - \Users\Public\
  - \Windows\Temp\
condition: selection and not 1 of filter_main_*
```

## False Positives

- Legitimate use by third party tools in order to investigate installed drivers

## References

- https://thedfirreport.com/2023/01/09/unwrapping-ursnifs-gifts/
- https://www.vmray.com/cyber-security-blog/analyzing-ursnif-behavior-malware-sandbox/
- https://www.fireeye.com/blog/threat-research/2020/01/saigon-mysterious-ursnif-fork.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_driverquery_usage.yml)
