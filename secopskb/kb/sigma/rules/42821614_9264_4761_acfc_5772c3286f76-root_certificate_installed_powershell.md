---
sigma_id: "42821614-9264-4761-acfc-5772c3286f76"
title: "Root Certificate Installed - PowerShell"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_root_certificate_installed.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_root_certificate_installed.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "medium"
logsource: "windows / ps_script"
aliases:
  - "42821614-9264-4761-acfc-5772c3286f76"
  - "Root Certificate Installed - PowerShell"
attack_technique_ids:
  - "T1553.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Root Certificate Installed - PowerShell

Adversaries may install a root certificate on a compromised system to avoid warnings when connecting to adversary controlled web servers.

## Metadata

- Rule ID: 42821614-9264-4761-acfc-5772c3286f76
- Status: test
- Level: medium
- Author: oscd.community, @redcanary, Zach Stanford @svch0st
- Date: 2020-10-10
- Modified: 2022-12-02
- Source Path: rules/windows/powershell/powershell_script/posh_ps_root_certificate_installed.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1553-subvert_trust_controls|T1553.004]]

## Detection

```yaml
selection1:
  ScriptBlockText|contains|all:
  - Move-Item
  - Cert:\LocalMachine\Root
selection2:
  ScriptBlockText|contains|all:
  - Import-Certificate
  - Cert:\LocalMachine\Root
condition: 1 of selection*
```

## False Positives

- Help Desk or IT may need to manually add a corporate Root CA on occasion. Need to test if GPO push doesn't trigger FP

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1553.004/T1553.004.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_root_certificate_installed.yml)
