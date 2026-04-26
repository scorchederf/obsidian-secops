---
sigma_id: "7ac407cc-0f48-4328-aede-de1d2e6fef41"
title: "Standard User In High Privileged Group"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/lsa_server/win_lsa_server_normal_user_admin.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/lsa_server/win_lsa_server_normal_user_admin.yml"
build_date: "2026-04-26 14:14:35"
status: "test"
level: "medium"
logsource: "windows / lsa-server"
aliases:
  - "7ac407cc-0f48-4328-aede-de1d2e6fef41"
  - "Standard User In High Privileged Group"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Standard User In High Privileged Group

Detect standard users login that are part of high privileged groups such as the Administrator group

## Metadata

- Rule ID: 7ac407cc-0f48-4328-aede-de1d2e6fef41
- Status: test
- Level: medium
- Author: frack113
- Date: 2023-01-13
- Modified: 2023-05-05
- Source Path: rules/windows/builtin/lsa_server/win_lsa_server_normal_user_admin.yml

## Logsource

- definition: Requirements: Microsoft-Windows-LSA/Operational (199FE037-2B82-40A9-82AC-E1D46C792B99) Event Log must be enabled and collected in order to use this rule.
- product: windows
- service: lsa-server

## Detection

```yaml
selection:
  EventID: 300
  TargetUserSid|startswith: S-1-5-21-
  SidList|contains:
  - S-1-5-32-544
  - -500}
  - -518}
  - -519}
filter_main_admin:
  TargetUserSid|endswith:
  - '-500'
  - '-518'
  - '-519'
condition: selection and not 1 of filter_main_*
```

## False Positives

- Standard domain users who are part of the administrator group. These users shouldn't have these right. But in the case where it's necessary. They should be filtered out using the "TargetUserName" field

## References

- https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-identifiers
- https://learn.microsoft.com/en-us/windows-server/security/credentials-protection-and-management/configuring-additional-lsa-protection
- https://github.com/nasbench/EVTX-ETW-Resources/blob/7a806a148b3d9d381193d4a80356016e6e8b1ee8/ETWProvidersManifests/Windows11/22H2/W11_22H2_Pro_20221220_22621.963/WEPExplorer/LsaSrv.xml

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/lsa_server/win_lsa_server_normal_user_admin.yml)
