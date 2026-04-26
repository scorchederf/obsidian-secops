---
sigma_id: "7100f7e3-92ce-4584-b7b7-01b40d3d4118"
title: "Default Cobalt Strike Certificate"
framework: "sigma"
generated: "true"
source_path: "rules/network/zeek/zeek_default_cobalt_strike_certificate.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/network/zeek/zeek_default_cobalt_strike_certificate.yml"
build_date: "2026-04-26 14:14:23"
status: "test"
level: "high"
logsource: "zeek / x509"
aliases:
  - "7100f7e3-92ce-4584-b7b7-01b40d3d4118"
  - "Default Cobalt Strike Certificate"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Default Cobalt Strike Certificate

Detects the presence of default Cobalt Strike certificate in the HTTPS traffic

## Metadata

- Rule ID: 7100f7e3-92ce-4584-b7b7-01b40d3d4118
- Status: test
- Level: high
- Author: Bhabesh Raj
- Date: 2021-06-23
- Modified: 2022-10-09
- Source Path: rules/network/zeek/zeek_default_cobalt_strike_certificate.yml

## Logsource

- product: zeek
- service: x509

## ATT&CK Mapping

### Software Tags

- S0154

## Detection

```yaml
selection:
  certificate.serial: 8BB00EE
condition: selection
```

## False Positives

- Unknown

## References

- https://sergiusechel.medium.com/improving-the-network-based-detection-of-cobalt-strike-c2-servers-in-the-wild-while-reducing-the-6964205f6468

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/network/zeek/zeek_default_cobalt_strike_certificate.yml)
