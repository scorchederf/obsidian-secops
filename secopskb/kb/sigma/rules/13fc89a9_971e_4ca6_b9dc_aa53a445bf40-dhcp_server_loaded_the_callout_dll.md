---
sigma_id: "13fc89a9-971e-4ca6-b9dc-aa53a445bf40"
title: "DHCP Server Loaded the CallOut DLL"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/system/microsoft_windows_dhcp_server/win_system_susp_dhcp_config.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/microsoft_windows_dhcp_server/win_system_susp_dhcp_config.yml"
build_date: "2026-04-26 17:03:18"
status: "test"
level: "high"
logsource: "windows / system"
aliases:
  - "13fc89a9-971e-4ca6-b9dc-aa53a445bf40"
  - "DHCP Server Loaded the CallOut DLL"
attack_technique_ids:
  - "T1574.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# DHCP Server Loaded the CallOut DLL

This rule detects a DHCP server in which a specified Callout DLL (in registry) was loaded

## Metadata

- Rule ID: 13fc89a9-971e-4ca6-b9dc-aa53a445bf40
- Status: test
- Level: high
- Author: Dimitrios Slamaris
- Date: 2017-05-15
- Modified: 2022-12-25
- Source Path: rules/windows/builtin/system/microsoft_windows_dhcp_server/win_system_susp_dhcp_config.yml

## Logsource

- product: windows
- service: system

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.001]]

## Detection

```yaml
selection:
  EventID: 1033
  Provider_Name: Microsoft-Windows-DHCP-Server
condition: selection
```

## False Positives

- Unknown

## References

- https://blog.3or.de/mimilib-dhcp-server-callout-dll-injection.html
- https://technet.microsoft.com/en-us/library/cc726884(v=ws.10).aspx
- https://msdn.microsoft.com/de-de/library/windows/desktop/aa363389(v=vs.85).aspx

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/microsoft_windows_dhcp_server/win_system_susp_dhcp_config.yml)
