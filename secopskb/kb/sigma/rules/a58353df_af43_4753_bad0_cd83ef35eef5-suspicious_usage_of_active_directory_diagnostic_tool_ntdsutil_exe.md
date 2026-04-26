---
sigma_id: "a58353df-af43-4753-bad0-cd83ef35eef5"
title: "Suspicious Usage Of Active Directory Diagnostic Tool (ntdsutil.exe)"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_ntdsutil_susp_usage.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_ntdsutil_susp_usage.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "a58353df-af43-4753-bad0-cd83ef35eef5"
  - "Suspicious Usage Of Active Directory Diagnostic Tool (ntdsutil.exe)"
attack_technique_ids:
  - "T1003.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Usage Of Active Directory Diagnostic Tool (ntdsutil.exe)

Detects execution of ntdsutil.exe to perform different actions such as restoring snapshots...etc.

## Metadata

- Rule ID: a58353df-af43-4753-bad0-cd83ef35eef5
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-09-14
- Source Path: rules/windows/process_creation/proc_creation_win_ntdsutil_susp_usage.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.003]]

## Detection

```yaml
selection_img:
- Image|endswith: \ntdsutil.exe
- OriginalFileName: ntdsutil.exe
selection_cli:
- CommandLine|contains|all:
  - snapshot
  - 'mount '
- CommandLine|contains|all:
  - ac
  - ' i'
  - ' ntds'
condition: all of selection_*
```

## False Positives

- Legitimate usage to restore snapshots
- Legitimate admin activity

## References

- https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/cc731620(v=ws.11)
- https://symantec-enterprise-blogs.security.com/blogs/threat-intelligence/espionage-asia-governments

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_ntdsutil_susp_usage.yml)
