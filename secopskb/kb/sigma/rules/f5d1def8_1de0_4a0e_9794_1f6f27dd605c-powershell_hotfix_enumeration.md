---
sigma_id: "f5d1def8-1de0-4a0e-9794-1f6f27dd605c"
title: "PowerShell Hotfix Enumeration"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_hotfix_enum.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_hotfix_enum.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "medium"
logsource: "windows / ps_script"
aliases:
  - "f5d1def8-1de0-4a0e-9794-1f6f27dd605c"
  - "PowerShell Hotfix Enumeration"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# PowerShell Hotfix Enumeration

Detects call to "Win32_QuickFixEngineering" in order to enumerate installed hotfixes often used in "enum" scripts by attackers

## Metadata

- Rule ID: f5d1def8-1de0-4a0e-9794-1f6f27dd605c
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-06-21
- Source Path: rules/windows/powershell/powershell_script/posh_ps_hotfix_enum.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## Detection

```yaml
selection:
  ScriptBlockText|contains|all:
  - Win32_QuickFixEngineering
  - HotFixID
condition: selection
```

## False Positives

- Legitimate administration scripts

## References

- https://github.com/411Hall/JAWS/blob/233f142fcb1488172aa74228a666f6b3c5c48f1d/jaws-enum.ps1

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_hotfix_enum.yml)
