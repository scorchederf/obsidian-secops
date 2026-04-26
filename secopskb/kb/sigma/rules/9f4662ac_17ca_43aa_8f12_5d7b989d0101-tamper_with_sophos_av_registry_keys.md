---
sigma_id: "9f4662ac-17ca-43aa-8f12-5d7b989d0101"
title: "Tamper With Sophos AV Registry Keys"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_sophos_av_tamper.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_sophos_av_tamper.yml"
build_date: "2026-04-26 14:14:38"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "9f4662ac-17ca-43aa-8f12-5d7b989d0101"
  - "Tamper With Sophos AV Registry Keys"
attack_technique_ids:
  - "T1562.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# Tamper With Sophos AV Registry Keys

Detects tamper attempts to sophos av functionality via registry key modification

## Metadata

- Rule ID: 9f4662ac-17ca-43aa-8f12-5d7b989d0101
- Status: test
- Level: high
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2022-09-02
- Modified: 2023-08-17
- Source Path: rules/windows/registry/registry_set/registry_set_sophos_av_tamper.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses|T1562.001]]

## Detection

```yaml
selection:
  TargetObject|contains:
  - \Sophos Endpoint Defense\TamperProtection\Config\SAVEnabled
  - \Sophos Endpoint Defense\TamperProtection\Config\SEDEnabled
  - \Sophos\SAVService\TamperProtection\Enabled
  Details: DWORD (0x00000000)
condition: selection
```

## False Positives

- Some FP may occur when the feature is disabled by the AV itself, you should always investigate if the action was legitimate

## References

- https://redacted.com/blog/bianlian-ransomware-gang-gives-it-a-go/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_sophos_av_tamper.yml)
