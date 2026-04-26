---
sigma_id: "b593fd50-7335-4682-a36c-4edcb68e4641"
title: "Monero Crypto Coin Mining Pool Lookup"
framework: "sigma"
generated: "true"
source_path: "rules/network/dns/net_dns_pua_cryptocoin_mining_xmr.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/network/dns/net_dns_pua_cryptocoin_mining_xmr.yml"
build_date: "2026-04-26 14:14:29"
status: "stable"
level: "high"
logsource: "dns"
aliases:
  - "b593fd50-7335-4682-a36c-4edcb68e4641"
  - "Monero Crypto Coin Mining Pool Lookup"
attack_technique_ids:
  - "T1496"
  - "T1567"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Monero Crypto Coin Mining Pool Lookup

Detects suspicious DNS queries to Monero mining pools

## Metadata

- Rule ID: b593fd50-7335-4682-a36c-4edcb68e4641
- Status: stable
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2021-10-24
- Source Path: rules/network/dns/net_dns_pua_cryptocoin_mining_xmr.yml

## Logsource

- category: dns

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1496-resource_hijacking|T1496]]
- [[kb/attack/techniques/T1567-exfiltration_over_web_service|T1567]]

## Detection

```yaml
selection:
  query|contains:
  - pool.minexmr.com
  - fr.minexmr.com
  - de.minexmr.com
  - sg.minexmr.com
  - ca.minexmr.com
  - us-west.minexmr.com
  - pool.supportxmr.com
  - mine.c3pool.com
  - xmr-eu1.nanopool.org
  - xmr-eu2.nanopool.org
  - xmr-us-east1.nanopool.org
  - xmr-us-west1.nanopool.org
  - xmr-asia1.nanopool.org
  - xmr-jp1.nanopool.org
  - xmr-au1.nanopool.org
  - xmr.2miners.com
  - xmr.hashcity.org
  - xmr.f2pool.com
  - xmrpool.eu
  - pool.hashvault.pro
condition: selection
```

## False Positives

- Legitimate crypto coin mining

## References

- https://www.nextron-systems.com/2021/10/24/monero-mining-pool-fqdns/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/network/dns/net_dns_pua_cryptocoin_mining_xmr.yml)
