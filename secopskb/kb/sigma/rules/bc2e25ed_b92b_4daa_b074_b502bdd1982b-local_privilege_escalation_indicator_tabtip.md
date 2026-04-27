---
sigma_id: "bc2e25ed-b92b-4daa-b074-b502bdd1982b"
title: "Local Privilege Escalation Indicator TabTip"
framework: "sigma"
generated: "true"
source_path: "rules/windows/builtin/system/microsoft_windows_distributed_com/win_system_lpe_indicators_tabtip.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/microsoft_windows_distributed_com/win_system_lpe_indicators_tabtip.yml"
build_date: "2026-04-27 19:13:52"
status: "test"
level: "high"
logsource: "windows / system"
aliases:
  - "bc2e25ed-b92b-4daa-b074-b502bdd1982b"
  - "Local Privilege Escalation Indicator TabTip"
attack_technique_ids:
  - "T1557.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the invocation of TabTip via CLSID as seen when JuicyPotatoNG is used on a system in brute force mode

## Logsource

- product: windows
- service: system

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1557-adversary-in-the-middle#^t1557001-llmnr-nbt-ns-poisoning-and-smb-relay|T1557.001: LLMNR/NBT-NS Poisoning and SMB Relay]]

## Detection

```yaml
selection:
  Provider_Name: Microsoft-Windows-DistributedCOM
  EventID: 10001
  param1: C:\Program Files\Common Files\microsoft shared\ink\TabTip.exe
  param2: 2147943140
  param3: '{054AAE20-4BEA-4347-8A35-64A533254A9D}'
condition: selection
```

## False Positives

- Unknown

## References

- https://github.com/antonioCoco/JuicyPotatoNG

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/builtin/system/microsoft_windows_distributed_com/win_system_lpe_indicators_tabtip.yml)
