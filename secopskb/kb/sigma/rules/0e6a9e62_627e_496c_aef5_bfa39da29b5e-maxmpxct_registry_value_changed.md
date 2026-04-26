---
sigma_id: "0e6a9e62-627e-496c-aef5-bfa39da29b5e"
title: "MaxMpxCt Registry Value Changed"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_optimize_file_sharing_network.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_optimize_file_sharing_network.yml"
build_date: "2026-04-26 14:14:29"
status: "test"
level: "low"
logsource: "windows / registry_set"
aliases:
  - "0e6a9e62-627e-496c-aef5-bfa39da29b5e"
  - "MaxMpxCt Registry Value Changed"
attack_technique_ids:
  - "T1070.005"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# MaxMpxCt Registry Value Changed

Detects changes to the "MaxMpxCt" registry value.
MaxMpxCt specifies the maximum outstanding network requests for the server per client, which is used when negotiating a Server Message Block (SMB) connection with a client. Note if the value is set beyond 125 older Windows 9x clients will fail to negotiate.
Ransomware threat actors and operators (specifically BlackCat) were seen increasing this value in order to handle a higher volume of traffic.

## Metadata

- Rule ID: 0e6a9e62-627e-496c-aef5-bfa39da29b5e
- Status: test
- Level: low
- Author: Nasreddine Bencherchali (Nextron Systems)
- Date: 2024-03-19
- Source Path: rules/windows/registry/registry_set/registry_set_optimize_file_sharing_network.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1070-indicator_removal|T1070.005]]

## Detection

```yaml
selection:
  TargetObject|endswith: \Services\LanmanServer\Parameters\MaxMpxCt
condition: selection
```

## False Positives

- Unknown

## References

- https://www.huntress.com/blog/blackcat-ransomware-affiliate-ttps
- https://securityscorecard.com/research/deep-dive-into-alphv-blackcat-ransomware
- https://www.intrinsec.com/alphv-ransomware-gang-analysis/?cn-reloaded=1
- https://www.sentinelone.com/labs/blackcat-ransomware-highly-configurable-rust-driven-raas-on-the-prowl-for-victims/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_optimize_file_sharing_network.yml)
