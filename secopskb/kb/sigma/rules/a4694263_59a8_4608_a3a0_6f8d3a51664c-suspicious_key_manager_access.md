---
sigma_id: "a4694263-59a8-4608-a3a0-6f8d3a51664c"
title: "Suspicious Key Manager Access"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_rundll32_keymgr.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_rundll32_keymgr.yml"
build_date: "2026-04-26 15:01:52"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "a4694263-59a8-4608-a3a0-6f8d3a51664c"
  - "Suspicious Key Manager Access"
attack_technique_ids:
  - "T1555.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Suspicious Key Manager Access

Detects the invocation of the Stored User Names and Passwords dialogue (Key Manager)

## Metadata

- Rule ID: a4694263-59a8-4608-a3a0-6f8d3a51664c
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2022-04-21
- Modified: 2023-02-09
- Source Path: rules/windows/process_creation/proc_creation_win_rundll32_keymgr.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1555-credentials_from_password_stores|T1555.004]]

## Detection

```yaml
selection_img:
- Image|endswith: \rundll32.exe
- OriginalFileName: RUNDLL32.EXE
selection_cli:
  CommandLine|contains|all:
  - keymgr
  - KRShowKeyMgr
condition: all of selection_*
```

## False Positives

- Administrative activity

## References

- https://twitter.com/NinjaParanoid/status/1516442028963659777

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_rundll32_keymgr.yml)
