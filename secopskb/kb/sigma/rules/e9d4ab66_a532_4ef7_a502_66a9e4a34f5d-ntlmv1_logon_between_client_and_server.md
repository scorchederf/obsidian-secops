---
sigma_id: "e9d4ab66-a532-4ef7-a502-66a9e4a34f5d"
title: "NTLMv1 Logon Between Client and Server"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/system/lsasrv/win_system_lsasrv_ntlmv1.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/lsasrv/win_system_lsasrv_ntlmv1.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "medium"
logsource: "windows / system"
aliases:
  - "e9d4ab66-a532-4ef7-a502-66a9e4a34f5d"
  - "NTLMv1 Logon Between Client and Server"
attack_technique_ids:
  - "T1550.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# NTLMv1 Logon Between Client and Server

Detects the reporting of NTLMv1 being used between a client and server. NTLMv1 is insecure as the underlying encryption algorithms can be brute-forced by modern hardware.

## Metadata

- Rule ID: e9d4ab66-a532-4ef7-a502-66a9e4a34f5d
- Status: test
- Level: medium
- Author: Tim Shelton, Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-04-26
- Modified: 2023-06-06
- Source Path: rules/windows/builtin/system/lsasrv/win_system_lsasrv_ntlmv1.yml

## Logsource

- product: windows
- service: system

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1550-use_alternate_authentication_material|T1550.002]]

## Detection

```yaml
selection:
  Provider_Name: LsaSrv
  EventID:
  - 6038
  - 6039
condition: selection
```

## False Positives

- Environments that use NTLMv1

## References

- https://github.com/nasbench/EVTX-ETW-Resources/blob/f1b010ce0ee1b71e3024180de1a3e67f99701fe4/ETWProvidersManifests/Windows10/22H2/W10_22H2_Pro_20230321_19045.2728/WEPExplorer/LsaSrv.xml

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/lsasrv/win_system_lsasrv_ntlmv1.yml)
