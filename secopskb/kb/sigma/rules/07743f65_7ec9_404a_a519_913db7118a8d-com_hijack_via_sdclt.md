---
sigma_id: "07743f65-7ec9-404a-a519-913db7118a8d"
title: "COM Hijack via Sdclt"
framework: "sigma"
generated: "true"
source_path: "rules/windows/registry/registry_set/registry_set_comhijack_sdclt.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/registry/registry_set/registry_set_comhijack_sdclt.yml"
build_date: "2026-04-27 19:13:50"
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

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects changes to 'HKCU\Software\Classes\Folder\shell\open\command\DelegateExecute'

## Logsource

- category: registry_set
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1546-event_triggered_execution|T1546: Event Triggered Execution]]
- [[kb/attack/techniques/T1548-abuse_elevation_control_mechanism|T1548: Abuse Elevation Control Mechanism]]

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
