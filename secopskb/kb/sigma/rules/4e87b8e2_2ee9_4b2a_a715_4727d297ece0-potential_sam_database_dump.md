---
sigma_id: "4e87b8e2-2ee9-4b2a-a715-4727d297ece0"
title: "Potential SAM Database Dump"
framework: "sigma"
generated: "true"
source_path: "rules/windows/file/file_event/file_event_win_sam_dump.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_sam_dump.yml"
build_date: "2026-04-26 15:01:49"
status: "test"
level: "high"
logsource: "windows / file_event"
aliases:
  - "4e87b8e2-2ee9-4b2a-a715-4727d297ece0"
  - "Potential SAM Database Dump"
attack_technique_ids:
  - "T1003.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Potential SAM Database Dump

Detects the creation of files that look like exports of the local SAM (Security Account Manager)

## Metadata

- Rule ID: 4e87b8e2-2ee9-4b2a-a715-4727d297ece0
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2022-02-11
- Modified: 2023-01-05
- Source Path: rules/windows/file/file_event/file_event_win_sam_dump.yml

## Logsource

- category: file_event
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.002]]

## Detection

```yaml
selection:
- TargetFilename|endswith:
  - \Temp\sam
  - \sam.sav
  - \Intel\sam
  - \sam.hive
  - \Perflogs\sam
  - \ProgramData\sam
  - \Users\Public\sam
  - \AppData\Local\sam
  - \AppData\Roaming\sam
  - _ShadowSteal.zip
  - \Documents\SAM.export
  - :\sam
- TargetFilename|contains:
  - \hive_sam_
  - \sam.save
  - \sam.export
  - \~reg_sam.save
  - \sam_backup
  - \sam.bck
  - \sam.backup
condition: selection
```

## False Positives

- Rare cases of administrative activity

## References

- https://github.com/search?q=CVE-2021-36934
- https://web.archive.org/web/20210725081645/https://github.com/cube0x0/CVE-2021-36934
- https://www.google.com/search?q=%22reg.exe+save%22+sam
- https://github.com/HuskyHacks/ShadowSteal
- https://github.com/FireFart/hivenightmare

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/file/file_event/file_event_win_sam_dump.yml)
