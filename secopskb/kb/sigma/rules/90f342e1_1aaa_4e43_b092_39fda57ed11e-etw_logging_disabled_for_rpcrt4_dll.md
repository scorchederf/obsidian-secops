---
sigma_id: "90f342e1-1aaa-4e43-b092-39fda57ed11e"
title: "ETW Logging Disabled For rpcrt4.dll"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_rpcrt4_etw_tamper.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_rpcrt4_etw_tamper.yml"
build_date: "2026-04-26 14:14:24"
status: "test"
level: "low"
logsource: "windows / registry_set"
aliases:
  - "90f342e1-1aaa-4e43-b092-39fda57ed11e"
  - "ETW Logging Disabled For rpcrt4.dll"
attack_technique_ids:
  - "T1112"
  - "T1562"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# ETW Logging Disabled For rpcrt4.dll

Detects changes to the "ExtErrorInformation" key in order to disable ETW logging for rpcrt4.dll

## Metadata

- Rule ID: 90f342e1-1aaa-4e43-b092-39fda57ed11e
- Status: test
- Level: low
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-12-09
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_rpcrt4_etw_tamper.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1112-modify_registry|T1112]]
- [[kb/attack/techniques/T1562-impair_defenses|T1562]]

## Detection

```yaml
selection:
  TargetObject|endswith: \Microsoft\Windows NT\Rpc\ExtErrorInformation
  Details:
  - DWORD (0x00000000)
  - DWORD (0x00000002)
condition: selection
```

## False Positives

- Unknown

## References

- http://redplait.blogspot.com/2020/07/whats-wrong-with-etw.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_rpcrt4_etw_tamper.yml)
