---
sigma_id: "50e54b8d-ad73-43f8-96a1-5191685b17a4"
title: "Silenttrinity Stager Msbuild Activity"
framework: "sigma"
generated: "true"
source_path: "rules/windows/network_connection/net_connection_win_silenttrinity_stager_msbuild_activity.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_silenttrinity_stager_msbuild_activity.yml"
build_date: "2026-04-27 19:13:56"
status: "test"
level: "high"
logsource: "windows / network_connection"
aliases:
  - "50e54b8d-ad73-43f8-96a1-5191685b17a4"
  - "Silenttrinity Stager Msbuild Activity"
attack_technique_ids:
  - "T1127.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects a possible remote connections to Silenttrinity c2

## Logsource

- category: network_connection
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1127-trusted_developer_utilities_proxy_execution#^t1127001-msbuild|T1127.001: MSBuild]]

## Detection

```yaml
selection:
  Image|endswith: \msbuild.exe
filter:
  DestinationPort:
  - 80
  - 443
  Initiated: 'true'
condition: selection and filter
```

## False Positives

- Unknown

## References

- https://www.blackhillsinfosec.com/my-first-joyride-with-silenttrinity/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_silenttrinity_stager_msbuild_activity.yml)
