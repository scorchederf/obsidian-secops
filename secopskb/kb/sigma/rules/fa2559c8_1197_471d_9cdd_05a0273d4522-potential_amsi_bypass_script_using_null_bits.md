---
sigma_id: "fa2559c8-1197-471d-9cdd-05a0273d4522"
title: "Potential AMSI Bypass Script Using NULL Bits"
framework: "sigma"
generated: "true"
source_path: "rules/windows/powershell/powershell_script/posh_ps_amsi_null_bits_bypass.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_amsi_null_bits_bypass.yml"
build_date: "2026-04-26 14:14:31"
status: "test"
level: "medium"
logsource: "windows / ps_script"
aliases:
  - "fa2559c8-1197-471d-9cdd-05a0273d4522"
  - "Potential AMSI Bypass Script Using NULL Bits"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Potential AMSI Bypass Script Using NULL Bits

Detects usage of special strings/null bits in order to potentially bypass AMSI functionalities

## Metadata

- Rule ID: fa2559c8-1197-471d-9cdd-05a0273d4522
- Status: test
- Level: medium
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2023-01-04
- Modified: 2023-05-09
- Source Path: rules/windows/powershell/powershell_script/posh_ps_amsi_null_bits_bypass.yml

## Logsource

- category: ps_script
- definition: Requirements: Script Block Logging must be enabled
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Detection

```yaml
selection:
  ScriptBlockText|contains:
  - if(0){{{0}}}' -f $(0 -as [char]) +
  - '#<NULL>'
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/r00t-3xp10it/hacking-material-books/blob/43cb1e1932c16ff1f58b755bc9ab6b096046853f/obfuscation/simple_obfuscation.md#amsi-bypass-using-null-bits-satoshi

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/powershell/powershell_script/posh_ps_amsi_null_bits_bypass.yml)
