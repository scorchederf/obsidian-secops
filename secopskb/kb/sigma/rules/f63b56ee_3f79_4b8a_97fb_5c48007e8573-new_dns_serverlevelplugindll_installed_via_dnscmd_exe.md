---
sigma_id: "f63b56ee-3f79-4b8a-97fb-5c48007e8573"
title: "New DNS ServerLevelPluginDll Installed Via Dnscmd.EXE"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_dnscmd_install_new_server_level_plugin_dll.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_dnscmd_install_new_server_level_plugin_dll.yml"
build_date: "2026-04-26 15:01:47"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "f63b56ee-3f79-4b8a-97fb-5c48007e8573"
  - "New DNS ServerLevelPluginDll Installed Via Dnscmd.EXE"
attack_technique_ids:
  - "T1574.001"
  - "T1112"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# New DNS ServerLevelPluginDll Installed Via Dnscmd.EXE

Detects the installation of a DNS plugin DLL via ServerLevelPluginDll parameter in registry, which can be used to execute code in context of the DNS server (restart required)

## Metadata

- Rule ID: f63b56ee-3f79-4b8a-97fb-5c48007e8573
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2017-05-08
- Modified: 2023-02-05
- Source Path: rules/windows/process_creation/proc_creation_win_dnscmd_install_new_server_level_plugin_dll.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.001]]
- [[kb/attack/techniques/T1112-modify_registry|T1112]]

## Detection

```yaml
selection:
  Image|endswith: \dnscmd.exe
  CommandLine|contains|all:
  - /config
  - /serverlevelplugindll
condition: selection
```

## False Positives

- Unknown

## References

- https://medium.com/@esnesenon/feature-not-bug-dnsadmin-to-dc-compromise-in-one-line-a0f779b8dc83
- https://blog.3or.de/hunting-dns-server-level-plugin-dll-injection.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_dnscmd_install_new_server_level_plugin_dll.yml)
