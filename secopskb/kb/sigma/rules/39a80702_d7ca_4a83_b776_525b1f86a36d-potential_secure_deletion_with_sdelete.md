---
sigma_id: "39a80702-d7ca-4a83-b776-525b1f86a36d"
title: "Potential Secure Deletion with SDelete"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/security/win_security_sdelete_potential_secure_deletion.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_sdelete_potential_secure_deletion.yml"
build_date: "2026-04-26 14:14:32"
status: "test"
level: "medium"
logsource: "windows / security"
aliases:
  - "39a80702-d7ca-4a83-b776-525b1f86a36d"
  - "Potential Secure Deletion with SDelete"
attack_technique_ids:
  - "T1070.004"
  - "T1027.005"
  - "T1485"
  - "T1553.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential Secure Deletion with SDelete

Detects files that have extensions commonly seen while SDelete is used to wipe files.

## Metadata

- Rule ID: 39a80702-d7ca-4a83-b776-525b1f86a36d
- Status: test
- Level: medium
- Author: Thomas Patzke
- Date: 2017-06-14
- Modified: 2024-12-13
- Source Path: rules/windows/builtin/security/win_security_sdelete_potential_secure_deletion.yml

## Logsource

- product: windows
- service: security

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1070-indicator_removal|T1070.004]]
- [[kb/attack/techniques/T1027-obfuscated_files_or_information|T1027.005]]
- [[kb/attack/techniques/T1485-data_destruction|T1485]]
- [[kb/attack/techniques/T1553-subvert_trust_controls|T1553.002]]

### Software Tags

- S0195

## Detection

```yaml
selection:
  EventID:
  - 4656
  - 4663
  - 4658
  ObjectName|endswith:
  - .AAA
  - .ZZZ
condition: selection
```

## False Positives

- Legitimate usage of SDelete
- Files that are interacted with that have these extensions legitimately

## References

- https://jpcertcc.github.io/ToolAnalysisResultSheet/details/sdelete.htm
- https://www.jpcert.or.jp/english/pub/sr/ir_research.html
- https://learn.microsoft.com/en-gb/sysinternals/downloads/sdelete

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/security/win_security_sdelete_potential_secure_deletion.yml)
