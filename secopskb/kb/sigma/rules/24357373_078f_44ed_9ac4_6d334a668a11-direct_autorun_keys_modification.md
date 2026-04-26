---
sigma_id: "24357373-078f-44ed-9ac4-6d334a668a11"
title: "Direct Autorun Keys Modification"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_reg_direct_asep_registry_keys_modification.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_reg_direct_asep_registry_keys_modification.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "24357373-078f-44ed-9ac4-6d334a668a11"
  - "Direct Autorun Keys Modification"
attack_technique_ids:
  - "T1547.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Direct Autorun Keys Modification

Detects direct modification of autostart extensibility point (ASEP) in registry using reg.exe.

## Metadata

- Rule ID: 24357373-078f-44ed-9ac4-6d334a668a11
- Status: test
- Level: medium
- Author: Victor Sergeev, Daniil Yugoslavskiy, oscd.community, Swachchhanda Shrawan Poudel (Nextron Systems)
- Date: 2019-10-25
- Modified: 2026-01-05
- Source Path: rules/windows/process_creation/proc_creation_win_reg_direct_asep_registry_keys_modification.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1547-boot_or_logon_autostart_execution|T1547.001]]

## Detection

```yaml
selection_img:
- Image|endswith: \reg.exe
- OriginalFileName: reg.exe
selection_cli_add:
  CommandLine|contains: add
selection_cli_keys:
  CommandLine|contains:
  - \software\Microsoft\Windows\CurrentVersion\Run
  - \software\WOW6432Node\Microsoft\Windows\CurrentVersion\Run
  - \software\Microsoft\Windows\CurrentVersion\Policies\Explorer\Run
  - \software\Microsoft\Windows NT\CurrentVersion\Winlogon\Userinit
  - \software\Microsoft\Windows NT\CurrentVersion\Winlogon\Shell
  - \software\Microsoft\Windows NT\CurrentVersion\Windows
  - \system\CurrentControlSet\Control\SafeBoot\AlternateShell
condition: all of selection_*
```

## False Positives

- Legitimate software automatically (mostly, during installation) sets up autorun keys for legitimate reasons.
- Legitimate administrator sets up autorun keys for legitimate reasons.
- Discord

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1547.001/T1547.001.md
- https://github.com/HackTricks-wiki/hacktricks/blob/e4c7b21b8f36c97c35b7c622732b38a189ce18f7/src/windows-hardening/windows-local-privilege-escalation/privilege-escalation-with-autorun-binaries.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_reg_direct_asep_registry_keys_modification.yml)
