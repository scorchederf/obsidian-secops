---
sigma_id: "01c42d3c-242d-4655-85b2-34f1739632f7"
title: "Potentially Over Permissive Permissions Granted Using Dsacls.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_dsacls_abuse_permissions.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_dsacls_abuse_permissions.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "01c42d3c-242d-4655-85b2-34f1739632f7"
  - "Potentially Over Permissive Permissions Granted Using Dsacls.EXE"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potentially Over Permissive Permissions Granted Using Dsacls.EXE

Detects usage of Dsacls to grant over permissive permissions

## Metadata

- Rule ID: 01c42d3c-242d-4655-85b2-34f1739632f7
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-06-20
- Modified: 2023-02-04
- Source Path: rules/windows/process_creation/proc_creation_win_dsacls_abuse_permissions.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection_img:
- Image|endswith: \dsacls.exe
- OriginalFileName: DSACLS.EXE
selection_flag:
  CommandLine|contains: ' /G '
selection_permissions:
  CommandLine|contains:
  - GR
  - GE
  - GW
  - GA
  - WP
  - WD
condition: all of selection_*
```

## False Positives

- Legitimate administrators granting over permissive permissions to users

## References

- https://ss64.com/nt/dsacls.html
- https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/cc771151(v=ws.11)

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_dsacls_abuse_permissions.yml)
