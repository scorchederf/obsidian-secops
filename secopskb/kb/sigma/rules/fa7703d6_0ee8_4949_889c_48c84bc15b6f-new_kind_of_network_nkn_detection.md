---
sigma_id: "fa7703d6-0ee8-4949-889c-48c84bc15b6f"
title: "New Kind of Network (NKN) Detection"
framework: "sigma"
generated: "true"
source_path: "rules/network/zeek/zeek_dns_nkn.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/network/zeek/zeek_dns_nkn.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "low"
logsource: "zeek / dns"
aliases:
  - "fa7703d6-0ee8-4949-889c-48c84bc15b6f"
  - "New Kind of Network (NKN) Detection"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# New Kind of Network (NKN) Detection

NKN is a networking service using blockchain technology to support a decentralized network of peers. While there are legitimate uses for it, it can also be used as a C2 channel. This rule looks for a DNS request to the ma>

## Metadata

- Rule ID: fa7703d6-0ee8-4949-889c-48c84bc15b6f
- Status: test
- Level: low
- Author: Michael Portera (@mportatoes)
- Date: 2022-04-21
- Source Path: rules/network/zeek/zeek_dns_nkn.yml

## Logsource

- product: zeek
- service: dns

## Detection

```yaml
selection:
  query|contains|all:
  - seed
  - .nkn.org
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/nknorg/nkn-sdk-go
- https://unit42.paloaltonetworks.com/manageengine-godzilla-nglite-kdcsponge/
- https://github.com/Maka8ka/NGLite

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/network/zeek/zeek_dns_nkn.yml)
