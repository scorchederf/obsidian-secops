---
sigma_id: "550d3350-bb8a-4ff3-9533-2ba533f4a1c0"
title: "ProxyLogon MSExchange OabVirtualDirectory"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/msexchange/win_exchange_proxylogon_oabvirtualdir.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/msexchange/win_exchange_proxylogon_oabvirtualdir.yml"
build_date: "2026-04-26 17:03:21"
status: "test"
level: "critical"
logsource: "windows / msexchange-management"
aliases:
  - "550d3350-bb8a-4ff3-9533-2ba533f4a1c0"
  - "ProxyLogon MSExchange OabVirtualDirectory"
attack_technique_ids:
  - "T1587.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# ProxyLogon MSExchange OabVirtualDirectory

Detects specific patterns found after a successful ProxyLogon exploitation in relation to a Commandlet invocation of Set-OabVirtualDirectory

## Metadata

- Rule ID: 550d3350-bb8a-4ff3-9533-2ba533f4a1c0
- Status: test
- Level: critical
- Author: Florian Roth (Nextron Systems)
- Date: 2021-08-09
- Modified: 2023-01-23
- Source Path: rules/windows/builtin/msexchange/win_exchange_proxylogon_oabvirtualdir.yml

## Logsource

- product: windows
- service: msexchange-management

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1587-develop_capabilities|T1587.001]]

## Detection

```yaml
keywords_cmdlet:
  '|all':
  - OabVirtualDirectory
  - ' -ExternalUrl '
keywords_params:
- eval(request
- http://f/<script
- '"unsafe"};'
- function Page_Load()
condition: keywords_cmdlet and keywords_params
```

## False Positives

- Unlikely

## References

- https://bi-zone.medium.com/hunting-down-ms-exchange-attacks-part-1-proxylogon-cve-2021-26855-26858-27065-26857-6e885c5f197c

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/msexchange/win_exchange_proxylogon_oabvirtualdir.yml)
