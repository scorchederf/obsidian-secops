---
sigma_id: "8e1cb247-6cf6-42fa-b440-3f27d57e9936"
title: "Potential Persistence Via Microsoft Office Add-In"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_office_addin_persistence.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_office_addin_persistence.yml"
build_date: "2026-04-26 15:01:49"
status: "test"
level: "high"
logsource: "windows / file_event"
aliases:
  - "8e1cb247-6cf6-42fa-b440-3f27d57e9936"
  - "Potential Persistence Via Microsoft Office Add-In"
attack_technique_ids:
  - "T1137.006"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Potential Persistence Via Microsoft Office Add-In

Detects potential persistence activity via startup add-ins that load when Microsoft Office starts (.wll/.xll are simply .dll fit for Word or Excel).

## Metadata

- Rule ID: 8e1cb247-6cf6-42fa-b440-3f27d57e9936
- Status: test
- Level: high
- Author: NVISO
- Date: 2020-05-11
- Modified: 2023-02-08
- Source Path: rules/windows/file/file_event/file_event_win_office_addin_persistence.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1137-office_application_startup|T1137.006]]

## Detection

```yaml
selection_wlldropped:
  TargetFilename|contains: \Microsoft\Word\Startup\
  TargetFilename|endswith: .wll
selection_xlldropped:
  TargetFilename|contains: \Microsoft\Excel\Startup\
  TargetFilename|endswith: .xll
selection_xladropped:
  TargetFilename|contains: Microsoft\Excel\XLSTART\
  TargetFilename|endswith: .xlam
selection_generic:
  TargetFilename|contains: \Microsoft\Addins\
  TargetFilename|endswith:
  - .xlam
  - .xla
  - .ppam
condition: 1 of selection_*
```

## False Positives

- Legitimate add-ins

## References

- Internal Research
- https://labs.withsecure.com/publications/add-in-opportunities-for-office-persistence
- https://github.com/redcanaryco/atomic-red-team/blob/4ae9580a1a8772db87a1b6cdb0d03e5af231e966/atomics/T1137.006/T1137.006.md

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_office_addin_persistence.yml)
