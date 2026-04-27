---
sigma_id: "71b31e99-9ad0-47d4-aeb5-c0ca3928eeeb"
title: "Potential Waveedit.DLL Sideloading"
framework: "sigma"
generated: "true"
source_path: "rules/windows/image_load/image_load_side_load_waveedit.yml"
source_url: "https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_waveedit.yml"
build_date: "2026-04-27 19:13:54"
status: "test"
level: "high"
logsource: "windows / image_load"
aliases:
  - "71b31e99-9ad0-47d4-aeb5-c0ca3928eeeb"
  - "Potential Waveedit.DLL Sideloading"
attack_technique_ids:
  - "T1574.001"
tags:
  - "sigma"
  - "detection-rule"
---

[[index|Home]] • [[kb/attack/index|ATT&CK]] • [[kb/tools/index|Tools]] • [[kb/defend/index|D3FEND]] • [[kb/car/index|CAR]] • [[kb/sigma/index|Sigma]] • [[kb/atomic/index|Atomic]] • [[kb/lolbas/index|LOLBAS]] • [[workspaces/index|Notes]]

Detects potential DLL sideloading of "waveedit.dll", which is part of the Nero WaveEditor audio editing software.

## Logsource

- category: image_load
- product: windows

## ATT&CK Mapping

### Techniques

- [[kb/attack/techniques/T1574-hijack_execution_flow#^t1574001-dll|T1574.001: DLL]]

## Detection

```yaml
selection:
  ImageLoaded|endswith: \waveedit.dll
filter_main_legit_path:
  Image:
  - C:\Program Files (x86)\Nero\Nero Apps\Nero WaveEditor\waveedit.exe
  - C:\Program Files\Nero\Nero Apps\Nero WaveEditor\waveedit.exe
  ImageLoaded|startswith:
  - C:\Program Files (x86)\Nero\Nero Apps\Nero WaveEditor\
  - C:\Program Files\Nero\Nero Apps\Nero WaveEditor\
condition: selection and not 1 of filter_main_*
```

## False Positives

- Unlikely

## References

- https://www.trendmicro.com/en_us/research/23/f/behind-the-scenes-unveiling-the-hidden-workings-of-earth-preta.html

## Source

- [Source YAML](https://github.com/SigmaHQ/sigma/blob/master/rules/windows/image_load/image_load_side_load_waveedit.yml)
