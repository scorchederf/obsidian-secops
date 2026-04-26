---
sigma_id: "d7fb8f0e-bd5f-45c2-b467-19571c490d7e"
title: "Cleartext Protocol Usage"
framework: "sigma"
generated: "true"
source_path: "rules/network/firewall/net_firewall_cleartext_protocols.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/network/firewall/net_firewall_cleartext_protocols.yml"
build_date: "2026-04-26 14:14:22"
status: "stable"
level: "low"
logsource: "firewall"
aliases:
  - "d7fb8f0e-bd5f-45c2-b467-19571c490d7e"
  - "Cleartext Protocol Usage"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Cleartext Protocol Usage

Ensure that all account usernames and authentication credentials are transmitted across networks using encrypted channels.
Ensure that an encryption is used for all sensitive information in transit. Ensure that an encrypted channels is used for all administrative account access.

## Metadata

- Rule ID: d7fb8f0e-bd5f-45c2-b467-19571c490d7e
- Status: stable
- Level: low
- Author: Alexandr Yampolskyi, SOC Prime, Tim Shelton
- Date: 2019-03-26
- Modified: 2022-10-10
- Source Path: rules/network/firewall/net_firewall_cleartext_protocols.yml

## Logsource

- category: firewall

## Detection

```yaml
selection:
  dst_port:
  - 8080
  - 21
  - 80
  - 23
  - 50000
  - 1521
  - 27017
  - 3306
  - 1433
  - 11211
  - 15672
  - 5900
  - 5901
  - 5902
  - 5903
  - 5904
selection_allow1:
  action:
  - forward
  - accept
  - 2
selection_allow2:
  blocked: 'false'
condition: selection and 1 of selection_allow*
```

## False Positives

- Unknown

## References

- https://www.cisecurity.org/controls/cis-controls-list/
- https://www.pcisecuritystandards.org/documents/PCI_DSS_v3-2-1.pdf
- https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.04162018.pdf

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/network/firewall/net_firewall_cleartext_protocols.yml)
