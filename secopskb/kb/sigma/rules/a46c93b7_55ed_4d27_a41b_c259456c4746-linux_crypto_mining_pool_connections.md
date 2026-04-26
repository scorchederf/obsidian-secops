---
sigma_id: "a46c93b7-55ed-4d27-a41b-c259456c4746"
title: "Linux Crypto Mining Pool Connections"
framework: "sigma"
generated: "true"
source_path: "rules/linux/network_connection/net_connection_lnx_crypto_mining_indicators.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/network_connection/net_connection_lnx_crypto_mining_indicators.yml"
build_date: "2026-04-26 17:03:19"
status: "stable"
level: "high"
logsource: "linux / network_connection"
aliases:
  - "a46c93b7-55ed-4d27-a41b-c259456c4746"
  - "Linux Crypto Mining Pool Connections"
attack_technique_ids:
  - "T1496"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Linux Crypto Mining Pool Connections

Detects process connections to a Monero crypto mining pool

## Metadata

- Rule ID: a46c93b7-55ed-4d27-a41b-c259456c4746
- Status: stable
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2021-10-26
- Source Path: rules/linux/network_connection/net_connection_lnx_crypto_mining_indicators.yml

## Logsource

- category: network_connection
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1496-resource_hijacking|T1496]]

## Detection

```yaml
selection:
  DestinationHostname:
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
  - moneroocean.stream
  - monerocean.stream
condition: selection
```

## False Positives

- Legitimate use of crypto miners

## References

- https://www.poolwatch.io/coin/monero

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/network_connection/net_connection_lnx_crypto_mining_indicators.yml)
