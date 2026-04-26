---
sigma_id: "94dc4390-6b7c-4784-8ffc-335334404650"
title: "Dump Ntds.dit To Suspicious Location"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/application/esent/win_esent_ntdsutil_abuse_susp_location.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/application/esent/win_esent_ntdsutil_abuse_susp_location.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "medium"
logsource: "windows / application"
aliases:
  - "94dc4390-6b7c-4784-8ffc-335334404650"
  - "Dump Ntds.dit To Suspicious Location"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Dump Ntds.dit To Suspicious Location

Detects potential abuse of ntdsutil to dump ntds.dit database to a suspicious location

## Metadata

- Rule ID: 94dc4390-6b7c-4784-8ffc-335334404650
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-08-14
- Modified: 2023-10-23
- Source Path: rules/windows/builtin/application/esent/win_esent_ntdsutil_abuse_susp_location.yml

## Logsource

- product: windows
- service: application

## Detection

```yaml
selection_root:
  Provider_Name: ESENT
  EventID: 325
  Data|contains: ntds.dit
selection_paths:
  Data|contains:
  - :\ntds.dit
  - \Appdata\
  - \Desktop\
  - \Downloads\
  - \Perflogs\
  - \Temp\
  - \Users\Public\
condition: all of selection_*
```

## False Positives

- Legitimate backup operation/creating shadow copies

## References

- https://twitter.com/mgreen27/status/1558223256704122882
- https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/jj574207(v=ws.11)

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/application/esent/win_esent_ntdsutil_abuse_susp_location.yml)
