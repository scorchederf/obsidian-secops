---
sigma_id: "c1dda054-d638-4c16-afc8-53e007f3fbc5"
title: "Automated Collection Command PowerShell"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_automated_collection.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_automated_collection.yml"
build_date: "2026-04-26 14:14:20"
status: "test"
level: "medium"
logsource: "windows / ps_script"
aliases:
  - "c1dda054-d638-4c16-afc8-53e007f3fbc5"
  - "Automated Collection Command PowerShell"
attack_technique_ids:
  - "T1119"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Automated Collection Command PowerShell

Once established within a system or network, an adversary may use automated techniques for collecting internal data.

## Metadata

- Rule ID: c1dda054-d638-4c16-afc8-53e007f3fbc5
- Status: test
- Level: medium
- Author: frack113
- Date: 2021-07-28
- Modified: 2022-12-25
- Source Path: rules/windows/powershell/powershell_script/posh_ps_automated_collection.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1119-automated_collection|T1119]]

## Detection

```yaml
selection_ext:
  ScriptBlockText|contains:
  - .doc
  - .docx
  - .xls
  - .xlsx
  - .ppt
  - .pptx
  - .rtf
  - .pdf
  - .txt
selection_cmd:
  ScriptBlockText|contains|all:
  - Get-ChildItem
  - ' -Recurse '
  - ' -Include '
condition: all of selection*
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1119/T1119.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_automated_collection.yml)
