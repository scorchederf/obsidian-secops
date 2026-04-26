---
sigma_id: "1b3b01c7-84e9-4072-86e5-fc285a41ff23"
title: "Nslookup PowerShell Download Cradle - ProcessCreation"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_nslookup_poweshell_download.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_nslookup_poweshell_download.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "1b3b01c7-84e9-4072-86e5-fc285a41ff23"
  - "Nslookup PowerShell Download Cradle - ProcessCreation"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Nslookup PowerShell Download Cradle - ProcessCreation

Detects suspicious powershell download cradle using nslookup. This cradle uses nslookup to extract payloads from DNS records

## Metadata

- Rule ID: 1b3b01c7-84e9-4072-86e5-fc285a41ff23
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-09-05
- Modified: 2022-12-19
- Source Path: rules/windows/process_creation/proc_creation_win_nslookup_poweshell_download.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection_img:
- Image|contains: \nslookup.exe
- OriginalFileName: \nslookup.exe
selection_cmd:
  ParentImage|endswith:
  - \powershell.exe
  - \pwsh.exe
  CommandLine|contains:
  - ' -q=txt '
  - ' -querytype=txt '
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://twitter.com/Alh4zr3d/status/1566489367232651264

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_nslookup_poweshell_download.yml)
