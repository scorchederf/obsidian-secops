---
sigma_id: "948a0953-f287-4806-bbcb-3b2e396df89f"
title: "Unsigned Mfdetours.DLL Sideloading"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_side_load_mfdetours_unsigned.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_mfdetours_unsigned.yml"
build_date: "2026-04-27 19:13:58"
status: "test"
level: "high"
logsource: "windows / image_load"
aliases:
  - "948a0953-f287-4806-bbcb-3b2e396df89f"
  - "Unsigned Mfdetours.DLL Sideloading"
attack_technique_ids:
  - "T1574.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects DLL sideloading of unsigned "mfdetours.dll". Executing "mftrace.exe" can be abused to attach to an arbitrary process and force load any DLL named "mfdetours.dll" from the current directory of execution.

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow#^t1574001-dll|T1574.001: DLL]]

## Detection

```yaml
selection:
  ImageLoaded|endswith: \mfdetours.dll
filter_main_legit_path:
  ImageLoaded|contains: :\Program Files (x86)\Windows Kits\10\bin\
  SignatureStatus: Valid
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unlikely

## References

- Internal Research

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_mfdetours_unsigned.yml)
