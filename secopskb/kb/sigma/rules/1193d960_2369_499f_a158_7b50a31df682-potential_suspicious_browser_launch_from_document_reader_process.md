---
sigma_id: "1193d960-2369-499f-a158-7b50a31df682"
title: "Potential Suspicious Browser Launch From Document Reader Process"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_browser_launch_from_document_reader_process.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_browser_launch_from_document_reader_process.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "1193d960-2369-499f-a158-7b50a31df682"
  - "Potential Suspicious Browser Launch From Document Reader Process"
attack_technique_ids:
  - "T1204.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Suspicious Browser Launch From Document Reader Process

Detects when a browser process or browser tab is launched from an application that handles document files such as Adobe, Microsoft Office, etc. And connects to a web application over http(s), this could indicate a possible phishing attempt.

## Metadata

- Rule ID: 1193d960-2369-499f-a158-7b50a31df682
- Status: test
- Level: medium
- Author: Joseph Kamau
- Date: 2024-05-27
- Modified: 2025-10-07
- Source Path: rules/windows/process_creation/proc_creation_win_susp_browser_launch_from_document_reader_process.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1204-user_execution|T1204.002]]

## Detection

```yaml
selection:
  ParentImage|contains:
  - Acrobat Reader
  - Microsoft Office
  - PDF Reader
  Image|endswith:
  - \brave.exe
  - \chrome.exe
  - \firefox.exe
  - \msedge.exe
  - \opera.exe
  - \maxthon.exe
  - \seamonkey.exe
  - \vivaldi.exe
  CommandLine|contains: http
filter_main_microsoft_help:
  CommandLine|contains: https://go.microsoft.com/fwlink/
filter_optional_foxit:
  CommandLine|contains:
  - http://ad.foxitsoftware.com/adlog.php?
  - https://globe-map.foxitservice.com/go.php?do=redirect
condition: selection and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- Unlikely in most cases, further investigation should be done in the commandline of the browser process to determine the context of the URL accessed.

## References

- https://app.any.run/tasks/69c5abaa-92ad-45ba-8c53-c11e23e05d04/
- https://app.any.run/tasks/64043a79-165f-4052-bcba-e6e49f847ec1/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_browser_launch_from_document_reader_process.yml)
