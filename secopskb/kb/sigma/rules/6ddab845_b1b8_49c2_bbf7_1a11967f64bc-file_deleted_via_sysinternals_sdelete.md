---
sigma_id: "6ddab845-b1b8-49c2-bbf7-1a11967f64bc"
title: "File Deleted Via Sysinternals SDelete"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_delete/file_delete_win_sysinternals_sdelete_file_deletion.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_delete/file_delete_win_sysinternals_sdelete_file_deletion.yml"
build_date: "2026-04-26 14:14:25"
status: "test"
level: "medium"
logsource: "windows / file_delete"
aliases:
  - "6ddab845-b1b8-49c2-bbf7-1a11967f64bc"
  - "File Deleted Via Sysinternals SDelete"
attack_technique_ids:
  - "T1070.004"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# File Deleted Via Sysinternals SDelete

Detects the deletion of files by the Sysinternals SDelete utility. It looks for the common name pattern used to rename files.

## Metadata

- Rule ID: 6ddab845-b1b8-49c2-bbf7-1a11967f64bc
- Status: test
- Level: medium
- Author: Roberto Rodriguez (Cyb3rWard0g), OTR (Open Threat Research)
- Date: 2020-05-02
- Modified: 2023-02-15
- Source Path: rules/windows/file/file_delete/file_delete_win_sysinternals_sdelete_file_deletion.yml

## Logsource

- category: file_delete
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1070-indicator_removal|T1070.004]]

## Detection

```yaml
selection:
  TargetFilename|endswith:
  - .AAA
  - .ZZZ
filter_wireshark:
  TargetFilename|endswith: \Wireshark\radius\dictionary.alcatel-lucent.aaa
condition: selection and not 1 of filter_*
```

## False Positives

- Legitimate usage

## References

- https://github.com/OTRF/detection-hackathon-apt29/issues/9
- https://github.com/OTRF/ThreatHunter-Playbook/blob/2d4257f630f4c9770f78d0c1df059f891ffc3fec/docs/evals/apt29/detections/4.B.4_83D62033-105A-4A02-8B75-DAB52D8D51EC.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_delete/file_delete_win_sysinternals_sdelete_file_deletion.yml)
