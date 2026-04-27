---
sigma_id: "0e0255bf-2548-47b8-9582-c0955c9283f5"
title: "Suspicious Reg Add BitLocker"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_reg_bitlocker.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_reg_bitlocker.yml"
build_date: "2026-04-27 19:13:57"
status: "test"
level: "high"
logsource: "windows / process_creation"
aliases:
  - "0e0255bf-2548-47b8-9582-c0955c9283f5"
  - "Suspicious Reg Add BitLocker"
attack_technique_ids:
  - "T1486"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects suspicious addition to BitLocker related registry keys via the reg.exe utility

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1486-data_encrypted_for_impact|T1486: Data Encrypted for Impact]]

## Detection

```yaml
selection:
  CommandLine|contains|all:
  - REG
  - ADD
  - \SOFTWARE\Policies\Microsoft\FVE
  - /v
  - /f
  CommandLine|contains:
  - EnableBDEWithNoTPM
  - UseAdvancedStartup
  - UseTPM
  - UseTPMKey
  - UseTPMKeyPIN
  - RecoveryKeyMessageSource
  - UseTPMPIN
  - RecoveryKeyMessage
condition: selection
```

## False Positives

- Unlikely

## References

- https://thedfirreport.com/2021/11/15/exchange-exploit-leads-to-domain-wide-ransomware/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_reg_bitlocker.yml)
