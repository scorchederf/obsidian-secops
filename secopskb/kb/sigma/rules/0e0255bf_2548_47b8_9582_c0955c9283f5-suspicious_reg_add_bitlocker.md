---
sigma_id: "0e0255bf-2548-47b8-9582-c0955c9283f5"
title: "Suspicious Reg Add BitLocker"
framework: "sigma"
generated: "true"
source_path: "rules/windows/process_creation/proc_creation_win_reg_bitlocker.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/process_creation/proc_creation_win_reg_bitlocker.yml"
build_date: "2026-04-26 14:14:37"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Suspicious Reg Add BitLocker

Detects suspicious addition to BitLocker related registry keys via the reg.exe utility

## Metadata

- Rule ID: 0e0255bf-2548-47b8-9582-c0955c9283f5
- Status: test
- Level: high
- Author: frack113
- Date: 2021-11-15
- Modified: 2022-09-09
- Source Path: rules/windows/process_creation/proc_creation_win_reg_bitlocker.yml

## Logsource

- category: process_creation
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1486-data_encrypted_for_impact|T1486]]

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
