---
sigma_id: "e6e88853-5f20-4c4a-8d26-cd469fd8d31f"
title: "Ntdsutil Abuse"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/application/esent/win_esent_ntdsutil_abuse.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/application/esent/win_esent_ntdsutil_abuse.yml"
build_date: "2026-04-26 14:14:30"
status: "test"
level: "medium"
logsource: "windows / application"
aliases:
  - "e6e88853-5f20-4c4a-8d26-cd469fd8d31f"
  - "Ntdsutil Abuse"
attack_technique_ids:
  - "T1003.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Ntdsutil Abuse

Detects potential abuse of ntdsutil to dump ntds.dit database

## Metadata

- Rule ID: e6e88853-5f20-4c4a-8d26-cd469fd8d31f
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-08-14
- Source Path: rules/windows/builtin/application/esent/win_esent_ntdsutil_abuse.yml

## Logsource

- product: windows
- service: application

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1003-os_credential_dumping|T1003.003]]

## Detection

```yaml
selection:
  Provider_Name: ESENT
  EventID:
  - 216
  - 325
  - 326
  - 327
  Data|contains: ntds.dit
condition: selection
```

## False Positives

- Legitimate backup operation/creating shadow copies

## References

- https://twitter.com/mgreen27/status/1558223256704122882
- https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/jj574207(v=ws.11)

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/application/esent/win_esent_ntdsutil_abuse.yml)
