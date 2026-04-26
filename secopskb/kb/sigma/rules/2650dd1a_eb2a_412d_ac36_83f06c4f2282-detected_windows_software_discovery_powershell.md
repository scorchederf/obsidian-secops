---
sigma_id: "2650dd1a-eb2a-412d-ac36-83f06c4f2282"
title: "Detected Windows Software Discovery - PowerShell"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_software_discovery.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_software_discovery.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "medium"
logsource: "windows / ps_script"
aliases:
  - "2650dd1a-eb2a-412d-ac36-83f06c4f2282"
  - "Detected Windows Software Discovery - PowerShell"
attack_technique_ids:
  - "T1518"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Detected Windows Software Discovery - PowerShell

Adversaries may attempt to enumerate software for a variety of reasons, such as figuring out what security measures are present or if the compromised system has a version of software that is vulnerable.

## Metadata

- Rule ID: 2650dd1a-eb2a-412d-ac36-83f06c4f2282
- Status: test
- Level: medium
- Author: Nikita Nazarov, oscd.community
- Date: 2020-10-16
- Modified: 2022-12-02
- Source Path: rules/windows/powershell/powershell_script/posh_ps_software_discovery.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1518-software_discovery|T1518]]

## Detection

```yaml
selection:
  ScriptBlockText|contains|all:
  - get-itemProperty
  - \software\
  - select-object
  - format-table
condition: selection
```

## False Positives

- Legitimate administration activities

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1518/T1518.md
- https://github.com/harleyQu1nn/AggressorScripts

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_software_discovery.yml)
