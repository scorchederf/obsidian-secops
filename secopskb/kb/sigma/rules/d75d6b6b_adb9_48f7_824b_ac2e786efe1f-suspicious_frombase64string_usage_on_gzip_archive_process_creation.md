---
sigma_id: "d75d6b6b-adb9-48f7-824b-ac2e786efe1f"
title: "Suspicious FromBase64String Usage On Gzip Archive - Process Creation"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_powershell_frombase64string_archive.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_frombase64string_archive.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "d75d6b6b-adb9-48f7-824b-ac2e786efe1f"
  - "Suspicious FromBase64String Usage On Gzip Archive - Process Creation"
attack_technique_ids:
  - "T1132.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious FromBase64String Usage On Gzip Archive - Process Creation

Detects attempts of decoding a base64 Gzip archive via PowerShell. This technique is often used as a method to load malicious content into memory afterward.

## Metadata

- Rule ID: d75d6b6b-adb9-48f7-824b-ac2e786efe1f
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-12-23
- Source Path: rules/windows/process_creation/proc_creation_win_powershell_frombase64string_archive.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1132-data_encoding|T1132.001]]

## Detection

```yaml
selection:
  CommandLine|contains|all:
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

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_powershell_frombase64string_archive.yml)
