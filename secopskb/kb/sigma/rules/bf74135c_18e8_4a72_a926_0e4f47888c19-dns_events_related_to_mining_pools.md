---
sigma_id: "bf74135c-18e8-4a72-a926-0e4f47888c19"
title: "DNS Events Related To Mining Pools"
framework: "sigma"
generated: "true"
source_path: "rules/network/zeek/zeek_dns_mining_pools.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/network/zeek/zeek_dns_mining_pools.yml"
build_date: "2026-04-26 14:14:23"
status: "test"
level: "low"
logsource: "zeek / dns"
aliases:
  - "bf74135c-18e8-4a72-a926-0e4f47888c19"
  - "DNS Events Related To Mining Pools"
attack_technique_ids:
  - "T1569.002"
  - "T1496"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# DNS Events Related To Mining Pools

Identifies clients that may be performing DNS lookups associated with common currency mining pools.

## Metadata

- Rule ID: bf74135c-18e8-4a72-a926-0e4f47888c19
- Status: test
- Level: low
- Author: Saw Winn Naung, Azure-Sentinel, @neu5ron
- Date: 2021-08-19
- Modified: 2022-07-07
- Source Path: rules/network/zeek/zeek_dns_mining_pools.yml

## Logsource

- product: zeek
- service: dns

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1569-system_services|T1569.002]]
- [[kb/attack/techniques/T1496-resource_hijacking|T1496]]

## Detection

```yaml
selection:
  query|endswith:
  - monerohash.com
  - do-dear.com
  - xmrminerpro.com
  - secumine.net
  - xmrpool.com
  - minexmr.org
  - hashanywhere.com
  - xmrget.com
  - mininglottery.eu
  - minergate.com
  - moriaxmr.com
  - multipooler.com
  - moneropools.com
  - xmrpool.eu
  - coolmining.club
  - supportxmr.com
  - minexmr.com
  - hashvault.pro
  - xmrpool.net
  - crypto-pool.fr
  - xmr.pt
  - miner.rocks
  - walpool.com
  - herominers.com
  - gntl.co.uk
  - semipool.com
  - coinfoundry.org
  - cryptoknight.cc
  - fairhash.org
  - baikalmine.com
  - tubepool.xyz
  - fairpool.xyz
  - asiapool.io
  - coinpoolit.webhop.me
  - nanopool.org
  - moneropool.com
  - miner.center
  - prohash.net
  - poolto.be
  - cryptoescrow.eu
  - monerominers.net
  - cryptonotepool.org
  - extrmepool.org
  - webcoin.me
  - kippo.eu
  - hashinvest.ws
  - monero.farm
  - linux-repository-updates.com
  - 1gh.com
  - dwarfpool.com
  - hash-to-coins.com
  - pool-proxy.com
  - hashfor.cash
  - fairpool.cloud
  - litecoinpool.org
  - mineshaft.ml
  - abcxyz.stream
  - moneropool.ru
  - cryptonotepool.org.uk
  - extremepool.org
  - extremehash.com
  - hashinvest.net
  - unipool.pro
  - crypto-pools.org
  - monero.net
  - backup-pool.com
  - mooo.com
  - freeyy.me
  - cryptonight.net
  - shscrypto.net
exclude_answers:
  answers:
  - 127.0.0.1
  - 0.0.0.0
exclude_rejected:
  rejected: 'true'
condition: selection and not 1 of exclude_*
```

## False Positives

- A DNS lookup does not necessarily  mean a successful attempt, verify a) if there was a response using the zeek answers field, if there was then verify the connections (conn.log) to those IPs. b) verify if HTTP, SSL, or TLS activity to the domain that was queried. http.log field is 'host' and ssl/tls is 'server_name'.

## References

- https://github.com/Azure/Azure-Sentinel/blob/fa0411f9424b6c47b4d5a20165e4f1b168c1f103/Detections/ASimDNS/imDNS_Miners.yaml

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/network/zeek/zeek_dns_mining_pools.yml)
