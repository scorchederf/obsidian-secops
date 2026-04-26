---
sigma_id: "c649a6c7-cd8c-4a78-9c04-000fc76df954"
title: "Potentially Suspicious Wuauclt Network Connection"
framework: "sigma"
generated: "true"
source_path: "rules/windows/network_connection/net_connection_win_wuauclt_network_connection.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_wuauclt_network_connection.yml"
build_date: "2026-04-26 14:14:33"
status: "test"
level: "medium"
logsource: "windows / network_connection"
aliases:
  - "c649a6c7-cd8c-4a78-9c04-000fc76df954"
  - "Potentially Suspicious Wuauclt Network Connection"
attack_technique_ids:
  - "T1218"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potentially Suspicious Wuauclt Network Connection

Detects the use of the Windows Update Client binary (wuauclt.exe) to proxy execute code and making network connections.
One could easily make the DLL spawn a new process and inject to it to proxy the network connection and bypass this rule.

## Metadata

- Rule ID: c649a6c7-cd8c-4a78-9c04-000fc76df954
- Status: test
- Level: medium
- Author: Roberto Rodriguez (Cyb3rWard0g), OTR (Open Threat Research)
- Date: 2020-10-12
- Modified: 2024-03-12
- Source Path: rules/windows/network_connection/net_connection_win_wuauclt_network_connection.yml

## Logsource

- category: network_connection
- definition: Requirements: The CommandLine field enrichment is required in order for this rule to be used.
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1218-system_binary_proxy_execution|T1218]]

## Detection

```yaml
selection:
  Image|contains: wuauclt
  CommandLine|contains: ' /RunHandlerComServer'
filter_main_ip:
  DestinationIp|cidr:
  - 127.0.0.0/8
  - 10.0.0.0/8
  - 169.254.0.0/16
  - 172.16.0.0/12
  - 192.168.0.0/16
  - ::1/128
  - fe80::/10
  - fc00::/7
filter_main_msrange:
  DestinationIp|cidr:
  - 20.184.0.0/13
  - 20.192.0.0/10
  - 23.79.0.0/16
  - 51.10.0.0/15
  - 51.103.0.0/16
  - 51.104.0.0/15
  - 52.224.0.0/11
filter_main_uus:
  CommandLine|contains:
  - :\Windows\UUS\Packages\Preview\amd64\updatedeploy.dll /ClassId
  - :\Windows\UUS\amd64\UpdateDeploy.dll /ClassId
filter_main_winsxs:
  CommandLine|contains|all:
  - :\Windows\WinSxS\
  - '\UpdateDeploy.dll /ClassId '
filter_main_cli_null:
  CommandLine: null
filter_main_cli_empty:
  CommandLine: ''
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unknown

## References

- https://dtm.uk/wuauclt/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_wuauclt_network_connection.yml)
