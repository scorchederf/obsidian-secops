---
sigma_id: "2837e152-93c8-43d2-85ba-c3cd3c2ae614"
title: "Powershell Local Email Collection"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_susp_mail_acces.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_mail_acces.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "medium"
logsource: "windows / ps_script"
aliases:
  - "2837e152-93c8-43d2-85ba-c3cd3c2ae614"
  - "Powershell Local Email Collection"
attack_technique_ids:
  - "T1114.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Powershell Local Email Collection

Adversaries may target user email on local systems to collect sensitive information.
Files containing email data can be acquired from a users local system, such as Outlook storage or cache files.

## Metadata

- Rule ID: 2837e152-93c8-43d2-85ba-c3cd3c2ae614
- Status: test
- Level: medium
- Author: frack113
- Date: 2021-07-21
- Modified: 2022-12-25
- Source Path: rules/windows/powershell/powershell_script/posh_ps_susp_mail_acces.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1114-email_collection|T1114.001]]

## Detection

```yaml
selection:
  ScriptBlockText|contains:
  - Get-Inbox.ps1
  - Microsoft.Office.Interop.Outlook
  - Microsoft.Office.Interop.Outlook.olDefaultFolders
  - -comobject outlook.application
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1114.001/T1114.001.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_mail_acces.yml)
