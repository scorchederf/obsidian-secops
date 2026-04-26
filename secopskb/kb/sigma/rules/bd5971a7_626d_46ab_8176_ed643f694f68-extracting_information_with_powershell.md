---
sigma_id: "bd5971a7-626d-46ab-8176-ed643f694f68"
title: "Extracting Information with PowerShell"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_susp_extracting.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_extracting.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "medium"
logsource: "windows / ps_script"
aliases:
  - "bd5971a7-626d-46ab-8176-ed643f694f68"
  - "Extracting Information with PowerShell"
attack_technique_ids:
  - "T1552.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Extracting Information with PowerShell

Adversaries may search local file systems and remote file shares for files containing insecurely stored credentials.
These can be files created by users to store their own credentials, shared credential stores for a group of individuals,
configuration files containing passwords for a system or service, or source code/binary files containing embedded passwords.

## Metadata

- Rule ID: bd5971a7-626d-46ab-8176-ed643f694f68
- Status: test
- Level: medium
- Author: frack113
- Date: 2021-12-19
- Modified: 2022-12-25
- Source Path: rules/windows/powershell/powershell_script/posh_ps_susp_extracting.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1552-unsecured_credentials|T1552.001]]

## Detection

```yaml
selection:
  ScriptBlockText|contains|all:
  - ls
  - ' -R'
  - 'select-string '
  - '-Pattern '
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1552.001/T1552.001.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_extracting.yml)
