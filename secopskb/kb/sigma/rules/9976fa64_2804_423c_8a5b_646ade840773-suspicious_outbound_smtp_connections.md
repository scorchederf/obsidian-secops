---
sigma_id: "9976fa64-2804-423c-8a5b-646ade840773"
title: "Suspicious Outbound SMTP Connections"
framework: "sigma"
generated: "true"
source_path: "rules/windows/network_connection/net_connection_win_susp_outbound_smtp_connections.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_susp_outbound_smtp_connections.yml"
build_date: "2026-04-26 14:14:36"
status: "test"
level: "medium"
logsource: "windows / network_connection"
aliases:
  - "9976fa64-2804-423c-8a5b-646ade840773"
  - "Suspicious Outbound SMTP Connections"
attack_technique_ids:
  - "T1048.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Outbound SMTP Connections

Adversaries may steal data by exfiltrating it over an un-encrypted network protocol other than that of the existing command and control channel.
The data may also be sent to an alternate network location from the main command and control server.

## Metadata

- Rule ID: 9976fa64-2804-423c-8a5b-646ade840773
- Status: test
- Level: medium
- Author: frack113
- Date: 2022-01-07
- Modified: 2022-09-21
- Source Path: rules/windows/network_connection/net_connection_win_susp_outbound_smtp_connections.yml

## Logsource

- category: network_connection
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1048-exfiltration_over_alternative_protocol|T1048.003]]

## Detection

```yaml
selection:
  DestinationPort:
  - 25
  - 587
  - 465
  - 2525
  Initiated: 'true'
filter_clients:
  Image|endswith:
  - \thunderbird.exe
  - \outlook.exe
filter_mailserver:
  Image|startswith: C:\Program Files\Microsoft\Exchange Server\
filter_outlook:
  Image|startswith: C:\Program Files\WindowsApps\microsoft.windowscommunicationsapps_
  Image|endswith: \HxTsr.exe
condition: selection and not 1 of filter_*
```

## False Positives

- Other SMTP tools

## References

- https://github.com/redcanaryco/atomic-red-team/blob/f339e7da7d05f6057fdfcdd3742bfcf365fee2a9/atomics/T1048.003/T1048.003.md#atomic-test-5---exfiltration-over-alternative-protocol---smtp
- https://www.ietf.org/rfc/rfc2821.txt

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/network_connection/net_connection_win_susp_outbound_smtp_connections.yml)
