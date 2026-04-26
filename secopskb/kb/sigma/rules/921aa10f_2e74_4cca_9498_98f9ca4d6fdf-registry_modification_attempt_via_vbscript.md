---
sigma_id: "921aa10f-2e74-4cca-9498-98f9ca4d6fdf"
title: "Registry Modification Attempt Via VBScript"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_vbscript_registry_modification.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_vbscript_registry_modification.yml"
build_date: "2026-04-26 14:14:34"
status: "experimental"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "921aa10f-2e74-4cca-9498-98f9ca4d6fdf"
  - "Registry Modification Attempt Via VBScript"
attack_technique_ids:
  - "T1112"
  - "T1059.005"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Registry Modification Attempt Via VBScript

Detects attempts to modify the registry using VBScript's CreateObject("Wscript.shell") and RegWrite methods via common LOLBINs.
It could be an attempt to modify the registry for persistence without using straightforward methods like regedit.exe, reg.exe, or PowerShell.
Threat Actors may use this technique to evade detection by security solutions that monitor for direct registry modifications through traditional tools.

## Metadata

- Rule ID: 921aa10f-2e74-4cca-9498-98f9ca4d6fdf
- Status: experimental
- Level: medium
- Author: Swachchhanda Shrawan Poudel (Nextron Systems)
- Date: 2025-08-13
- Source Path: rules/windows/process_creation/proc_creation_win_vbscript_registry_modification.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1112-modify_registry|T1112]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.005]]

## Detection

```yaml
selection:
  CommandLine|contains|all:
  - CreateObject
  - Wscript.shell
  - .RegWrite
condition: selection
```

## False Positives

- Unknown

## References

- https://www.linkedin.com/posts/mauricefielenbach_livingofftheland-redteam-persistence-activity-7344801774182051843-TE00/
- https://www.nextron-systems.com/2025/07/29/detecting-the-most-popular-mitre-persistence-method-registry-run-keys-startup-folder/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_vbscript_registry_modification.yml)
