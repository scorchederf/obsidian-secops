---
sigma_id: "58f4ea09-0fc2-4520-ba18-b85c540b0eaf"
title: "Suspicious Serv-U Process Pattern"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_servu_susp_child_process.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_servu_susp_child_process.yml"
build_date: "2026-04-26 17:03:23"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "58f4ea09-0fc2-4520-ba18-b85c540b0eaf"
  - "Suspicious Serv-U Process Pattern"
attack_technique_ids:
  - "T1555"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Suspicious Serv-U Process Pattern

Detects a suspicious process pattern which could be a sign of an exploited Serv-U service

## Metadata

- Rule ID: 58f4ea09-0fc2-4520-ba18-b85c540b0eaf
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2021-07-14
- Modified: 2022-07-14
- Source Path: rules/windows/process_creation/proc_creation_win_servu_susp_child_process.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1555-credentials_from_password_stores|T1555]]

## Detection

```yaml
selection:
  ParentImage|endswith: \Serv-U.exe
  Image|endswith:
  - \cmd.exe
  - \powershell.exe
  - \pwsh.exe
  - \wscript.exe
  - \cscript.exe
  - \sh.exe
  - \bash.exe
  - \schtasks.exe
  - \regsvr32.exe
  - \wmic.exe
  - \mshta.exe
  - \rundll32.exe
  - \msiexec.exe
  - \forfiles.exe
  - \scriptrunner.exe
condition: selection
```

## False Positives

- Legitimate uses in which users or programs use the SSH service of Serv-U for remote command execution

## References

- https://www.microsoft.com/security/blog/2021/07/13/microsoft-discovers-threat-actor-targeting-solarwinds-serv-u-software-with-0-day-exploit/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_servu_susp_child_process.yml)
