---
sigma_id: "9f4662ac-17ca-43aa-8f12-5d7b989d0101"
title: "Tamper With Sophos AV Registry Keys"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_sophos_av_tamper.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_sophos_av_tamper.yml"
build_date: "2026-04-27 19:13:57"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects tamper attempts to sophos av functionality via registry key modification

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses#^t1562001-disable-or-modify-tools|T1562.001: Disable or Modify Tools]]

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
