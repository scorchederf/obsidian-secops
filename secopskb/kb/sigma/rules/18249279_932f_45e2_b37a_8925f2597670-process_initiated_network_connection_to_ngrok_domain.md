---
sigma_id: "18249279-932f-45e2-b37a-8925f2597670"
title: "Process Initiated Network Connection To Ngrok Domain"
framework: "sigma"
generated: "true"
source_path: "rules/windows/network_connection/net_connection_win_domain_ngrok.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_domain_ngrok.yml"
build_date: "2026-04-26 17:03:21"
status: "test"
level: "high"
logsource: "windows / network_connection"
aliases:
  - "18249279-932f-45e2-b37a-8925f2597670"
  - "Process Initiated Network Connection To Ngrok Domain"
attack_technique_ids:
  - "T1567"
  - "T1572"
  - "T1102"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

# Process Initiated Network Connection To Ngrok Domain

Detects an executable initiating a network connection to "ngrok" domains.
Attackers were seen using this "ngrok" in order to store their second stage payloads and malware.
While communication with such domains can be legitimate, often times is a sign of either data exfiltration by malicious actors or additional download.

## Metadata

- Rule ID: 18249279-932f-45e2-b37a-8925f2597670
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2022-07-16
- Modified: 2025-07-30
- Source Path: rules/windows/network_connection/net_connection_win_domain_ngrok.yml

## Logsource

- category: network_connection
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1567-exfiltration_over_web_service|T1567]]
- [[kb/attack/techniques/T1572-protocol_tunneling|T1572]]
- [[kb/attack/techniques/T1102-web_service|T1102]]

## Detection

```yaml
selection:
  Initiated: 'true'
  DestinationHostname|endswith:
  - .ngrok-free.app
  - .ngrok-free.dev
  - .ngrok.app
  - .ngrok.dev
  - .ngrok.io
condition: selection
```

## False Positives

- Legitimate use of the ngrok service.

## References

- https://ngrok.com/
- https://ngrok.com/blog-post/new-ngrok-domains
- https://www.virustotal.com/gui/file/cca0c1182ac114b44dc52dd2058fcd38611c20bb6b5ad84710681d38212f835a/
- https://www.rnbo.gov.ua/files/2023_YEAR/CYBERCENTER/november/APT29%20attacks%20Embassies%20using%20CVE-2023-38831%20-%20report%20en.pdf

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_domain_ngrok.yml)
