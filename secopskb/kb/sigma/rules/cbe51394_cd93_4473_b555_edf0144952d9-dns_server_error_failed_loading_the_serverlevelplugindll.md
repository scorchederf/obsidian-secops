---
sigma_id: "cbe51394-cd93-4473-b555-edf0144952d9"
title: "DNS Server Error Failed Loading the ServerLevelPluginDLL"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/dns_server/win_dns_server_susp_server_level_plugin_dll.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/dns_server/win_dns_server_susp_server_level_plugin_dll.yml"
build_date: "2026-04-26 14:14:23"
status: "test"
level: "high"
logsource: "windows / dns-server"
aliases:
  - "cbe51394-cd93-4473-b555-edf0144952d9"
  - "DNS Server Error Failed Loading the ServerLevelPluginDLL"
attack_technique_ids:
  - "T1574.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# DNS Server Error Failed Loading the ServerLevelPluginDLL

Detects a DNS server error in which a specified plugin DLL (in registry) could not be loaded

## Metadata

- Rule ID: cbe51394-cd93-4473-b555-edf0144952d9
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2017-05-08
- Modified: 2023-02-05
- Source Path: rules/windows/builtin/dns_server/win_dns_server_susp_server_level_plugin_dll.yml

## Logsource

- product: windows
- service: dns-server

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.001]]

## Detection

```yaml
selection:
  EventID:
  - 150
  - 770
  - 771
condition: selection
```

## False Positives

- Unknown

## References

- https://medium.com/@esnesenon/feature-not-bug-dnsadmin-to-dc-compromise-in-one-line-a0f779b8dc83
- https://technet.microsoft.com/en-us/library/cc735829(v=ws.10).aspx
- https://twitter.com/gentilkiwi/status/861641945944391680

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/dns_server/win_dns_server_susp_server_level_plugin_dll.yml)
