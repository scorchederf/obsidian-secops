---
sigma_id: "25eabf56-22f0-4915-a1ed-056b8dae0a68"
title: "Suspicious Dropbox API Usage"
framework: "sigma"
generated: "true"
source_path: "rules/windows/network_connection/net_connection_win_domain_dropbox_api.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_domain_dropbox_api.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "high"
logsource: "windows / network_connection"
aliases:
  - "25eabf56-22f0-4915-a1ed-056b8dae0a68"
  - "Suspicious Dropbox API Usage"
attack_technique_ids:
  - "T1105"
  - "T1567.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Dropbox API Usage

Detects an executable that isn't dropbox but communicates with the Dropbox API

## Metadata

- Rule ID: 25eabf56-22f0-4915-a1ed-056b8dae0a68
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2022-04-20
- Source Path: rules/windows/network_connection/net_connection_win_domain_dropbox_api.yml

## Logsource

- category: network_connection
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1105-ingress_tool_transfer|T1105]]
- [[kb/attack/techniques/T1567-exfiltration_over_web_service|T1567.002]]

## Detection

```yaml
selection:
  Initiated: 'true'
  DestinationHostname|endswith:
  - api.dropboxapi.com
  - content.dropboxapi.com
filter_main_legit_dropbox:
  Image|contains: \Dropbox
condition: selection and not 1 of filter_main_*
```

## False Positives

- Legitimate use of the API with a tool that the author wasn't aware of

## References

- https://app.any.run/tasks/7e906adc-9d11-447f-8641-5f40375ecebb
- https://www.zscaler.com/blogs/security-research/new-espionage-attack-molerats-apt-targeting-users-middle-east

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_domain_dropbox_api.yml)
