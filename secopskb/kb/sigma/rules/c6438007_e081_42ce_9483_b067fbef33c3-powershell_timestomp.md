---
sigma_id: "c6438007-e081-42ce-9483-b067fbef33c3"
title: "Powershell Timestomp"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_timestomp.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_timestomp.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "medium"
logsource: "windows / ps_script"
aliases:
  - "c6438007-e081-42ce-9483-b067fbef33c3"
  - "Powershell Timestomp"
attack_technique_ids:
  - "T1070.006"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Powershell Timestomp

Adversaries may modify file time attributes to hide new or changes to existing files.
Timestomping is a technique that modifies the timestamps of a file (the modify, access, create, and change times), often to mimic files that are in the same folder.

## Metadata

- Rule ID: c6438007-e081-42ce-9483-b067fbef33c3
- Status: test
- Level: medium
- Author: frack113
- Date: 2021-08-03
- Modified: 2022-12-25
- Source Path: rules/windows/powershell/powershell_script/posh_ps_timestomp.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1070-indicator_removal|T1070.006]]

## Detection

```yaml
selection_ioc:
  ScriptBlockText|contains:
  - .CreationTime =
  - .LastWriteTime =
  - .LastAccessTime =
  - '[IO.File]::SetCreationTime'
  - '[IO.File]::SetLastAccessTime'
  - '[IO.File]::SetLastWriteTime'
condition: selection_ioc
```

## False Positives

- Legitimate admin script

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1070.006/T1070.006.md
- https://www.offensive-security.com/metasploit-unleashed/timestomp/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_timestomp.yml)
