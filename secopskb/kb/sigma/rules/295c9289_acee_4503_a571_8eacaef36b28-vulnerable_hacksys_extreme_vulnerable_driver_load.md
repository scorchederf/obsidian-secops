---
sigma_id: "295c9289-acee-4503-a571-8eacaef36b28"
title: "Vulnerable HackSys Extreme Vulnerable Driver Load"
framework: "sigma"
generated: "true"
source_path: "rules/windows/driver_load/driver_load_win_vuln_hevd_driver.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/driver_load/driver_load_win_vuln_hevd_driver.yml"
build_date: "2026-04-26 17:03:24"
status: "test"
level: "high"
logsource: "windows / driver_load"
aliases:
  - "295c9289-acee-4503-a571-8eacaef36b28"
  - "Vulnerable HackSys Extreme Vulnerable Driver Load"
attack_technique_ids:
  - "T1543.003"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# Vulnerable HackSys Extreme Vulnerable Driver Load

Detects the load of HackSys Extreme Vulnerable Driver which is an intentionally vulnerable Windows driver developed for security enthusiasts to learn and polish their exploitation skills at Kernel level and often abused by threat actors

## Metadata

- Rule ID: 295c9289-acee-4503-a571-8eacaef36b28
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-08-18
- Modified: 2024-11-23
- Source Path: rules/windows/driver_load/driver_load_win_vuln_hevd_driver.yml

## Logsource

- category: driver_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1543-create_or_modify_system_process|T1543.003]]

## Detection

```yaml
selection:
- ImageLoaded|endswith: \HEVD.sys
- Hashes|contains:
  - IMPHASH=f26d0b110873a1c7d8c4f08fbeab89c5
  - IMPHASH=c46ea2e651fd5f7f716c8867c6d13594
condition: selection
```

## False Positives

- Unlikely

## References

- https://github.com/hacksysteam/HackSysExtremeVulnerableDriver

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/driver_load/driver_load_win_vuln_hevd_driver.yml)
