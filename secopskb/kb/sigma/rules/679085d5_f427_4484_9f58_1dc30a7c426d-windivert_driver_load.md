---
sigma_id: "679085d5-f427-4484-9f58-1dc30a7c426d"
title: "WinDivert Driver Load"
framework: "sigma"
generated: "true"
source_path: "rules/windows/driver_load/driver_load_win_windivert.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/driver_load/driver_load_win_windivert.yml"
build_date: "2026-04-26 15:01:54"
status: "test"
level: "high"
logsource: "windows / driver_load"
aliases:
  - "679085d5-f427-4484-9f58-1dc30a7c426d"
  - "WinDivert Driver Load"
attack_technique_ids:
  - "T1599.001"
  - "T1557.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[workspaces/index|Notes]]

# WinDivert Driver Load

Detects the load of the Windiver driver, a powerful user-mode capture/sniffing/modification/blocking/re-injection package for Windows

## Metadata

- Rule ID: 679085d5-f427-4484-9f58-1dc30a7c426d
- Status: test
- Level: high
- Author: Florian Roth (Nextron Systems)
- Date: 2021-07-30
- Modified: 2024-11-23
- Source Path: rules/windows/driver_load/driver_load_win_windivert.yml

## Logsource

- category: driver_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1599-network_boundary_bridging|T1599.001]]
- [[kb/attack/techniques/T1557-adversary-in-the-middle|T1557.001]]

## Detection

```yaml
selection:
- ImageLoaded|contains:
  - \WinDivert.sys
  - \WinDivert64.sys
  - \NordDivert.sys
  - \lingtiwfp.sys
  - \eswfp.sys
- Hashes|contains:
  - IMPHASH=0604bb7cb4bb851e2168d5c7d9399087
  - IMPHASH=2e5f0e649d97f32b03c09e4686d0574f
  - IMPHASH=52f8aa269f69f0edad9e8fcdaedce276
  - IMPHASH=c0e5d314da39dbf65a2dbff409cc2c76
  - IMPHASH=58623490691babe8330adc81cd04a663
  - IMPHASH=8ee39b48656e4d6b8459d7ba7da7438b
  - IMPHASH=45ee545ae77e8d43fc70ede9efcd4c96
  - IMPHASH=a1b2e245acd47e4a348e1a552a02859a
  - IMPHASH=2a5f85fe4609461c6339637594fa9b0a
  - IMPHASH=6b2c6f95233c2914d1d488ee27531acc
  - IMPHASH=9f2fdd3f9ab922bbb0560a7df46f4342
  - IMPHASH=d8a719865c448b1bd2ec241e46ac1c88
  - IMPHASH=0ea54f8c9af4a2fe8367fa457f48ed38
  - IMPHASH=9d519ae0a0864d6d6ae3f8b6c9c70af6
  - IMPHASH=a74929edfc3289895e3f2885278947ae
  - IMPHASH=a66b476c2d06c370f0a53b5537f2f11e
  - IMPHASH=bdcd836a46bc2415773f6b5ea77a46e4
  - IMPHASH=c28cd6ccd83179e79dac132a553693d9
condition: selection
```

## False Positives

- Legitimate WinDivert driver usage

## References

- https://reqrypt.org/windivert-doc.html
- https://rastamouse.me/ntlm-relaying-via-cobalt-strike/

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/driver_load/driver_load_win_windivert.yml)
