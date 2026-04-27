---
sigma_id: "0cf7a157-8879-41a2-8f55-388dd23746b7"
title: "Linux Recon Indicators"
framework: "sigma"
generated: "true"
source_path: "rules/linux/process_creation/proc_creation_lnx_susp_recon_indicators.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_susp_recon_indicators.yml"
build_date: "2026-04-27 19:13:52"
status: "test"
level: "high"
logsource: "linux / process_creation"
aliases:
  - "0cf7a157-8879-41a2-8f55-388dd23746b7"
  - "Linux Recon Indicators"
attack_technique_ids:
  - "T1592.004"
  - "T1552.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects events with patterns found in commands used for reconnaissance on linux systems

## Logsource

- category: process_creation
- product: linux

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1592-gather_victim_host_information#^t1592004-client-configurations|T1592.004: Client Configurations]]
- [[kb/attack/techniques/T1552-unsecured_credentials#^t1552001-credentials-in-files|T1552.001: Credentials In Files]]

## Detection

```yaml
selection:
  CommandLine|contains:
  - ' -name .htpasswd'
  - ' -perm -4000 '
condition: selection
```

## False Positives

- Legitimate administration activities

## References

- https://github.com/sleventyeleven/linuxprivchecker/blob/0d701080bbf92efd464e97d71a70f97c6f2cd658/linuxprivchecker.py

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/linux/process_creation/proc_creation_lnx_susp_recon_indicators.yml)
