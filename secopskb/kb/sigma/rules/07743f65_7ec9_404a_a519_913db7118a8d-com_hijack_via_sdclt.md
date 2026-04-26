---
sigma_id: "07743f65-7ec9-404a-a519-913db7118a8d"
title: "COM Hijack via Sdclt"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_comhijack_sdclt.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_comhijack_sdclt.yml"
build_date: "2026-04-26 14:14:21"
status: "test"
level: "high"
logsource: "windows / registry_set"
aliases:
  - "07743f65-7ec9-404a-a519-913db7118a8d"
  - "COM Hijack via Sdclt"
attack_technique_ids:
  - "T1546"
  - "T1548"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[workspaces/index|Notes]]

# COM Hijack via Sdclt

Detects changes to 'HKCU\Software\Classes\Folder\shell\open\command\DelegateExecute'

## Metadata

- Rule ID: 07743f65-7ec9-404a-a519-913db7118a8d
- Status: test
- Level: high
- Author: Omkar Gudhate
- Date: 2020-09-27
- Modified: 2023-09-28
- Source Path: rules/windows/registry/registry_set/registry_set_comhijack_sdclt.yml

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1546-event_triggered_execution|T1546]]
- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548]]

## Detection

```yaml
selection:
  TargetObject|contains: \Software\Classes\Folder\shell\open\command\DelegateExecute
condition: selection
```

## False Positives

- Unknown

## References

- http://blog.sevagas.com/?Yet-another-sdclt-UAC-bypass
- https://www.exploit-db.com/exploits/47696

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_comhijack_sdclt.yml)
