---
sigma_id: "47e4bab7-c626-47dc-967b-255608c9a920"
title: "Permission Misconfiguration Reconnaissance Via Findstr.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_findstr_recon_everyone.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_findstr_recon_everyone.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "47e4bab7-c626-47dc-967b-255608c9a920"
  - "Permission Misconfiguration Reconnaissance Via Findstr.EXE"
attack_technique_ids:
  - "T1552.006"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Permission Misconfiguration Reconnaissance Via Findstr.EXE

Detects usage of findstr with the "EVERYONE" or "BUILTIN" keywords.
This was seen being used in combination with "icacls" and other utilities to spot misconfigured files or folders permissions.

## Metadata

- Rule ID: 47e4bab7-c626-47dc-967b-255608c9a920
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-08-12
- Modified: 2023-11-11
- Source Path: rules/windows/process_creation/proc_creation_win_findstr_recon_everyone.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1552-unsecured_credentials|T1552.006]]

## Detection

```yaml
selection_findstr_img:
- Image|endswith:
  - \find.exe
  - \findstr.exe
- OriginalFileName:
  - FIND.EXE
  - FINDSTR.EXE
selection_findstr_cli:
  CommandLine|contains:
  - '"Everyone"'
  - '''Everyone'''
  - '"BUILTIN\\"'
  - '''BUILTIN\'''
selection_special:
  CommandLine|contains|all:
  - 'icacls '
  - 'findstr '
  - Everyone
condition: all of selection_findstr_* or selection_special
```

## False Positives

- Unknown

## References

- https://www.absolomb.com/2018-01-26-Windows-Privilege-Escalation-Guide/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_findstr_recon_everyone.yml)
