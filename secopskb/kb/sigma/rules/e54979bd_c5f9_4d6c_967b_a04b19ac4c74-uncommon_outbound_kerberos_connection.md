---
sigma_id: "e54979bd-c5f9-4d6c-967b-a04b19ac4c74"
title: "Uncommon Outbound Kerberos Connection"
framework: "sigma"
generated: "true"
source_path: "rules/windows/network_connection/net_connection_win_susp_outbound_kerberos_connection.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_susp_outbound_kerberos_connection.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "medium"
logsource: "windows / network_connection"
aliases:
  - "e54979bd-c5f9-4d6c-967b-a04b19ac4c74"
  - "Uncommon Outbound Kerberos Connection"
attack_technique_ids:
  - "T1558"
  - "T1550.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Uncommon Outbound Kerberos Connection

Detects uncommon outbound network activity via Kerberos default port indicating possible lateral movement or first stage PrivEsc via delegation.

## Metadata

- Rule ID: e54979bd-c5f9-4d6c-967b-a04b19ac4c74
- Status: test
- Level: medium
- Author: Ilyas Ochkov, oscd.community
- Date: 2019-10-24
- Modified: 2024-03-15
- Source Path: rules/windows/network_connection/net_connection_win_susp_outbound_kerberos_connection.yml

## Logsource

- category: network_connection
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1558-steal_or_forge_kerberos_tickets|T1558]]
- [[kb/attack/techniques/T1550-use_alternate_authentication_material|T1550.003]]

## Detection

```yaml
selection:
  DestinationPort: 88
  Initiated: 'true'
filter_main_lsass:
  Image: C:\Windows\System32\lsass.exe
filter_optional_chrome:
  Image:
  - C:\Program Files (x86)\Google\Chrome\Application\chrome.exe
  - C:\Program Files\Google\Chrome\Application\chrome.exe
filter_optional_firefox:
  Image:
  - C:\Program Files (x86)\Mozilla Firefox\firefox.exe
  - C:\Program Files\Mozilla Firefox\firefox.exe
filter_optional_tomcat:
  Image|endswith: \tomcat\bin\tomcat8.exe
condition: selection and not 1 of filter_main_* and not 1 of filter_optional_*
```

## False Positives

- Web Browsers and third party application might generate similar activity. An initial baseline is required.

## References

- https://github.com/GhostPack/Rubeus

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_susp_outbound_kerberos_connection.yml)
