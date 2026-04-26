---
sigma_id: "0b8baa3f-575c-46ee-8715-d6f28cc7d33c"
title: "NTDS.DIT Created"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_ntds_dit_creation.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_ntds_dit_creation.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "low"
logsource: "windows / file_event"
aliases:
  - "0b8baa3f-575c-46ee-8715-d6f28cc7d33c"
  - "NTDS.DIT Created"
attack_technique_ids:
  - "T1003.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# NTDS.DIT Created

Detects creation of a file named "ntds.dit" (Active Directory Database)

## Metadata

- Rule ID: 0b8baa3f-575c-46ee-8715-d6f28cc7d33c
- Status: test
- Level: low
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-05-05
- Source Path: rules/windows/file/file_event/file_event_win_ntds_dit_creation.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.003]]

## Detection

```yaml
selection:
  TargetFilename|endswith: ntds.dit
condition: selection
```

## False Positives

- Unknown

## References

- Internal Research

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_ntds_dit_creation.yml)
