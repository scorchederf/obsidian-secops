---
sigma_id: "965e2db9-eddb-4cf6-a986-7a967df651e4"
title: "Potential Keylogger Activity"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_susp_keylogger_activity.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_keylogger_activity.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "windows / ps_script"
aliases:
  - "965e2db9-eddb-4cf6-a986-7a967df651e4"
  - "Potential Keylogger Activity"
attack_technique_ids:
  - "T1056.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Keylogger Activity

Detects PowerShell scripts that contains reference to keystroke capturing functions

## Metadata

- Rule ID: 965e2db9-eddb-4cf6-a986-7a967df651e4
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-01-04
- Source Path: rules/windows/powershell/powershell_script/posh_ps_susp_keylogger_activity.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1056-input_capture|T1056.001]]

## Detection

```yaml
selection:
  ScriptBlockText|contains: '[Windows.Input.Keyboard]::IsKeyDown([System.Windows.Input.Key]::'
condition: selection
```

## False Positives

- Unknown

## References

- https://twitter.com/ScumBots/status/1610626724257046529
- https://www.virustotal.com/gui/file/d4486b63512755316625230e0c9c81655093be93876e0d80732e7eeaf7d83476/content
- https://www.virustotal.com/gui/file/720a7ee9f2178c70501d7e3f4bcc28a4f456e200486dbd401b25af6da3b4da62/content
- https://learn.microsoft.com/en-us/dotnet/api/system.windows.input.keyboard.iskeydown?view=windowsdesktop-7.0

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_keylogger_activity.yml)
