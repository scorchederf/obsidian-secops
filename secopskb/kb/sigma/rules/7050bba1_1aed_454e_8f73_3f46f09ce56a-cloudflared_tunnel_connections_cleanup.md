---
sigma_id: "7050bba1-1aed-454e-8f73-3f46f09ce56a"
title: "Cloudflared Tunnel Connections Cleanup"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_cloudflared_tunnel_cleanup.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_cloudflared_tunnel_cleanup.yml"
build_date: "2026-04-26 14:14:22"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "7050bba1-1aed-454e-8f73-3f46f09ce56a"
  - "Cloudflared Tunnel Connections Cleanup"
attack_technique_ids:
  - "T1102"
  - "T1090"
  - "T1572"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Cloudflared Tunnel Connections Cleanup

Detects execution of the "cloudflared" tool with the tunnel "cleanup" flag in order to cleanup tunnel connections.

## Metadata

- Rule ID: 7050bba1-1aed-454e-8f73-3f46f09ce56a
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-05-17
- Modified: 2023-12-21
- Source Path: rules/windows/process_creation/proc_creation_win_cloudflared_tunnel_cleanup.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1102-web_service|T1102]]
- [[kb/attack/techniques/T1090-proxy|T1090]]
- [[kb/attack/techniques/T1572-protocol_tunneling|T1572]]

## Detection

```yaml
selection:
  CommandLine|contains|all:
  - ' tunnel '
  - 'cleanup '
  CommandLine|contains:
  - '-config '
  - '-connector-id '
condition: selection
```

## False Positives

- Legitimate usage of Cloudflared.

## References

- https://github.com/cloudflare/cloudflared
- https://developers.cloudflare.com/cloudflare-one/connections/connect-apps

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_cloudflared_tunnel_cleanup.yml)
