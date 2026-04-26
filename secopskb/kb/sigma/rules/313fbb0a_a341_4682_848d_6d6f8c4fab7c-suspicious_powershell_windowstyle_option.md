---
sigma_id: "313fbb0a-a341-4682-848d-6d6f8c4fab7c"
title: "Suspicious PowerShell WindowStyle Option"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_susp_windowstyle.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_windowstyle.yml"
build_date: "2026-04-26 14:14:37"
status: "test"
level: "medium"
logsource: "windows / ps_script"
aliases:
  - "313fbb0a-a341-4682-848d-6d6f8c4fab7c"
  - "Suspicious PowerShell WindowStyle Option"
attack_technique_ids:
  - "T1564.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious PowerShell WindowStyle Option

Adversaries may use hidden windows to conceal malicious activity from the plain sight of users.
In some cases, windows that would typically be displayed when an application carries out an operation can be hidden

## Metadata

- Rule ID: 313fbb0a-a341-4682-848d-6d6f8c4fab7c
- Status: test
- Level: medium
- Author: frack113, Tim Shelton (fp AWS)
- Date: 2021-10-20
- Modified: 2023-01-03
- Source Path: rules/windows/powershell/powershell_script/posh_ps_susp_windowstyle.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1564-hide_artifacts|T1564.003]]

## Detection

```yaml
selection:
  ScriptBlockText|contains|all:
  - powershell
  - WindowStyle
  - Hidden
filter:
  ScriptBlockText|contains|all:
  - :\Program Files\Amazon\WorkSpacesConfig\Scripts\
  - $PSScriptRoot\Module\WorkspaceScriptModule\WorkspaceScriptModule
condition: selection and not filter
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1564.003/T1564.003.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_windowstyle.yml)
