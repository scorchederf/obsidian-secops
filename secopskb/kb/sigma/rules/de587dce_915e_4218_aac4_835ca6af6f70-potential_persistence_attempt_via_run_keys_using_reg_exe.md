---
sigma_id: "de587dce-915e-4218-aac4-835ca6af6f70"
title: "Potential Persistence Attempt Via Run Keys Using Reg.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_reg_add_run_key.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_reg_add_run_key.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "de587dce-915e-4218-aac4-835ca6af6f70"
  - "Potential Persistence Attempt Via Run Keys Using Reg.EXE"
attack_technique_ids:
  - "T1547.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Persistence Attempt Via Run Keys Using Reg.EXE

Detects suspicious command line reg.exe tool adding key to RUN key in Registry

## Metadata

- Rule ID: de587dce-915e-4218-aac4-835ca6af6f70
- Status: test
- Level: medium
- Author: Florian Roth (Nextron Systems), Swachchhanda Shrawan Poudel (Nextron Systems)
- Date: 2021-06-28
- Modified: 2025-02-17
- Source Path: rules/windows/process_creation/proc_creation_win_reg_add_run_key.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547.001]]

## Detection

```yaml
selection:
  Image|endswith: \reg.exe
  CommandLine|contains|all:
  - reg
  - ' add '
  CommandLine|contains:
  - Software\Microsoft\Windows\CurrentVersion\Run
  - \Software\WOW6432Node\Microsoft\Windows\CurrentVersion\Run
  - \Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\Run
condition: selection
```

## False Positives

- Legitimate software automatically (mostly, during installation) sets up autorun keys for legitimate reasons.
- Legitimate administrator sets up autorun keys for legitimate reasons.
- Discord

## References

- https://app.any.run/tasks/9c0f37bc-867a-4314-b685-e101566766d7/
- https://learn.microsoft.com/en-us/windows/win32/setupapi/run-and-runonce-registry-keys
- https://github.com/HackTricks-wiki/hacktricks/blob/e4c7b21b8f36c97c35b7c622732b38a189ce18f7/src/windows-hardening/windows-local-privilege-escalation/privilege-escalation-with-autorun-binaries.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_reg_add_run_key.yml)
