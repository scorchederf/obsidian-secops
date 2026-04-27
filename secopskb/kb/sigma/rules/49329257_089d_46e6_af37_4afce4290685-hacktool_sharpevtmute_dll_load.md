---
sigma_id: "49329257-089d-46e6-af37-4afce4290685"
title: "HackTool - SharpEvtMute DLL Load"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_hktl_sharpevtmute.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_hktl_sharpevtmute.yml"
build_date: "2026-04-27 19:13:51"
status: "test"
level: "high"
logsource: "windows / image_load"
aliases:
  - "49329257-089d-46e6-af37-4afce4290685"
  - "HackTool - SharpEvtMute DLL Load"
attack_technique_ids:
  - "T1562.002"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects the load of EvtMuteHook.dll, a key component of SharpEvtHook, a tool that tampers with the Windows event logs

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1562-impair_defenses#^t1562002-disable-windows-event-logging|T1562.002: Disable Windows Event Logging]]

## Detection

```yaml
selection:
  Hashes|contains: IMPHASH=330768A4F172E10ACB6287B87289D83B
condition: selection
```

## False Positives

- Other DLLs with the same Imphash

## References

- https://github.com/bats3c/EvtMute

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_hktl_sharpevtmute.yml)
