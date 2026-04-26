---
sigma_id: "75edd3fd-7146-48e5-9848-3013d7f0282c"
title: "DHCP Server Error Failed Loading the CallOut DLL"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/system/microsoft_windows_dhcp_server/win_system_susp_dhcp_config_failed.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/microsoft_windows_dhcp_server/win_system_susp_dhcp_config_failed.yml"
build_date: "2026-04-26 15:01:44"
status: "test"
level: "high"
logsource: "windows / system"
aliases:
  - "75edd3fd-7146-48e5-9848-3013d7f0282c"
  - "DHCP Server Error Failed Loading the CallOut DLL"
attack_technique_ids:
  - "T1574.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# DHCP Server Error Failed Loading the CallOut DLL

This rule detects a DHCP server error in which a specified Callout DLL (in registry) could not be loaded

## Metadata

- Rule ID: 75edd3fd-7146-48e5-9848-3013d7f0282c
- Status: test
- Level: high
- Author: Dimitrios Slamaris, @atc_project (fix)
- Date: 2017-05-15
- Modified: 2022-12-25
- Source Path: rules/windows/builtin/system/microsoft_windows_dhcp_server/win_system_susp_dhcp_config_failed.yml

## Logsource

- product: windows
- service: system

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow|T1574.001]]

## Detection

```yaml
selection:
  EventID:
  - 1031
  - 1032
  - 1034
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

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/microsoft_windows_dhcp_server/win_system_susp_dhcp_config_failed.yml)
