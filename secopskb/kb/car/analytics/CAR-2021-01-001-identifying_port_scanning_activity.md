---
car_id: "CAR-2021-01-001"
title: "Identifying Port Scanning Activity"
framework: "car"
generated: "true"
source_url: "https://car.mitre.org/analytics/CAR-2021-01-001/"
repo_url: "https://github.com/mitre-attack/car/blob/master/analytics/CAR-2021-01-001.yaml"
build_date: "2026-04-27 19:03:49"
aliases:
  - "CAR-2021-01-001"
  - "Identifying Port Scanning Activity"
attack_technique_ids:
  - "T1046"
platforms:
  - "Windows"
  - "Linux"
implementation_types:
  - "Splunk"
tags:
  - "car"
  - "analytic"
  - "detection"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

After compromising an initial machine, adversaries commonly attempt to laterally move across the network. The first step to attempt the lateral movement often involves conducting host identification, port and service scans on the internal network via the compromised machine using tools such as Nmap, Cobalt Strike, etc.

## ATT&CK Coverage

- [[kb/attack/techniques/T1046-network_service_discovery|T1046: Network Service Discovery]] (coverage: Moderate; tactics: TA0007)

## Implementations

### Splunk

It should be noted that when a host/ port/ service scan is performed from a compromised machine, a single machine makes multiple calls to other hosts in the network to identify live hosts and services. This can be detected using the following query

- Data Model: Sysmon native

```splunk
sourcetype='firewall_logs' dest_ip = 'internal_subnet' | stats dc(dest_port) as pcount by src_ip | where pcount >5
```

## Data Model References

- flow/start/dest_ip

## D3FEND Mappings

- [[kb/defend/techniques/D3-CAA-connection_attempt_analysis|D3-CAA: Connection Attempt Analysis]]

## Source

- [CAR website](https://car.mitre.org/analytics/CAR-2021-01-001/)
- [Source YAML](https://github.com/mitre-attack/car/blob/master/analytics/CAR-2021-01-001.yaml)
