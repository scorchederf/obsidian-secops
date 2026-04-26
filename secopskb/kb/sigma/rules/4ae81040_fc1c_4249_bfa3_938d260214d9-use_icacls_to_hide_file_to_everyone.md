---
sigma_id: "4ae81040-fc1c-4249-bfa3-938d260214d9"
title: "Use Icacls to Hide File to Everyone"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_icacls_deny.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_icacls_deny.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "4ae81040-fc1c-4249-bfa3-938d260214d9"
  - "Use Icacls to Hide File to Everyone"
attack_technique_ids:
  - "T1564.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Use Icacls to Hide File to Everyone

Detect use of icacls to deny access for everyone in Users folder sometimes used to hide malicious files

## Metadata

- Rule ID: 4ae81040-fc1c-4249-bfa3-938d260214d9
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-07-18
- Modified: 2024-04-29
- Source Path: rules/windows/process_creation/proc_creation_win_icacls_deny.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1564-hide_artifacts|T1564.001]]

## Detection

```yaml
selection_icacls:
- OriginalFileName: iCACLS.EXE
- Image|endswith: \icacls.exe
selection_cmd:
  CommandLine|contains|all:
  - /deny
  - '*S-1-1-0:'
condition: all of selection_*
```

## False Positives

- Unknown

## References

- https://app.any.run/tasks/1df999e6-1cb8-45e3-8b61-499d1b7d5a9b/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_icacls_deny.yml)
