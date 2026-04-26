---
sigma_id: "1c563233-030e-4a07-af8c-ee0490a66d3a"
title: "Suspicious New-PSDrive to Admin Share"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_susp_new_psdrive.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_new_psdrive.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "medium"
logsource: "windows / ps_script"
aliases:
  - "1c563233-030e-4a07-af8c-ee0490a66d3a"
  - "Suspicious New-PSDrive to Admin Share"
attack_technique_ids:
  - "T1021.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious New-PSDrive to Admin Share

Adversaries may use to interact with a remote network share using Server Message Block (SMB). The adversary may then perform actions as the logged-on user.

## Metadata

- Rule ID: 1c563233-030e-4a07-af8c-ee0490a66d3a
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-08-13
- Source Path: rules/windows/powershell/powershell_script/posh_ps_susp_new_psdrive.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1021-remote_services|T1021.002]]

## Detection

```yaml
selection:
  ScriptBlockText|contains|all:
  - New-PSDrive
  - '-psprovider '
  - filesystem
  - '-root '
  - \\\\
  - $
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1021.002/T1021.002.md#atomic-test-2---map-admin-share-powershell
- https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/new-psdrive?view=powershell-7.2

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_susp_new_psdrive.yml)
