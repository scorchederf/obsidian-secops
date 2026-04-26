---
sigma_id: "23ceaf5c-b6f1-4a32-8559-f2ff734be516"
title: "Dumping Process via Sqldumper.exe"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_lolbin_susp_sqldumper_activity.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_susp_sqldumper_activity.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "23ceaf5c-b6f1-4a32-8559-f2ff734be516"
  - "Dumping Process via Sqldumper.exe"
attack_technique_ids:
  - "T1003.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Dumping Process via Sqldumper.exe

Detects process dump via legitimate sqldumper.exe binary

## Metadata

- Rule ID: 23ceaf5c-b6f1-4a32-8559-f2ff734be516
- Status: test
- Level: medium
- Author: Kirill Kiryanov, oscd.community
- Date: 2020-10-08
- Modified: 2021-11-27
- Source Path: rules/windows/process_creation/proc_creation_win_lolbin_susp_sqldumper_activity.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.001]]

## Detection

```yaml
selection:
  Image|endswith: \sqldumper.exe
  CommandLine|contains:
  - '0x0110'
  - 0x01100:40
condition: selection
```

## False Positives

- Legitimate MSSQL Server actions

## References

- https://twitter.com/countuponsec/status/910977826853068800
- https://twitter.com/countuponsec/status/910969424215232518
- https://lolbas-project.github.io/lolbas/OtherMSBinaries/Sqldumper/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_lolbin_susp_sqldumper_activity.yml)
