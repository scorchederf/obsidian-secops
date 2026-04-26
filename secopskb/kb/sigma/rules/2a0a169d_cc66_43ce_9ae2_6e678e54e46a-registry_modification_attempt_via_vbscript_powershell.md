---
sigma_id: "2a0a169d-cc66-43ce-9ae2-6e678e54e46a"
title: "Registry Modification Attempt Via VBScript - PowerShell"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_vbscript_registry_modification.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_vbscript_registry_modification.yml"
build_date: "2026-04-26 14:14:34"
status: "experimental"
level: "medium"
logsource: "windows / ps_script"
aliases:
  - "2a0a169d-cc66-43ce-9ae2-6e678e54e46a"
  - "Registry Modification Attempt Via VBScript - PowerShell"
attack_technique_ids:
  - "T1112"
  - "T1059.005"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Registry Modification Attempt Via VBScript - PowerShell

Detects attempts to modify the registry using VBScript's CreateObject("Wscript.shell") and RegWrite methods embedded within PowerShell scripts or commands.
Threat actors commonly embed VBScript code within PowerShell to perform registry modifications, attempting to evade detection that monitors for direct registry access through traditional tools.
This technique can be used for persistence, defense evasion, and privilege escalation by modifying registry keys without using regedit.exe, reg.exe, or PowerShell's native registry cmdlets.

## Metadata

- Rule ID: 2a0a169d-cc66-43ce-9ae2-6e678e54e46a
- Status: experimental
- Level: medium
- Author: Swachchhanda Shrawan Poudel (Nextron Systems)
- Date: 2025-08-13
- Source Path: rules/windows/powershell/powershell_script/posh_ps_vbscript_registry_modification.yml

## Logsource

- category: ps_script
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1112-modify_registry|T1112]]
- [[kb/attack/techniques/T1059-command_and_scripting_interpreter|T1059.005]]

## Detection

```yaml
selection:
  ScriptBlockText|contains|all:
  - CreateObject
  - Wscript.shell
  - .RegWrite
condition: selection
```

## False Positives

- Some legitimate admin or install scripts may use these processes for registry modifications.

## References

- https://www.linkedin.com/posts/mauricefielenbach_livingofftheland-redteam-persistence-activity-7344801774182051843-TE00/
- https://www.nextron-systems.com/2025/07/29/detecting-the-most-popular-mitre-persistence-method-registry-run-keys-startup-folder/
- https://detect.fyi/hunting-fileless-malware-in-the-windows-registry-1339ccde00ad

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_vbscript_registry_modification.yml)
