---
sigma_id: "b9e1f193-d236-4451-aaae-2f3d2102120d"
title: "Cisco Sniffing"
framework: "sigma"
generated: "true"
source_path: "rules/network/cisco/aaa/cisco_cli_net_sniff.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/network/cisco/aaa/cisco_cli_net_sniff.yml"
build_date: "2026-04-26 14:14:22"
status: "test"
level: "medium"
logsource: "cisco / aaa"
aliases:
  - "b9e1f193-d236-4451-aaae-2f3d2102120d"
  - "Cisco Sniffing"
attack_technique_ids:
  - "T1040"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Cisco Sniffing

Show when a monitor or a span/rspan is setup or modified

## Metadata

- Rule ID: b9e1f193-d236-4451-aaae-2f3d2102120d
- Status: test
- Level: medium
- Author: Austin Clark
- Date: 2019-08-11
- Modified: 2023-01-04
- Source Path: rules/network/cisco/aaa/cisco_cli_net_sniff.yml

## Logsource

- product: cisco
- service: aaa

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1040-network_sniffing|T1040]]

## Detection

```yaml
keywords:
- monitor capture point
- set span
- set rspan
condition: keywords
```

## False Positives

- Admins may setup new or modify old spans, or use a monitor for troubleshooting

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/network/cisco/aaa/cisco_cli_net_sniff.yml)
