---
sigma_id: "bdeeabc9-ff2a-4a51-be59-bb253aac7891"
title: "PUA - Wsudo Suspicious Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_pua_wsudo_susp_execution.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pua_wsudo_susp_execution.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "bdeeabc9-ff2a-4a51-be59-bb253aac7891"
  - "PUA - Wsudo Suspicious Execution"
attack_technique_ids:
  - "T1059"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# PUA - Wsudo Suspicious Execution

Detects usage of wsudo (Windows Sudo Utility). Which is a tool that let the user execute programs with different permissions (System, Trusted Installer, Administrator...etc)

## Metadata

- Rule ID: bdeeabc9-ff2a-4a51-be59-bb253aac7891
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-12-02
- Modified: 2023-02-14
- Source Path: rules/windows/process_creation/proc_creation_win_pua_wsudo_susp_execution.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059]]

## Detection

```yaml
selection_metadata:
- Image|endswith: \wsudo.exe
- OriginalFileName: wsudo.exe
- Description: Windows sudo utility
- ParentImage|endswith: \wsudo-bridge.exe
selection_cli:
  CommandLine|contains:
  - -u System
  - -uSystem
  - -u TrustedInstaller
  - -uTrustedInstaller
  - ' --ti '
condition: 1 of selection_*
```

## False Positives

- Unknown

## References

- https://github.com/M2Team/Privexec/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_pua_wsudo_susp_execution.yml)
