---
sigma_id: "e61e8a88-59a9-451c-874e-70fcc9740d67"
title: "New DNS ServerLevelPluginDll Installed"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_dns_server_level_plugin_dll.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_dns_server_level_plugin_dll.yml"
build_date: "2026-04-26 17:03:20"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "e61e8a88-59a9-451c-874e-70fcc9740d67"
  - "New DNS ServerLevelPluginDll Installed"
attack_technique_ids:
  - "T1574.001"
  - "T1112"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# New DNS ServerLevelPluginDll Installed

Detects the installation of a DNS plugin DLL via ServerLevelPluginDll parameter in registry, which can be used to execute code in context of the DNS server (restart required)

## Metadata

- Rule ID: e61e8a88-59a9-451c-874e-70fcc9740d67
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2017-05-08
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_dns_server_level_plugin_dll.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.001]]
- [[kb/attack/techniques/T1112-modify_registry|T1112]]

## Detection

```yaml
selection:
  TargetObject|endswith: \services\DNS\Parameters\ServerLevelPluginDll
condition: selection
```

## False Positives

- Unknown

## References

- https://medium.com/@esnesenon/feature-not-bug-dnsadmin-to-dc-compromise-in-one-line-a0f779b8dc83
- https://blog.3or.de/hunting-dns-server-level-plugin-dll-injection.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_dns_server_level_plugin_dll.yml)
