---
sigma_id: "9a019ffc-3580-4c9d-8d87-079f7e8d3fd4"
title: "Cloudflared Tunnel Execution"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_cloudflared_tunnel_run.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_cloudflared_tunnel_run.yml"
build_date: "2026-04-26 14:14:22"
status: "test"
level: "medium"
logsource: "windows / process_creation"
aliases:
  - "9a019ffc-3580-4c9d-8d87-079f7e8d3fd4"
  - "Cloudflared Tunnel Execution"
attack_technique_ids:
  - "T1102"
  - "T1090"
  - "T1572"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Cloudflared Tunnel Execution

Detects execution of the "cloudflared" tool to connect back to a tunnel. This was seen used by threat actors to maintain persistence and remote access to compromised networks.

## Metadata

- Rule ID: 9a019ffc-3580-4c9d-8d87-079f7e8d3fd4
- Status: test
- Level: medium
- Author: Janantha Marasinghe, Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-05-17
- Modified: 2023-12-20
- Source Path: rules/windows/process_creation/proc_creation_win_cloudflared_tunnel_run.yml

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
  - ' run '
  CommandLine|contains:
  - '-config '
  - '-credentials-contents '
  - '-credentials-file '
  - '-token '
condition: selection
```

## False Positives

- Legitimate usage of Cloudflared tunnel.

## References

- https://blog.reconinfosec.com/emergence-of-akira-ransomware-group
- https://github.com/cloudflare/cloudflared
- https://developers.cloudflare.com/cloudflare-one/connections/connect-apps

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_cloudflared_tunnel_run.yml)
