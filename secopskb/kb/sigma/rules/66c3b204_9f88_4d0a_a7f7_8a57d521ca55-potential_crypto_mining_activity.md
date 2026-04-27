---
sigma_id: "66c3b204-9f88-4d0a-a7f7-8a57d521ca55"
title: "Potential Crypto Mining Activity"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_susp_crypto_mining_monero.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_crypto_mining_monero.yml"
build_date: "2026-04-27 19:13:53"
status: "stable"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "66c3b204-9f88-4d0a-a7f7-8a57d521ca55"
  - "Potential Crypto Mining Activity"
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
- product: windows

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
  - LS1kb25hdGUtbGV2ZWw9
  - 0tZG9uYXRlLWxldmVsP
  - tLWRvbmF0ZS1sZXZlbD
  - c3RyYXR1bSt0Y3A6Ly
  - N0cmF0dW0rdGNwOi8v
  - zdHJhdHVtK3RjcDovL
  - c3RyYXR1bSt1ZHA6Ly
  - N0cmF0dW0rdWRwOi8v
  - zdHJhdHVtK3VkcDovL
filter:
  CommandLine|contains:
  - ' pool.c '
  - ' pool.o '
  - gcc -
condition: selection and not filter
```

## False Positives

- Legitimate use of crypto miners
- Some build frameworks

## References

- https://www.poolwatch.io/coin/monero

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_susp_crypto_mining_monero.yml)
