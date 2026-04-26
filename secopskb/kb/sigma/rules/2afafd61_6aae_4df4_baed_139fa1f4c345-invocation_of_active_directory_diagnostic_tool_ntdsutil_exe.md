---
sigma_id: "2afafd61-6aae-4df4-baed-139fa1f4c345"
title: "Invocation of Active Directory Diagnostic Tool (ntdsutil.exe)"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_ntdsutil_usage.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_ntdsutil_usage.yml"
build_date: "2026-04-26 14:14:27"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "2afafd61-6aae-4df4-baed-139fa1f4c345"
  - "Invocation of Active Directory Diagnostic Tool (ntdsutil.exe)"
attack_technique_ids:
  - "T1003.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Invocation of Active Directory Diagnostic Tool (ntdsutil.exe)

Detects execution of ntdsutil.exe, which can be used for various attacks against the NTDS database (NTDS.DIT)

## Metadata

- Rule ID: 2afafd61-6aae-4df4-baed-139fa1f4c345
- Status: test
- Level: medium
- Author: Thomas Patzke
- Date: 2019-01-16
- Modified: 2022-03-11
- Source Path: rules/windows/process_creation/proc_creation_win_ntdsutil_usage.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.003]]

## Detection

```yaml
selection:
  Image|endswith: \ntdsutil.exe
condition: selection
```

## False Positives

- NTDS maintenance

## References

- https://jpcertcc.github.io/ToolAnalysisResultSheet/details/ntdsutil.htm

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_ntdsutil_usage.yml)
