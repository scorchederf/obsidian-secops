---
sigma_id: "9069ea3c-b213-4c52-be13-86506a227ab1"
title: "Linux Crypto Mining Indicators"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_crypto_mining.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_crypto_mining.yml"
build_date: "2026-04-27 19:13:52"
status: "test"
level: "high"
logsource: "linux / process_creation"
aliases:
  - "9069ea3c-b213-4c52-be13-86506a227ab1"
  - "Linux Crypto Mining Indicators"
attack_technique_ids:
  - "T1496"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects command line parameters or strings often used by crypto miners

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1496-resource_hijacking|T1496: Resource Hijacking]]

## Detection

```yaml
selection:
  CommandLine|contains:
  - ' --cpu-priority='
  - --donate-level=0
  - ' -o pool.'
  - ' --nicehash'
  - ' --algo=rx/0 '
  - stratum+tcp://
  - stratum+udp://
  - sh -c /sbin/modprobe msr allow_writes=on
  - LS1kb25hdGUtbGV2ZWw9
  - 0tZG9uYXRlLWxldmVsP
  - tLWRvbmF0ZS1sZXZlbD
  - c3RyYXR1bSt0Y3A6Ly
  - N0cmF0dW0rdGNwOi8v
  - zdHJhdHVtK3RjcDovL
  - c3RyYXR1bSt1ZHA6Ly
  - N0cmF0dW0rdWRwOi8v
  - zdHJhdHVtK3VkcDovL
condition: selection
```

## False Positives

- Legitimate use of crypto miners

## References

- https://www.poolwatch.io/coin/monero

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_crypto_mining.yml)
