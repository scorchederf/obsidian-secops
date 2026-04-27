---
sigma_id: "10344bb3-7f65-46c2-b915-2d00d47be5b0"
title: "IE ZoneMap Setting Downgraded To MyComputer Zone For HTTP Protocols Via CLI"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_registry_ie_security_zone_protocol_defaults_downgrade.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_registry_ie_security_zone_protocol_defaults_downgrade.yml"
build_date: "2026-04-26 17:03:19"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "10344bb3-7f65-46c2-b915-2d00d47be5b0"
  - "IE ZoneMap Setting Downgraded To MyComputer Zone For HTTP Protocols Via CLI"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# IE ZoneMap Setting Downgraded To MyComputer Zone For HTTP Protocols Via CLI

Detects changes to Internet Explorer's (IE / Windows Internet properties) ZoneMap configuration of the "HTTP" and "HTTPS" protocols to point to the "My Computer" zone. This allows downloaded files from the Internet to be granted the same level of trust as files stored locally.

## Metadata

- Rule ID: 10344bb3-7f65-46c2-b915-2d00d47be5b0
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-09-05
- Source Path: rules/windows/process_creation/proc_creation_win_registry_ie_security_zone_protocol_defaults_downgrade.yml

## Logsource

- category: process_creation
- product: windows

## Detection

```yaml
selection:
  CommandLine|contains|all:
  - \Microsoft\Windows\CurrentVersion\Internet Settings\ZoneMap\ProtocolDefaults
  - http
  - ' 0'
condition: selection
```

## False Positives

- Unknown

## References

- https://twitter.com/M_haggis/status/1699056847154725107
- https://twitter.com/JAMESWT_MHT/status/1699042827261391247
- https://learn.microsoft.com/en-us/troubleshoot/developer/browsers/security-privacy/ie-security-zones-registry-entries
- https://www.virustotal.com/gui/file/339ff720c74dc44265b917b6d3e3ba0411d61f3cd3c328e9a2bae81592c8a6e5/content

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_registry_ie_security_zone_protocol_defaults_downgrade.yml)
