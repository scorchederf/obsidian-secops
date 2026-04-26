---
sigma_id: "fdeebdf0-9f3f-4d08-84a6-4c4d13e39fe4"
title: "Network Connection Initiated To Mega.nz"
framework: "sigma"
generated: "true"
source_path: "rules/windows/network_connection/net_connection_win_domain_mega_nz.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_domain_mega_nz.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "low"
logsource: "windows / network_connection"
aliases:
  - "fdeebdf0-9f3f-4d08-84a6-4c4d13e39fe4"
  - "Network Connection Initiated To Mega.nz"
attack_technique_ids:
  - "T1567.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Network Connection Initiated To Mega.nz

Detects a network connection initiated by a binary to "api.mega.co.nz".
Attackers were seen abusing file sharing websites similar to "mega.nz" in order to upload/download additional payloads.

## Metadata

- Rule ID: fdeebdf0-9f3f-4d08-84a6-4c4d13e39fe4
- Status: test
- Level: low
- Author: Florian Roth (Nextron Systems)
- Date: 2021-12-06
- Modified: 2024-05-31
- Source Path: rules/windows/network_connection/net_connection_win_domain_mega_nz.yml

## Logsource

- category: network_connection
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1567-exfiltration_over_web_service|T1567.002]]

## Detection

```yaml
selection:
  Initiated: 'true'
  DestinationHostname|endswith:
  - mega.co.nz
  - mega.nz
condition: selection
```

## False Positives

- Legitimate MEGA installers and utilities are expected to communicate with this domain. Exclude hosts that are known to be allowed to use this tool.

## References

- https://megatools.megous.com/
- https://www.mandiant.com/resources/russian-targeting-gov-business

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_domain_mega_nz.yml)
