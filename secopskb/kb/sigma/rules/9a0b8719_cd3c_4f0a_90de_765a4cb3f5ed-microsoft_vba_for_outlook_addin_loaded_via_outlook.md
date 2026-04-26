---
sigma_id: "9a0b8719-cd3c-4f0a-90de-765a4cb3f5ed"
title: "Microsoft VBA For Outlook Addin Loaded Via Outlook"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_office_outlook_outlvba_load.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_office_outlook_outlvba_load.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "medium"
logsource: "windows / image_load"
aliases:
  - "9a0b8719-cd3c-4f0a-90de-765a4cb3f5ed"
  - "Microsoft VBA For Outlook Addin Loaded Via Outlook"
attack_technique_ids:
  - "T1204.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Microsoft VBA For Outlook Addin Loaded Via Outlook

Detects outlvba (Microsoft VBA for Outlook Addin) DLL being loaded by the outlook process

## Metadata

- Rule ID: 9a0b8719-cd3c-4f0a-90de-765a4cb3f5ed
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-02-08
- Modified: 2024-03-12
- Source Path: rules/windows/image_load/image_load_office_outlook_outlvba_load.yml

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1204-user_execution|T1204.002]]

## Detection

```yaml
selection:
  Image|endswith: \outlook.exe
  ImageLoaded|endswith: \outlvba.dll
condition: selection
```

## False Positives

- Legitimate macro usage. Add the appropriate filter according to your environment

## References

- https://speakerdeck.com/heirhabarov/hunting-for-persistence-via-microsoft-exchange-server-or-outlook?slide=58

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_office_outlook_outlvba_load.yml)
