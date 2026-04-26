---
sigma_id: "df69cb1d-b891-4cd9-90c7-d617d90100ce"
title: "Suspicious FromBase64String Usage On Gzip Archive - Ps Script"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_frombase64string_archive.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_frombase64string_archive.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "medium"
logsource: "windows / ps_script"
aliases:
  - "df69cb1d-b891-4cd9-90c7-d617d90100ce"
  - "Suspicious FromBase64String Usage On Gzip Archive - Ps Script"
attack_technique_ids:
  - "T1132.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious FromBase64String Usage On Gzip Archive - Ps Script

Detects attempts of decoding a base64 Gzip archive in a PowerShell script. This technique is often used as a method to load malicious content into memory afterward.

## Metadata

- Rule ID: df69cb1d-b891-4cd9-90c7-d617d90100ce
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-12-23
- Source Path: rules/windows/powershell/powershell_script/posh_ps_frombase64string_archive.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1132-data_encoding|T1132.001]]

## Detection

```yaml
selection:
  ScriptBlockText|contains|all:
  - FromBase64String
  - MemoryStream
  - H4sI
condition: selection
```

## False Positives

- Legitimate administrative script

## References

- https://speakerdeck.com/heirhabarov/hunting-for-powershell-abuse?slide=43

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_frombase64string_archive.yml)
